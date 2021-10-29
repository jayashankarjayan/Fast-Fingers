$(document).ready(function() {

  var base_url = window.location.origin;

  var current_path = window.location.pathname;
  if (current_path == "/fast_fingers/") {
    setInterval(function() {
      $.ajax({
        url: base_url + "/fast_fingers/get_page/",
        method: "post",
        data: {
          "text": $("#user_input").val().trim(),
          "assinged_input": $(".assinged_input").text().trim()
        },
        success: function(result) {
          console.log(result);
        }
      });
    }, 5000);

    setInterval(function() {
      var assinged_input = $(".assinged_input").text()
      var trimmedString = assinged_input.substr(0, 30);
      trimmedString = trimmedString.substr(0, Math.min(trimmedString.length,
        trimmedString.lastIndexOf(" ")))

      assinged_input = assinged_input.replace(trimmedString, "")
      $(".assinged_input").text(assinged_input)
    }, 15000)
  } else if (current_path == "/fast_fingers/display_score/") {
    setInterval(function() {
      $.ajax({
        url: base_url + "/fast_fingers/calculate_all_scores/",
        method: "post"
      });
    }, 5000);

  }

});
