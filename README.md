# Smart Shuffle

This application shuffles any Spotify album or playlist while retaining the order of songs that are flagged as sequential.

### First Things First, Authorization!

Get the client id and secret from the [Spotify developer console](https://developer.spotify.com/dashboard).
Go into this repository and stick the credentials as environment variables by running the following commands:

```
export SPOTIFY_SMART_SHUFFLE_CLIENT_ID=<CLIENT_ID>
export SPOTIFY_SMART_SHUFFLE_CLIENT_SECRET=<CLIENT_SECRET>
```

### Shuffling a Playlist or Album

In Spotfiy, navigate to the album or playlist you wish to shuffle and begin playing the first song you want to play. As the song is playing, run the following command.

`python3 shuffle.py`

***Note:*** The script will throw an error if you attempt to shuffle during a song that is in, but doesn't begin a sequence.

### Flagging Songs as Being in a Sequence

If you want to flag a pair of songs as being in a sequence (namely song with id `SONG_ID_1` is to be followed by song with id `SONG_ID_2`), run the following command.

`python3 shuffleUtils.py <SONG_ID_1> <SONG_ID_2>`

To find a song's id, navigate to the song in Spotify. One of the `Share` options is `Copy Spotify URI`. This URI will be of the form:

`spotify:track:<SONG_ID>`
