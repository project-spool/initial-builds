# testing/learning the functionality of the spotipy library

import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'
username = 'ndnboi1996'

token = util.prompt_for_user_token(username, scope, client_id='782c30dd0a69426db82d7a172d38802c',client_secret='a8d41bb555584b258e35f04f0903b8d0',redirect_uri='http://localhost:8888/callback')

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)