class Songs:

    def __init__(self,title,description,length,artist=None):
        self.title = title
        self.description = description
        self.length = length
        self.artist = artist
        self.album = None
        self.featuring = []

    def is_single(self):
        return self.album is None

    def set_artist(self,artist):
        self.artist = artist

    def set_album(self,album):
        self.album = album

    def add_featuring(self,artist):
        if artist not in self.featuring:
            self.featuring.append(artist)

    def __str__(self):
        if len(self.featuring) > 0:
            feat = ""
            for artist in self.featuring:
                feat += ", {}".format(artist.name)
            return "{} by {} ft {}".format(self.title,self.artist.name,feat)


class Artists:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.singles = []
        self.albums = []

    def add_single(self,song):
        if song.is_single():
            self.singles.append(song)
        else:
            return "{} Not a single".format(song.title)

    def add_album(self,album):
        self.albums.append(album)

    def __str__(self):
        return self.name

class Albums:

    def __init__(self,title,artist,production,songs=[]):
        self.title = title
        self.artist = artist
        self.production = production
        self.songs = songs

    def add_songs(self,song):
        if not song.is_single():
            self.songs.append(song)
        else:
            return "This song is a single"

    def show_album(self):
        for index, song in enumerate(self.songs):
            print("{}- {}".format(index+1,song.title))

    def __str__(self):
        return self.title


class Playlist:

    def __init__(self,title,songs=[]):
        self.title = title
        self.songs = []

    def add_song(self,song):
        self.songs.append(song)

    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)

    def show_playlist(self):
        for song in self.songs:
            print(song)

    def __str__(self):
        return self.title

# songs
song1 = Songs("Tchokoloto", "chanson fun", 200)
song2 = Songs("Majesty", "love song", 230)
song3 = Songs("Mapi", "Togolese pop music", 190)
song4 = Songs("Realife", "Nigerian pop music", 200)
# artists
tonyx = Artists("Tony X",32)
burnaboy = Artists("Burna Boy",34)
peruzzi = Artists("Peruzzi",29)
# Album
tony_album = Albums("Niveau",tonyx,"Metamorphoo")
# Playlist
ma_playlsit = Playlist("Fun playlist")


song1.set_album(tony_album)
song3.set_album(tony_album)
tony_album.add_songs(song1)
tony_album.add_songs(song3)

tony_album.show_album()

