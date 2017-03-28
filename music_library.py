class Music():
    def _init_(self):
        self.name=""
        self.artist=""
        self.release_date=""
        self.genre = ""
        self.number_of_songs=""

first_album = Music()

first_album.name = "Pretty. Odd."
first_album.artist = "Panic! At The Disco"
first_album.release_date = "March 25, 2008"
first_album.genre = "Punk Rock"
first_album.number_of_songs = "15"

print("The first album in the library is", first_album.name)
print("It is by", first_album.artist)
print("It was released on", first_album.release_date)
print("The genre of the album is", first_album.genre)
print("The number of songs it has is", first_album.number_of_songs)

second_album = Music()

second_album.name="Take Off Your Pants and Jacket "
second_album.artist="Blink-182"
second_album.release_date="June 12, 2001"
second_album.genre="Pop Punk"
second_album.number_of_songs="13"


print("The second album is", second_album.name)
print("It is by", second_album.artist)
print("It was released on", first_album.release_date)
print("The genre of the album is", second_album.genre)
print("The number of songs it has is", second_album.number_of_songs)
