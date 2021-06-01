


function createUser() {
  
    let data = {
        first_name: $('#first-name').val(),
        last_name: $('#last-name').val(),
        hobbies: $('#hobbies').val()
    };

    $.ajax({
        url: "http://127.0.0.1:5000/users",
        type: "POST",
        data: JSON.stringify(data),
        contentType: 'application/json',
        success: function (res) {
            console.log("Server says: ", res);
            
            //humidity = "Current humidity: " + res.current.humidity + "%"
            //$("#weather-info").append(currentWeather)
        },
        error: function (details) {
            console.log("Error sending data", details);
        }
    });
}

function init() {
    createUser();

    $('#btn-create').click(createUser)
}



window.onload = init;