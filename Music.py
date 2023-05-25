from abc import ABC, abstractmethod


class MusicOperations(ABC):
    @abstractmethod
    def search_song(self, title):
        pass

    @abstractmethod
    def play_song(self, title):
        pass


class Song:
    def __init__(self, title, artist, length):
        self.__title = title
        self.__artist = artist
        self.length = length

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_artist(self, artist):
        self.__artist = artist

    def get_artist(self):
        return self.__artist

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.length} minutes)"


class Album:
    def __init__(self, title, artist, release_date, songs):
        self.title = title
        self.artist = artist
        self.release_date = release_date
        self.songs = songs

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.release_date})"


class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def __str__(self):
        return f"{self.name} ({len(self.songs)} songs)"


class RockMusic(MusicOperations):
    def __init__(self):
        self.songs = []

    def search_song(self, title):
        for song in self.songs:
            if song.title.lower() == title.lower():
                return song
        return None

    def play_song(self, title):
        song = self.search_song(title)
        if song:
            print(f"Playing {song}")
        else:
            print(f"{title} not found in the rock music library.")

    def add_song(self, song):
        self.songs.append(song)


class PopMusic(MusicOperations):
    def __init__(self):
        self.songs = []

    def search_song(self, title):
        for song in self.songs:
            if song.title.lower() == title.lower():
                return song
        return None

    def play_song(self, title):
        song = self.search_song(title)
        if song:
            print(f"Playing {song}")
        else:
            print(f"{title} not found in the pop music library.")

    def add_song(self, song):
        self.songs.append(song)


# Example usage
song1 = Song("Stairway to Heaven", "Led Zeppelin", 8)
song2 = Song("Bohemian Rhapsody", "Queen", 6)
song3 = Song("Purple Haze", "Jimi Hendrix", 5)
song4 = Song("Like a Rolling Stone", "Bob Dylan", 6)

rock_music = RockMusic()
rock_music.add_song(song1)
rock_music.add_song(song3)

pop_music = PopMusic()
pop_music.add_song(song2)
pop_music.add_song(song4)

rock_music.play_song("Stairway to Heaven")
pop_music.play_song("Bohemian Rhapsody")

rock_playlist = Playlist("Rock Classics", [song1, song3])
pop_playlist = Playlist("Pop Hits", [song2, song4])

print(rock_playlist)
print(pop_playlist)
