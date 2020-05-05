from multiprocessing import Process
from firebase import firebase
from sseclient import SSEClient
import json
import time

FIREBASE_URL = "https://chocomarket-hackaton-b9628.firebaseio.com/"


def poll_chat():
    sse = SSEClient(FIREBASE_URL + "chats/5bjfDpOpLEWASgDRPdlj.json")
    print("Watching Firebase node - %s" % (FIREBASE_URL + "chats/5bjfDpOpLEWASgDRPdlj.json"))

    for new_message in sse:
        message_data = json.loads(new_message.data)

        if message_data is None:  # Keep alive
            continue

        if message_data["data"] is None:
            continue

        # print("message_data = %s\n" %(message_data))

        if message_data["path"] == "/":  # Initial Read for old messages
            print("Previous messages")
            for (nodeid, message) in message_data["data"].items():
                try:
                    # print("message = %s" % (message))
                    print("%s says: %s" % (message["name"], message["text"]))
                except:
                    pass

        else:  # New Message
            try:
                print("%s says: %s" % (message_data["data"]["name"], message_data["data"]["text"]))
            except:
                pass


# Main
if __name__ == '__main__':

    # Start a thread to monitor changes to firebase
    t = Process(target=poll_chat)
    t.start()

    time.sleep(1)
    username = raw_input("Input your name: ")
    # username = 'me'
    fb = firebase.FirebaseApplication(FIREBASE_URL, None)

    # Post initial message to Firebase
    fb.post('/chats/5bjfDpOpLEWASgDRPdlj',
            {"name": username,
             "text": "Joined the chat",
             "sender_id": username,
             ".priority": time.time() * 1000
            })

    # Post new messages to Firebase
    while (True):
        message = raw_input("")
        # message= 'hi'
        print("\n")
        fb.post('/chats/5bjfDpOpLEWASgDRPdlj',
                {
                    "name": username,
                    "text": message,
                    "sender_id": username,
                    ".priority": time.time() * 1000
                })










