from firebase import firebase
from sseclient import SSEClient
import json

FIREBASE_URL = "https://chocomarket-hackaton-b9628.firebaseio.com/"

# Main
if __name__ == '__main__':
    fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application

    sse = SSEClient("https://chocomarket-hackaton-b9628.firebaseio.com/chats.json")

    for new_message in sse:
        message_data = json.loads(new_message.data)

        print("message_data = %s\n" %(message_data))
