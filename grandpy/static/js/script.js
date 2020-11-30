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

function createMessage(text="dummy text", type='user', btn){
	var time = getHour();
	var textPosition = "text-right";
	var who = "Vous";
	var offset = "offset-6";
	var text_color = "text-white";
	var bg = "bg-info";
	var gmap_widget = '<div></div>';

    if (type === 'bot') {
		textPosition = "text-left";
		who = "Papy Bot";
		offset = "offset";
		text_color = "text-dark";
		bg = "bg-white";
		gmap_widget = '<div id="map_' + idNumber + '"  class="gmap border border-primary"></div>'
    }
    
    var idName = "seeMoreButton_" + idNumber;
    btnState = "d-none";
    if (btn === 'enabled'){
        btnState = "d-inline";
    }

	var message = 
		'<div class="media-body ' + textPosition + '">' +
		    '<small>' + time + '</small><h6><b>' + who + '</b></h6>' +
		    '<div class="bubble col-6 ' + offset + ' mt-1 border shadow ' + bg + ' ' + text_color + ' pt-3 pl-4">' +
				'<p>' + text + gmap_widget +'</p>' +
				'<button class="' + btnState + ' btn-primary btn-circle mb-2" onClick="seeMore(' + idName + ')" id="seeMoreButton_' + idNumber + '"><i class="fa fa-plus"></i></button>' +
            '</div>' +
        '</div>';
	return message;
}

function seeMore(thisId){
    var idNum = $(thisId).attr("id").split("_")[1];
    console.log("ID : " + idNum);

    var dots = $("#dots_" + idNum);
    var moreText = $("#more_" + idNum);
    var btnText = $("#seeMoreButton_" + idNum);

    if (dots.attr('class') === 'd-none') {
        dots.removeClass('d-none').addClass('d-inline');
        moreText.removeClass('d-inline').addClass('d-none');
        btnText.find('i').removeClass("fa fa-minus").addClass("fa fa-plus")
    } else {
        dots.removeClass('d-inline').addClass('d-none');
        moreText.removeClass('d-none').addClass('d-inline');
        btnText.find('i').removeClass("fa fa-plus").addClass("fa fa-minus")
    }
}

function initMap(id, coord){
    // var test = {lat: 48.85837009999999, lng: 2.2944813};
    var map = new google.maps.Map(document.getElementById("map_" + id), {
        center : coord,
        zoom : 16
	});
	return map
}

function addMessageToChat(message, type='user'){
    console.log(type + ' : ' + message.length + ' character(s)');
    btnState = 'disabled';

	if (message.length > 150){
		messageMin = message.substring(0,150)
		messageMax = message.substring(150,message.length)
        message = messageMin + '<span class="d-inline" id="dots_' + idNumber + '">...</span><span class="d-none" id="more_' + idNumber + '">' + messageMax
        btnState = 'enabled'
	}

    newMessage = createMessage(message, type, btnState); 
	chatbox.innerHTML += newMessage;
}

function updateScroll(){
	chatbox.scrollTop = chatbox.scrollHeight;
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
			var respons = response.result;
            addMessageToChat(respons['wikiped'], 'bot');
			initMap(idNumber, respons['gmap_coord']);
			updateScroll();
			$("#input").val("");
		},
		failure: function(response){
			alert("failure");
		}
    })
    idNumber++;
})