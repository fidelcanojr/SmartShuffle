import spotipy as sp
import spotipy.util as util
import time
import random
import os
from shuffleUtils import get_flagged_tracks

CLIENT_ID=os.environ['SPOTIFY_SMART_SHUFFLE_CLIENT_ID']
CLIENT_SECRET=os.environ['SPOTIFY_SMART_SHUFFLE_CLIENT_SECRET']
scope='streaming user-read-email user-modify-playback-state \
playlist-read-private playlist-modify-public playlist-modify-private \
user-read-playback-state'
token = util.prompt_for_user_token(
    os.environ['SPOTIFY_SMART_SHUFFLE_USERNAME'],
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

forbidden_fruit, current_to_next_map = get_flagged_tracks()

#Get information about the track that's currently playing
track_info = spotify_client.current_user_playing_track()
current_track_context = track_info['context']

#Collect the tracks in the playlist or album that is playing
track_ids = []
if current_track_context['type'] == 'playlist':
    playlist = spotify_client.user_playlist(my_id, playlist_id=current_track_context['uri'])['tracks']['items']
    for track in playlist:
        track_ids.append(track['track']['id'])
elif current_track_context['type'] == 'album':
    album = spotify_client.album_tracks(current_track_context['uri'])
    for track in album['items']:
        track_ids.append(track['id'])

#Add the first song to the track along with any chain it may begin
track = track_info['item']['id']
if track in forbidden_fruit:
    raise Exception("This track is part of a sequence. Please select another track from where to start shuffling.")
track_ids.remove(track)
shuffled_ids = [track]
while True:
    try:
        track = current_to_next_map[track]
        track_ids.remove(track)
        shuffled_ids.append(track)
    except KeyError:
        break

#Add the remaining songs
while len(track_ids) != 0:
    track = random.choice(track_ids)
    if track not in forbidden_fruit:
        track_ids.remove(track)
        shuffled_ids.append(track)
        while True:
            try:
                track = current_to_next_map[track]
                track_ids.remove(track)
                shuffled_ids.append(track)
            except KeyError:
                break

spotify_client.shuffle(False)
spotify_client.user_playlist_replace_tracks(my_id, smart_shuffle_id, shuffled_ids)
time.sleep(2)
spotify_client.start_playback(context_uri='spotify:user:'+my_id+':playlist:'+smart_shuffle_id)
