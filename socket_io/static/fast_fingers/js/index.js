$(document).ready(function() {
  const socket = io();
  const userName = window.prompt("My name is");
  // const userName = "Jay"

  if(userName == null || userName == undefined || userName == "") {
    window.location.reload();
  }
  localStorage["fastFingerUser"] = userName;
  localStorage["fastFingerUserScore"] = 0
  socket.on("connect", () => {
    socket.emit("new_user", userName);
  });

  $("#user_input").focus();

  $("#user_input").on("input", function(e) {
    const currentUserInput = $("#user_input").val();
    const data = {"user": userName, "input": currentUserInput};
    socket.emit("user_input", data, function(response) {
      console.log("Score: " + response)
    });
  });

  socket.on("disconnect", () => {
    console.log(socket.id); // "G5p5..."
    socket.emit("exit_user", userName);
  });

  $(".assinged_input").on("onmousedown", function(){
    return false;
  });
  $(".assinged_input").on("onselectstart", function(){
    return false;
  });
});

$(document).bind("beforeunload", function () {
  socket.emit("exit_user", userName);
});