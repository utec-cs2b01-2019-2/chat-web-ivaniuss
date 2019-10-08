function get_all_users(){
    console.log("voy a traer todos los usuarios");

    $.getJSON("/users", function(data){
    var i = 0;
    $.each(data,function(){
        user_to = data[i]['id'];
        e = '<div class = "alert" role="alert">';
        e = e+ '<button type="button" class="btn btn-secondary btn-sm" id ="'+i+'" onclick="show_messages('+i+')">';
        e = e+data[i]['username']+'</button>';
        e = e+'</div>';i = i+1;
        $("<div/>", {html:e}).appendTo("#users");
    });
    });

}

function show_messages(i){                       
    console.log(i);
    $("#message").empty();
    $.getJSON("/messages", function(data){
        message_to=data[i]['id'];
        e = '<div class = "alert" role="alert">';
        e = e+ '<p>'+data[i]['content']+'</button>';
        e = e+'</div>';
        $("<div/>", {html:e}).appendTo("#message");
    });
}

function send_message(){    
    var x=document.getElementById("txtMessage").value;
    $("<div/>", {html:x}).appendTo("#message");  
   
}