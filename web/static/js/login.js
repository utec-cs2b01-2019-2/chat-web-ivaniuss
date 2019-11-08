function login(){
    console.log("Login User");
    var username = $('#username').val();  //getting username by ID
    var password = $('#password').val();  // getting password by id
    console.log("DATA>", username, password);
    var credentials = {'username':username, 'password':password};
    $.post({
        url:'/authenticate',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        success: function(data){
            console.log("Authenticated!");
            alert("Authenticated!!!");

        },
        data: JSON.stringify(credentials)
    });
}