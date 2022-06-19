$(document).ready(function(){
    const socket = io();
    
    function addRowToScoreboard(userDetails) {
        var userName = userDetails.name;
        var userScore = userDetails.score;
        var numUsers = $(".scoredboard-users tbody > tr:last").length;
        var nextRank = $(".scoredboard-users tbody > tr").length + 1;
        var newListItem = "<tr><td>" + nextRank + "</td><td>" + userName + "</td><td>" + userScore + "</td></tr>"
        if (numUsers == 0) {
            $(".scoredboard-users tbody").append(newListItem)
        }
        else {
            $(".scoredboard-users tr:last").after(newListItem);
        }
    }

    socket.on("connect", function(){
        socket.emit("list_all_users", function(userDetails) {
            console.log(userDetails);
            userDetails.forEach(element => {
                addRowToScoreboard(element);
            });
        });

        socket.on("new_user_on_scoreboard", function (userDetails) {
            addRowToScoreboard(userDetails);
        });    
    });
});