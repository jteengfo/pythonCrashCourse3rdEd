'''
: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
'''
is_active = True
def make_album(artist_name, album_title, song_number = None):
    dict = {
        'artist' : artist_name,
        'album' : album_title,
        'song tracks' : song_number,
    }
    return dict

# art1 = make_album("dre", "in the hood", 2)
# art2 = make_album('yjo', 'sporatic')
# art3 = make_album("kbee", "sky's the limit", 9)

def print_album(album):

    if album['song tracks']:
        print(f"\nArtist: {album['artist'].title()}")
        print(f"Album: {album['album'].title()}")
        print(f"Tracknumbers: {album['song tracks']}")
    else:
        print(f"\nArtist: {album['artist'].title()}")
        print(f"Album: {album['album'].title()}")

# print_album(art1)
# print_album(art2)
# print_album(art3)

while is_active: 
    artist = input("Please enter an artist's name: ")

    if artist == 'q' or album == 'q':
        is_active = False
        break

    album = input("Please enter an album name: ")
    if artist == 'q' or album == 'q':
        is_active = False
        break

    album_details = make_album(artist_name= artist, album_title= album)
    print_album(album_details)

    if artist == 'q' or album == 'q':
        is_active = False