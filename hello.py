from lyricsgenius import Genius
from dotenv import dotenv_values

token = dotenv_values(".env")["GENIUS_TOKEN"]
genius = Genius(token)
artist = genius.search_artist('Andy Shauf')
artist.save_lyrics()