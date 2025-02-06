import tkinter as tk
from tkinter import messagebox

file_name = 'lbtest.txt'

root = tk.Tk()

root = root
root.title("Список задач!!!")
root.geometry("600x600")

tasks = []
arr = []

def update_task_listbox():
    task_listbox.delete(0, tk.END)

    with open(file_name, 'r') as file:
        lines = file.readlines()  # Читаем все строки из файла

    for task in tasks:
        task_text = task["task"]
        if task["done"]:
            if len(lines) == 0:
                with open(file_name, 'a') as file:
                    arr.append(task_text)
                    file.write(task_text + '\n')

            if task_text not in arr:
                arr.append(task_text)
                print(task_text)
                with open(file_name, 'a') as file:
                    file.write(task_text + '\n')                

            task_text += " ✔"
        task_listbox.insert(tk.END, task_text)

# Добавление задачи!
def add_task():      
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        update_task_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Что-то пошло не так!!", "Введите задачу!")

# Удаление задачи!
def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        with open(file_name, 'r') as file:
            lines = file.readlines()  # Читаем все строки из файла

        with open(file_name, 'w') as file:
            for line in lines:
                for task in tasks:
                    if line.strip() != task["task"]:  # Удаляем только если строка совпадает с нужным словом
                        file.write(line)

        update_task_listbox()
    else:
        messagebox.showwarning("Что-то пошло не так!!!", "Выберите задачу для удаления!")

# Отметка задачи!
def mark_task_done():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]["done"] = True
        update_task_listbox()
    else:
        messagebox.showwarning("Что-то пошло не так!!!", "Выберите задачу для отметки!")

# Элементы интерфейса
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Добавить", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

remove_button = tk.Button(root, text="Удалить", command=remove_task)
remove_button.grid(row=2, column=0, padx=10, pady=10)

mark_done_button = tk.Button(root, text="Отметить выполненной", command=mark_task_done)
mark_done_button.grid(row=2, column=1, padx=10, pady=10)
       
root.mainloop()