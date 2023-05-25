from abc import ABC, abstractmethod


class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


class Artist:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info


class User:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.favorites = []

    def add_favorite_song(self, song):
        self.favorites.append(song)

    def add_favorite_artist(self, artist):
        self.favorites.append(artist)


class MusicStreaming(ABC):
    @abstractmethod
    def search_song(self, title):
        pass

    @abstractmethod
    def play_song(self, song):
        pass

    @abstractmethod
    def create_playlist(self, name):
        pass

    @abstractmethod
    def share_playlist(self, name, user):
        pass


class RockSong(Song):
    def __init__(self, title, artist, duration, subgenre):
        super().__init__(title, artist, duration)
        self.subgenre = subgenre


class PopSong(Song):
    def __init__(self, title, artist, duration, danceability):
        super().__init__(title, artist, duration)
        self.danceability = danceability


class Spotify(MusicStreaming):
    def __init__(self):
        self.songs = []
        self.artists = []
        self.playlists = []

    def add_song(self, song):
        self.songs.append(song)

    def add_artist(self, artist):
        self.artists.append(artist)

    def search_song(self, title):
        for song in self.songs:
            if song.title == title:
                return song
        return None

    def play_song(self, song):
        print("Now playing: {} by {}".format(song.title, song.artist.name))

    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
        return playlist

    def share_playlist(self, name, user):
        for playlist in self.playlists:
            if playlist.name == name:
                user.playlists.append(playlist)
                return True
        return False


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def play(self):
        for song in self.songs:
            print("Now playing: {} by {}".format(song.title, song.artist.name))

# Create some songs, artists, and users
song1 = RockSong("Sweet Child O' Mine", Artist("Guns N' Roses", "contact@gunsnroses.com"), 356, "hard rock")
song2 = PopSong("Uptown Funk", Artist("Mark Ronson ft. Bruno Mars", "contact@markronson.com"), 270, 9.8)
artist1 = Artist("Led Zeppelin", "contact@ledzeppelin.com")
user1 = User("John Doe", "john.doe@example.com")
user2 = User("Jane Doe", "jane.doe@example.com")

# Add the songs and artists to Spotify
spotify = Spotify()
spotify.add_song(song1)
spotify.add_song(song2)
spotify.add_artist(artist1)

# Add some songs and artists to the
