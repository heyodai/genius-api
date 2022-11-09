from lyricsgenius import Genius
from dotenv import dotenv_values

token = dotenv_values(".env")["GENIUS_TOKEN"]
genius = Genius(token)
artist = genius.search_artist('Amon Tobin', max_songs=3, sort='title', get_full_info=False)
artist.save_lyrics('tobin.json')