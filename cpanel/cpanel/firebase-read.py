from firebase import firebase

FIREBASE_URL = "https://chocomarket-hackaton-b9628.firebaseio.com//"

# Main
if __name__ == '__main__':
    fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application

    result = fb.get('/chats', "Node1") # Get  data from firebase

    print("FB Data = %s" % result)
