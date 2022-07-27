"""
    M. Ashuza 
    july 26 2022
    Python Crash Course Book chapter 8 Exercises 
"""

# Question 8-3. T-Shirt
from sre_constants import AT_LOC_BOUNDARY

from matplotlib import artist


def make_shirt(size, text):
    print(f"The shirt will be of size {size.title()} and the message printed on it will be {text.title()}.")

make_shirt('M', 'I love python')
make_shirt(size='x', text='i love jengo')
print("\n")

# Question 8-4. Large Shirts
def make_shirt(text='i love python', size='L'):
    print(f"The shirt will be of size {size.title()} and the message printed on it will be {text.title()}.")

make_shirt()
make_shirt(size='M')
make_shirt(size='x', text='i love jengo')
print("\n")
# Question 8-5. Cities
def describe_city(city_name, country='Iceland'):
    print(f"{city_name.title()} is in {country.title()}.")

describe_city('Reykjavik')
describe_city('Goma', country='drc')
describe_city(city_name='bukavu', country='drc')
print("\n")

# Question 8-6. City Names

def city_country(city_name, country):
    """Return a formated string of city and coutry name."""
    city_country_name = f"{city_name.title(), country.title()}"
    return city_country_name

city_country_name = city_country('Santiago', 'chili')
print(city_country_name)
print(city_country('Goma', country='drc'))
print(city_country(city_name='bukavu', country='drc'))
print("\n")

# Question 8-7. Album

def make_album(artist_name, album_title, tracks=''):
    """Return a dictionary of information about a music album"""
    album = {'artist': artist_name, 'album': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

album1 = make_album('Maitre Gims', 'Subliminal')
print(album1)
album2 = make_album('Maitre Gims', 'Ceinture Noire')
print(album2)
album3 = make_album('Maitre Gims', 'Mon Coeur Avait Raison')
print(album3)

album4 = make_album('Maitre Gims', 'Mon Coeur Avait Raison', tracks=28)
print(album4)
print("\n")
# Question 8-8. User Albums
album5 = {}
while True:
    print("Inter the artist name and album name")
    print("Inter q to quit the programm.\n")
    artist = input("Airtist : ")
    if artist == 'q':
        break

    album = input("Album name: ")
    if album == 'q':
        break

    album5 = make_album(artist, album)
print(album5)
