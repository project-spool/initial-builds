import sys
import spotipy
import spotipy.util as util

#this portion of code should create a token to login with
scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]

else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope, client_id = '782c30dd0a69426db82d7a172d38802c', client_secret = 'a8d41bb555584b258e35f04f0903b8d0', redirect_uri = 'http://localhost:8888/callback')
# make sure you have another terminal window with the app.js file running ('node app.js')
# print(token)

if token:
    sp = spotipy.Spotify(auth = token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("FAILED BECAUSE RAHUL DOESN'T KNOW HOW TO CODE FOR FUCK'S SAKE")
