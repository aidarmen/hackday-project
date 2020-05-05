

angular.module("chat").
    factory("ChatService", ["$firebase", function($firebase) {
        console.log("In service");
        var firebaseUrl = "https://chocomarket-hackaton-b9628.firebaseio.com/chats/Track";
        var chatRef = new Firebase(firebaseUrl);

        chatRef.on("child_added", function(snapshot) {
            var chat_message = snapshot.val();
            console.log("Chat message = " + chat_message);
        })

    }]);