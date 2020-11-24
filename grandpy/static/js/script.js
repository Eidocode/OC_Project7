// Add Two digits to hours and minutes
// Check UserInput

const chatbox = $("#chatbox")[0];

function getHour(){
	var date = new Date();
	var hours = date.getHours();
	var minutes = date.getMinutes();
	if(hours < 10){ hours = "0" + hours; }
	if(minutes < 10){ minutes = "0" + minutes; }

	var time = hours + ":" + minutes;
	return time;
}

function createMessage(text="dummy text", type='user'){
	var time = getHour();
	var textPosition = "text-right";
	var who = "Vous";
	var offset = "offset-6";
	var text_color = "text-white";
	var bg = "bg-info";

    if (type == 'bot') {
		textPosition = "text-left";
		who = "Papy Bot";
		offset = "offset";
		text_color = "text-dark";
		bg = "bg-white";
	}

	var message = 
		'<div class="media-body ' + textPosition + '">' +
		    '<small>' + time + '</small><h6><b>' + who + '</b></h6>' +
		    '<div class="bubble col-6 ' + offset + ' mt-1 border shadow ' + bg + ' ' + text_color + ' pt-3 pl-4">' +
		        '<p>' + text + '</p>' +
		    '</div>' +
		'</div>';

	return message;
}

function addMessageToChat(message, type='user'){
	console.log(type + ' : ' + message.length + ' character(s)');
	newMessage = createMessage(message, type);
	chatbox.innerHTML += newMessage;
}


$("#send_btn").click(function(){
	var userText = $("#input").val();  // Return user input value
	addMessageToChat(userText);
	$.ajax({
		type : 'POST',
		url : '/process',
		data : { message : userText },
		dataType : 'json',
		success: function(response){
			var botText = response.result;
			addMessageToChat(botText, 'bot');
		},
		failure: function(response){
			alert("failure");
		}
	})
})