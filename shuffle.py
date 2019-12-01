import spotipy as sp
import spotipy.util as util
import random
import os

CLIENT_ID=os.environ['SPOTIFY_SMART_SHUFFLE_CLIENT_ID']
CLIENT_SECRET=os.environ['SPOTIFY_SMART_SHUFFLE_CLIENT_SECRET']
scope='streaming user-read-email user-modify-playback-state playlist-read-private'
token = util.prompt_for_user_token(
    'fidelcanojr',
    scope,
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    redirect_uri = 'https://www.spotify.com/us/'
)

spotify_client = sp.Spotify(auth = token)
my_id = spotify_client.me()['id']

smart_shuffle_id = None
playlists = spotify_client.user_playlists(my_id)['items']
for playlist in playlists:
    if (playlist['name']=='Smart Shuffle'):
        smart_shuffle_id = playlist['id']

forbidden_fruit = {'4nwKdZID1ht0lDBJ5h2p87','4JOyMhad5dD81uGYLGgKrS'
    '1FTCA6wQwulQFokDddKE68', '2jtUGFsqanQ82zqDlhiKIp', '01SfTM5nfCou5gQL70r6gs',
    '5eZrW59C3UgBhkqNlowEID', '5aHHf6jrqDRb1fcBmue2kn', '6UCFZ9ZOFRxK8oak7MdPZu'
}
current_to_next_map = {
    '1jOLTO379yIu9aMnCkpMQl': '4nwKdZID1ht0lDBJ5h2p87',
    '4nwKdZID1ht0lDBJ5h2p87': '4JOyMhad5dD81uGYLGgKrS',
    '4JOyMhad5dD81uGYLGgKrS': '1FTCA6wQwulQFokDddKE68',
    '1FTCA6wQwulQFokDddKE68': '2jtUGFsqanQ82zqDlhiKIp',
    '2jtUGFsqanQ82zqDlhiKIp': '01SfTM5nfCou5gQL70r6gs',
    '01SfTM5nfCou5gQL70r6gs': '5eZrW59C3UgBhkqNlowEID',
    '5eZrW59C3UgBhkqNlowEID': '5aHHf6jrqDRb1fcBmue2kn',
    '5aHHf6jrqDRb1fcBmue2kn': '6UCFZ9ZOFRxK8oak7MdPZu'
}

current_track_context = spotify_client.current_user_playing_track()['context']
track_ids = []
shuffled_ids = []
if current_track_context['type'] == 'playlist':
    playlist = spotify_client.user_playlist(my_id, playlist_id=current_track_context['uri'])['tracks']['items']
    for track in playlist:
        track_ids.append(track['track']['id'])
elif current_track_context['type'] == 'album':
    album = spotify_client.album_tracks(current_track_context['uri'])
    for track in album['items']:
        track_ids.append(track['id'])
print(track_ids)
while len(track_ids) != 0:
    track = random.choice()#lm -> lm(poop~chicken+gravy, data = thanksgiving, method = "anova"))


spotify_client.shuffle(False)
# spotify_cleint.user_playlist_replace_tracks(my_id, smart_shuffle_id)
# spotify_client.start_playback(context_uri='spotify:album:7gsWAHLeT0w7es6FofOXk1')
