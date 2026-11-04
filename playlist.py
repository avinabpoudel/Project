class Playlist:
    def __init__(self , name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
    def add_songs(self,song):
        self.songs.append(song)
        print(f"{song} is added")
    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
        else:
            print(f"Not found in playlist")
    def display(self):
        if self.songs:
            for i , song in enumerate(self.songs,1):
                print(f"{i}.{song}")
        else:
            print("Song not added")
    def __del__(self):
        print("All the songs are deleted")

my_playlist = Playlist("Road Trip "," Pop")

while True:
    print("Press 1 for Add song","Press 2 for remove song", "Press 3 for see playlist","Press 4 for delete playlist")
    choice = input("Enter your choice: ")
    if choice == "1":
        song = input("Enter the song name: ")
        my_playlist.add_songs(song)
    elif choice == "2":
        song = input("Enter the song to remove: ")
        my_playlist.remove_song(song)
    elif choice == "3":
        my_playlist.display()
    elif choice == "4":
        del my_playlist
        break
    else:
        print("Invalid Choice")


