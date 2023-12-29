


from google.oauth2.credentials
import Credentials
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build

def main () :
    flow = google_auth_oauthlib.flow.Flow.installAppFlow.from_client_secrets_file(
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
    
    credentials = flow.run_local_server(port=8080, open_browser=True)
    credentials = flow.run_local_server(port=8080, open_browser=True)
    with open('credentials.json', 'w') as credentials_file:
        credentials_file.write(credentials.to_json())

   
    
    Youtube = build ("youtube","v3" ,credentials=credentials)

    request = Youtube.subcriptions().insert( part = "snippet", 
    body = {
        "snippet": {
                "resourceId": {
                    "kind": "youtube#channel",
                    "channelId": "UCOx6Q46KMebEwmtLAPTcHjA"
                }
            }
    } )
    response = request.execute()
    print (response)
 

