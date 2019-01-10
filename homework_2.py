from main import genre, song_writers, recorded


def Artist():
    return song_writers


def Genre():
    return genre


def Year():
    return str(recorded)


year = Year()
genre = Genre()
artist = Artist()
print("Artist: " + artist)
print("Genre: " + genre)
print("Year: " + year)
