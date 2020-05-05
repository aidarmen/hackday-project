
angular.module("chat").
    controller("ChatController", ['$scope', '$firebase', function ($scope, $firebase) {
        console.log("In controller");
        console.log("var " + $scope.IdDelivery);
        var firebaseUrl = 'https://chocomarket-hackaton-b9628.firebaseio.com/chats/' + $scope.IdDelivery;
        console.log(firebaseUrl);
        var chatRef = new Firebase(firebaseUrl);
        var sync = $firebase(chatRef);

        // $scope.username = "New Use22r";
        // $scope.sender_id = "222";
        $scope.chat_messages = sync.$asArray();
      

        $scope.newMessageKeyPress = function(keyEvent) {
            if (keyEvent.which === 13) {
              
                console.log("Enter clicked : " + $scope.new_message);
                $scope.chat_messages.$add({name: $scope.username, text: $scope.new_message,sender_id: $scope.sender_id});
                $scope.new_message = "";
            }
        }
    }]);
