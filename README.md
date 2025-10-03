# Spotify Automatic Music Statistics Aggregator (SAMSA)

A Python library to aggregate data about your Spotify listening habits (it also has the benefit that you can run it locally and will not give your data to a third party), so that you can have a Spotify Wrapped at any time of the year.

Extremely rudimentary at the moment.

## How to Use
I tried to make the code elegant enough to be self-documenting, but here's what you should know:

1. It's assumed that Python 3 is installed, and you also have access to ``pandas``.
2. Go to the [Spotify account privacy settings](https://www.spotify.com/us/account/privacy/) for your Spotify account, and request your Extended Streaming History.
3. Spotify will provide you with it in the form of a few JSON files, maybe after a few days. 
4. Put all of the files starting with ``Streaming_History_Audio`` in a folder called ``json_data`` (or anything to match ``DATA_DIRECTORY_NAME``) within the repository (so in the same directory where this README lives).
5. Use any of the cool functions we've got thus far.