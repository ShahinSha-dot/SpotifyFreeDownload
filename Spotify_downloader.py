import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from selenium import webdriver
import time


client_id = str(input('enter your client id'))
client_secret_id = str(input('enter your client secret id'))
SPOTIPY_REDIRECT_URI='https://www.google.com/'
browser=webdriver.Chrome()


spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret_id))
a= []


def getTrackIDs(user, playlist_id):
    ids = []
    playlist = spotify.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['name'])
    return ids

playlist =  str(input('enter playlist id : '))
items = getTrackIDs('Tut',playlist)


for songs in items:
        link = "https://www.youtube.com/results?search_query=" + songs
        browser.get(link)
        browser.execute_script(
            "document.cookie=\"VISITOR_INFO1_LIVE=oKckVSqvaGw; path=/; domain=.youtube.com\";window.location.reload();")  # Disable ads
        browser.find_element_by_id("img").click()
        be = browser.current_url
        browser.get('https://ytmp3.cc/en13/')
        browser.find_element_by_id('input').send_keys(be)
        browser.find_element_by_id('submit').click()
        time.sleep(1)
        ab = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]')
        song = ab.get_attribute('href')
        browser.get(song)
        browser.get('chrome://downloads/')
        browser.maximize_window()