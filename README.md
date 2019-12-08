# Smart Shuffle

This application shuffles any Spotify album or playlist while retaining the order of songs that are flagged as sequential.

### First Things First, Authorization!

[Register the app with a redirect URL](https://developer.spotify.com/documentation/general/guides/app-settings/) or get a client id and secret from the [Spotify developer console](https://developer.spotify.com/dashboard). The redirect URL should be `https://www.spotify.com/us/`.
Go into this repository and stick the credentials as environment variables by running the following commands:

```
export SPOTIFY_SMART_SHUFFLE_CLIENT_ID=<CLIENT_ID>
export SPOTIFY_SMART_SHUFFLE_CLIENT_SECRET=<CLIENT_SECRET>
```

You will also have to stick your Spotify username into your environment variables by running the following command:

```
export SPOTIFY_SMART_SHUFFLE_USERNAME=<USERNAME>
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

The following songs are already flagged as sequential when you clone this repository:

* `You Never Give Me Your Money` is followed by `Sun King`, both by `The Beatles`
* `Sun King` is followed by `Mean Mr. Mustard`, both by `The Beatles`
* `Mean Mr. Mustard` is followed by `Polythene Pam`, both by `The Beatles`
* `Polythene Pam` is followed by `She Came In Through The Bathroom Window`, both by `The Beatles`
* `She Came In Through The Bathroom Window` is followed by `Golden Slumbers`, both by `The Beatles`
* `Golden Slumbers` is followed by `Carry That Weight`, both by `The Beatles`
* `Carry That Weight` is followed by `The End`, both by `The Beatles`
* `Sgt. Pepper's Lonely Hearts Club Band` is followed by `With a Little Help From My Friends`, both by `The Beatles`
* `A Savior in the Square` is followed by `When Your Time has Come`, both by `Dream Theater`
* `Helpless` is followed by `Satisfied`, both from the `Hamilton Original Broadway Cast Soundtrack`
