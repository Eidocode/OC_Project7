// Add Two digits to hours and minutes
// Check UserInput

const chatbox = $("#chatbox")[0];
var idNumber = 0;

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
			'<button onClick="seeMore()" id="seeMoreButton' + idNumber + '"></button>' +
        '</div>';
    console.log("id Number : " + idNumber);
    idNumber++;
	return message;
}

function addMessageToChat(message, type='user'){
	console.log(type + ' : ' + message.length + ' character(s)');

	if (message.length > 150){
		messageMin = message.substring(0,150)
		messageMax = message.substring(150,message.length)
		message = messageMin + '<span id="dots' + idNumber + '">...</span><span id="more' + idNumber + '">' + messageMax
	}

	newMessage = createMessage(message, type);
	chatbox.innerHTML += newMessage;
}

function seeMore(){


	var dots = document.getElementById("dots" + idNumber);
	var moreText = document.getElementById("more" + idNumber);
    var btnText = document.getElementById("seeMoreButton" + idNumber);
    
	if (dots.style.display === "none") {
		dots.style.display = "inline";
		btnText.innerHTML = "Read more";
		moreText.style.display = "none";
	} else {
		dots.style.display = "none";
		btnText.innerHTML = "Read less";
		moreText.style.display = "inline"
	}
}

$("[id^=seeMoreButton]").click(function(){
    var id = $(this).attr("id");
    alert(id);
})

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