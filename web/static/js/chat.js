function get_current(){
    console.log("voy a traer al usuario logueado")
    $.getJSON("/current", function (data){
        console.log("current user is " +data['username'])
        get_all_users(data['id']);
    });
}



function getMessages(user_from_id,user_to_id){
    alert("voy a traer los mensajes entre"+user_from_id+'y'+user_to_id);
}

function get_all_users(user_from_id){
    console.log("voy a traer todos los usuarios");

    $.getJSON("/users", function(data){
    var i = 0;
    $.each(data,function(){
        user_to = data[i]['id'];
        e = '<div class = "alert" role="alert" onclick="getMessages('+user_from_id+','+data[i]['id']+')">';
        e = e+ '<div>'+data[i]['username']+'</div>';
        e = e+'</div>';
        i = i+1;
        $("<div/>", {html:e}).appendTo("#users");
    });
    });

}






function show_messages(){                       
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