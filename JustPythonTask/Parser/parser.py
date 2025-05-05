import requests
from bs4 import BeautifulSoup
import csv
from tabulate import tabulate
import matplotlib.pyplot as plt
import os
from urllib.parse import urljoin

# Настройки
BASE_URL = "https://en.wikipedia.org"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Создаем папки для сохранения данных
os.makedirs('text_content', exist_ok=True)
os.makedirs('external_links', exist_ok=True)

# Обновленный список страниц Wikipedia с гарантированно работающими примерами
wikipedia_pages = [
    'Python_(programming_language)',
    'JavaScript',
    'Java_(programming_language)',
    'C_(programming_language)',
    'C%2B%2B',  # Экранированная версия для C++
    'Ruby_(programming_language)',
    'PHP',
    'SQL',
    'HTML',
    'CSS',
    'Algorithm',
    'Data_structure',
    'Artificial_intelligence',
    'Machine_learning',
    'Computer_science',
    'Software_engineering',
    'Database',
    'Operating_system',
    'Computer_network',
    'Computer_programming'
]

def get_page_content(url):
    """Безопасное получение содержимого страницы"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Ошибка при получении страницы: {e}")
        return None

def extract_main_content(soup):
    """Извлекаем основной контент статьи"""
    content = soup.find('div', {'id': 'mw-content-text'})
    if not content:
        content = soup.find('div', {'class': 'mw-parser-output'})
    return content

def save_text_content(title, soup):
    """Сохраняем заголовок и первый осмысленный абзац"""
    try:
        # Извлекаем заголовок
        title_header = soup.find('h1', {'id': 'firstHeading'})
        article_title = title_header.text if title_header else title.replace('_', ' ')
        
        # Ищем первый содержательный абзац
        content = extract_main_content(soup)
        first_paragraph = ""
        
        if content:
            for p in content.find_all('p'):
                if p.text.strip() and len(p.text.strip()) > 50:  # Отсеиваем короткие/пустые параграфы
                    first_paragraph = p.text.strip()
                    break
        
        with open(f'text_content/{title}.txt', 'w', encoding='utf-8') as f:
            f.write(f"Title: {article_title}\n\n")
            f.write(first_paragraph if first_paragraph else "Не удалось извлечь содержание")
            
        return article_title, first_paragraph
    except Exception as e:
        print(f"Ошибка при сохранении текста: {e}")
        return title.replace('_', ' '), ""

def extract_external_links(soup, base_url):
    """Извлекаем все внешние ссылки со страницы"""
    external_links = []
    try:
        # Ищем все внешние ссылки в основном контенте
        content = extract_main_content(soup)
        if content:
            for link in content.find_all('a', {'class': 'external'}):
                href = link.get('href', '')
                if href.startswith('http'):
                    external_links.append({
                        'name': link.text.strip() or href,
                        'url': href
                    })
            
            # Дополнительно проверяем раздел "External links"
            dls_links_section = soup.find('span', {'id': 'External_links'})
            if not dls_links_section:
                dls_links_section = soup.find('h2', string='External links')
            
            if dls_links_section:
                ul = dls_links_section.find_next('ul')
                if ul:
                    for li in ul.find_all('li'):
                        link = li.find('a', {'class': 'external'}) or li.find('a', rel='nofollow')
                        if link and link.get('href'):
                            href = link['href']
                            if not href.startswith('http'):
                                href = urljoin(base_url, href)
                            external_links.append({
                                'name': link.text.strip() or href,
                                'url': href
                            })
    except Exception as e:
        print(f"Ошибка при извлечении ссылок: {e}")
    
    return external_links

def save_external_links(title, links):
    """Сохраняем внешние ссылки в CSV"""
    try:
        with open(f'external_links/{title}_links.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['name', 'url'])
            writer.writeheader()
            writer.writerows(links)
        return len(links)
    except Exception as e:
        print(f"Ошибка при сохранении ссылок: {e}")
        return 0

def extract_infobox(soup):
    """Извлекаем данные из инфобокса"""
    infobox = soup.find('table', {'class': 'infobox'})
    if not infobox:
        return None
    
    infobox_data = []
    for row in infobox.find_all('tr'):
        th = row.find('th')
        td = row.find('td')
        if th and td:
            infobox_data.append([th.get_text('\n', strip=True), 
                               td.get_text('\n', strip=True)])
    return infobox_data

def analyze_page(soup):
    """Анализируем страницу"""
    content = extract_main_content(soup)
    if not content:
        return 0, 0
    
    paragraphs = len(content.find_all('p', recursive=True))
    links = len(content.find_all('a', recursive=True))
    return paragraphs, links

# Основной цикл обработки
stats = []
for page in wikipedia_pages:
    print(f"\nОбрабатываем: {page}")
    url = f"{BASE_URL}/wiki/{page}"
    soup = get_page_content(url)
    
    if not soup:
        print(f"Не удалось загрузить страницу: {page}")
        stats.append({
            'title': page.replace('_', ' '),
            'paragraphs': 0,
            'links': 0,
            'external_links': 0
        })
        continue
    
    try:
        # Извлекаем и сохраняем текст
        title, _ = save_text_content(page, soup)
        
        # Извлекаем и сохраняем внешние ссылки
        ext_links = extract_external_links(soup, BASE_URL)
        ext_links_count = save_external_links(page, ext_links)
        
        # Извлекаем инфобокс
        infobox_data = extract_infobox(soup)
        if infobox_data:
            print(f"\nИнфобокс для {title}:")
            print(tabulate(infobox_data, headers=['Атрибут', 'Значение'], tablefmt='grid'))
        
        # Анализируем страницу
        paragraphs, links = analyze_page(soup)
        
        stats.append({
            'title': title,
            'paragraphs': paragraphs,
            'links': links,
            'external_links': ext_links_count
        })
        
    except Exception as e:
        print(f"Ошибка при обработке страницы {page}: {e}")
        stats.append({
            'title': page.replace('_', ' '),
            'paragraphs': 0,
            'links': 0,
            'external_links': 0
        })

# Выводим статистику
print("\nСводная статистика:")
print(tabulate(stats, headers='keys', tablefmt='grid'))

# Визуализация
if stats:
    titles = [s['title'] for s in stats]
    paragraphs = [s['paragraphs'] for s in stats]
    links = [s['links'] for s in stats]
    ext_links = [s['external_links'] for s in stats]

    plt.figure(figsize=(15, 6))
    
    # График количества параграфов
    plt.subplot(1, 2, 1)
    plt.barh(titles, paragraphs, color='skyblue')
    plt.title('Количество параграфов')
    plt.xlabel('Количество')
    plt.tight_layout()

    # График количества внешних ссылок
    plt.subplot(1, 2, 2)
    plt.barh(titles, ext_links, color='lightgreen')
    plt.title('Количество внешних ссылок')
    plt.xlabel('Количество')
    plt.tight_layout()

    plt.show()