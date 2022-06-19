$(document).ready(function(){
    const socket = io();
    
    function addRowToScoreboard(userDetails, isNewUser=false) {
        var userName = userDetails.name;
        var userScore = userDetails.score;
        var socketId = userDetails.sock_id
        var numUsers = $(".scoredboard-users tbody > tr:last").length;
        var nextRank = $(".scoredboard-users tbody > tr").length + 1;
        var newListItem = ""
        if(isNewUser) {
            newListItem = "<tr class=\"table-primary\"><td>" + nextRank + "</td><td>" + userName + "</td><td id=\"score-" + socketId + "\">" + userScore + "</td></tr>"
        }
        else {
            newListItem = "<tr><td>" + nextRank + "</td><td>" + userName + "</td><td id=\"score-" + socketId + "\">" + userScore + "</td></tr>"
        }
        if (numUsers == 0) {
            $(".scoredboard-users tbody").append(newListItem)
        }
        else {
            $(".scoredboard-users tr:last").after(newListItem);
        }
    }

    socket.on("connect", function(){
        socket.emit("list_all_users", function(userDetails) {
            $(".scoredboard-users tbody").empty();
            userDetails.forEach(element => {
                addRowToScoreboard(element);
            });
        });

        socket.on("update_user_score", function (details) {
            const score = details.score;
            const socketId = details.sock_id
            $("#score-" + socketId).text(score);
        });    

        socket.on("new_user_on_scoreboard", function (userDetails) {
            addRowToScoreboard(userDetails, isNewUser=true);
        });    
    });
});