'''
Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.

Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.'''

def make_album(artist_name, album_title, song_number = None):
    dict = {
        'artist' : artist_name,
        'album' : album_title,
        'song tracks' : song_number,
    }
    return dict

art1 = make_album("dre", "in the hood", 2)
art2 = make_album('yjo', 'sporatic')
art3 = make_album("kbee", "sky's the limit", 9
)

def print_album(album):

    if album['song tracks']:
        print(f"\nArtist: {album['artist'].title()}")
        print(f"Album: {album['album'].title()}")
        print(f"Tracknumbers: {album['song tracks']}")
    else:
        print(f"\nArtist: {album['artist'].title()}")
        print(f"Album: {album['album'].title()}")

print_album(art1)
print_album(art2)
print_album(art3)