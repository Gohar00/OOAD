from abc import ABC, abstractmethod


class Song:
    def __init__(self, title, artist, length):
        self.title = title
        self.artist = artist
        self.length = length


class Album:
    def __init__(self, title, artist, release_date):
        self.title = title
        self.artist = artist
        self.release_date = release_date


class Playlist:
    def __init__(self, name, songs=None):
        self.name = name
        self.songs = songs or []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)


class MusicOperations(ABC):
    @abstractmethod
    def search(self, query):
        pass

    @abstractmethod
    def play(self, song):
        pass

    @abstractmethod
    def create_playlist(self, name):
        pass

    @abstractmethod
    def add_to_playlist(self, playlist, song):
        pass

    @abstractmethod
    def remove_from_playlist(self, playlist, song):
        pass

    @abstractmethod
    def view_history(self):
        pass


class RockMusic(MusicOperations, ABC):
    @abstractmethod
    def rock_method(self):
        pass


class PopMusic(MusicOperations, ABC):
    @abstractmethod
    def pop_method(self):
        pass


class ACDCMusic(RockMusic):
    def search(self, query):
        print(f"Searching for AC/DC songs related to '{query}'...")

    def play(self, song):
        print(f"Playing AC/DC song '{song.title}' by {song.artist}...")

    def create_playlist(self, name):
        print(f"Creating a new AC/DC playlist '{name}'...")

    def add_to_playlist(self, playlist, song):
        print(f"Adding AC/DC song '{song.title}' by {song.artist} to playlist '{playlist.name}'...")

    def remove_from_playlist(self, playlist, song):
        print(f"Removing AC/DC song '{song.title}' by {song.artist} from playlist '{playlist.name}'...")

    def view_history(self):
        print("Viewing AC/DC music listening history...")

    def rock_method(self):
        print("This is a method specific to AC/DC rock music.")


class EdSheeranMusic(PopMusic):
    def search(self, query):
        print(f"Searching for Ed Sheeran songs related to '{query}'...")

    def play(self, song):
        print(f"Playing Ed Sheeran song '{song.title}' by {song.artist}...")

    def create_playlist(self, name):
        print(f"Creating a new Ed Sheeran playlist '{name}'...")

    def add_to_playlist(self, playlist, song):
        print(f"Adding Ed Sheeran song '{song.title}' by {song.artist} to playlist '{playlist.name}'...")

    def remove_from_playlist(self, playlist, song):
        print(f"Removing Ed Sheeran song '{song.title}' by {song.artist} from playlist '{playlist.name}'...")

    def view_history(self):
        print("Viewing Ed Sheeran music listening history...")

    def pop_method(self):
        print("This is a method specific to Ed Sheeran pop music.")


song1 = Song("Back in Black", "AC/DC", 4.15)
song2 = Song("Highway to Hell", "AC/DC", 3.29)
song3 = Song("Shape of You", "Ed Sheeran", 3.54)
song4 = Song("Thinking Out Loud", "Ed Sheeran", 4.41)

album1 = Album("Back in Black", "AC/DC", "1980-07-25")
album2 = Album("Divide", "Ed Sheeran", "2017-03-03")

playlist1 = Playlist("My AC/DC Playlist", [song1, song2])
playlist2 = Playlist("My Ed Sheeran Playlist", [song3, song4])

acdc_music = ACDCMusic()
ed_sheeran_music = EdSheeranMusic()

acdc_music.search("Back in Black")
ed_sheeran_music.search("Shape of You")

acdc_music.play(song1)
ed_sheeran_music.play(song3)

acdc_music.create_playlist("My New AC/DC Playlist")
acdc_music.add_to_playlist(playlist1, song2)
acdc_music.remove_from_playlist(playlist1, song1)

ed_sheeran_music.create_playlist("My New Ed Sheeran Playlist")
ed_sheeran_music.add_to_playlist(playlist2, song4)
ed_sheeran_music.remove_from_playlist(playlist2, song3)

acdc_music.view_history()
ed_sheeran_music.view_history()

acdc_music.rock_method()
ed_sheeran_music.pop_method()
