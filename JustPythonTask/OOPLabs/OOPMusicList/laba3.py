'''
Создать систему управления музыкальной библиотекой, которая
позволяет добавлять песни, альбомы и отслеживать исполнителей.
'''

class Song:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.duration} мин)"

class Album:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        songs_info = "\n".join([f"  - {song}" for song in self.songs])
        return f"Альбом: {self.name} ({self.year})\n{songs_info}"

class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def __str__(self):
        albums_info = "\n".join([f"- {album}" for album in self.albums])
        return f"Исполнитель: {self.name} \n {albums_info}"

class MusicLib:
    def __init__(self):
        self.artists = []

    def add_artist(self, artist):
        self.artists.append(artist)

    def find_artist(self, name):
        for artist in self.artists:
            if artist.name == name:
                return artist
        return None

    def __str__(self):
        artists_info = "\n\n".join([str(artist) for artist in self.artists])
        return f"Музыкальная библиотека: \n {artists_info}"

library = MusicLib()

while True:
    print("\n Меню:")
    print("1. Добавить исполнителя")
    print("2. Добавить альбом")
    print("3. Добавить песню")
    print("4. Показать библиотеку")
    print("5. Выйти")

    choice = input("\n Выберите действие: ")

    if choice == "1":
        name = input("Введите имя исполнителя: ")
        artist = Artist(name)
        library.add_artist(artist)
        print(f"Исполнитель {name} добавлен!!!")
    elif choice == "2":
        artist_name = input("Введите имя исполнителя: ")
        artist = library.find_artist(artist_name)
        if artist:
            album_name = input("Введите название альбома: ")
            year = input("Введите год выпуска альбома: ")
            album = Album(album_name, year)
            artist.add_album(album)
            print(f"Альбом {album_name} добавлен к исполнителю {artist_name}.")
        else:
            print(f"Исполнитель {artist_name} не найден!!!")
    elif choice == "3":
        artist_name = input("Введите имя исполнителя: ")
        artist = library.find_artist(artist_name)
        if artist:
            album_name = input("Введите название альбома: ")
            album = next((a for a in artist.albums if a.name == album_name), None)
            if album:
                song_title = input("Введите название песни: ")
                song_duration = input("Введите продолжительность песни (в минутах): ")
                song = Song(song_title, song_duration)
                album.add_song(song)
                print(f"Песня {song_title} добавлена в альбом {album_name}.")
            else:
                print(f"Альбом {album_name} не найден!!!")
        else:
            print(f"Исполнитель {artist_name} не найден!!!")
    elif choice == "4":
        print(library)
    elif choice == "5":
        print("Выход из программы. Спасибо за внимание!!!")
        break
    else:
        print("Что-то пошло не так:) Попробуйте снова!!!")