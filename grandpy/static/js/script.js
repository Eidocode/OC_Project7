
const chatbox = $("#chatbox")[0];
var idNumber = 0; // used when inserting new ID in HTML file

function getHour(){
    // Function used to get the current time
    // It will be displayed when a new message is added

	var date = new Date();
	var hours = date.getHours();
    var minutes = date.getMinutes();
    
    // Adds a '0' before the hour or minutes if they are less than 10
	if(hours < 10){ hours = "0" + hours; }
	if(minutes < 10){ minutes = "0" + minutes; }

	var time = hours + ":" + minutes;
	return time;
}

function createMessage(text, type='user', btn, map=false){
    // Function used to create a message

	var time = getHour(); // Get current time
    
    // Sets message's default properties
    var textPosition = "text-right";
	var who = "Vous";
	var offset = "offset-6";
	var text_color = "text-white";
	var bg = "bg-info";
	var gmap_widget = '<div></div>';

    // Sets message's properties if type == 'bot'
    if (type === 'bot') {
		textPosition = "text-left";
		who = "Papy Bot";
		offset = "offset";
		text_color = "text-dark";
		bg = "bg-white";
    }

    // Adds this div if the message must contain a map
    if (map === true) {
		gmap_widget = '<div id="map_' + idNumber + '"  class="gmap border border-primary"></div>'
    }
    
    // Sets see more button's properties
    var idName = "seeMoreButton_" + idNumber;
    btnState = "d-none";
    if (btn === 'enabled'){
        btnState = "d-inline";
    }

    // Contains the elements necessary to display the message
    var message = 
		'<div class="media-body ' + textPosition + '">' +
		    '<small>' + time + '</small><h6><b>' + who + '</b></h6>' +
		    '<div class="bubble col-6 ' + offset + ' mt-1 border shadow ' + bg + ' ' + text_color + ' pt-3 pl-4">' +
				'<p>' + text + gmap_widget +'</p>' +
				'<button style="outline: none;" class="' + btnState + ' btn-primary btn-circle mb-2" onClick="seeMore(' + idName + ')" id="seeMoreButton_' + idNumber + '"><i class="fa fa-plus"></i></button>' +
            '</div>' +
        '</div>';
	return message;
}

function addMessageToChat(message, type='user', map=false, url){
    // Function used to add a message to the chat

    console.log(type + ' : ' + message.length + ' character(s)');
    
    var btnState = 'disabled'; // See more button state
	var link = null; // Wikipedia's page link

    // Checks if message length is greater than 150 chars
    if (message.length > 150){
		messageMin = message.substring(0,150);
		messageMax = message.substring(150,message.length);
		message = messageMin + '<span class="d-inline" id="dots_' + idNumber + '">...</span><span class="d-none" id="more_' + idNumber + '">' + messageMax;
        btnState = 'enabled' // adds see more button
	}

    // Adds Wikipedia's page link if necessary
    if (url != null){
		link = ' ' + '<a href="' + url + '" target="_blank">[Page Wikipedia]</a>';
		message += link;
	}

    newMessage = createMessage(message, type, btnState, map); // Creates the message
    chatbox.innerHTML += newMessage; // Adds it to chatbox
}

function seeMore(thisId){
    // Function used if seeMoreButton is required
    // It allows to split the message into two parts and to display only
    // the first part or all of it

    var idNum = $(thisId).attr("id").split("_")[1]; // Get the dynamic HTML id number
    console.log("ID : " + idNum);

    // Based on idNum, gets different elements of the DOM
    var dots = $("#dots_" + idNum); 
    var moreText = $("#more_" + idNum);
    var btnText = $("#seeMoreButton_" + idNum);

    // Checks the DOM elements state and modifies them
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

function initMap(id, coord, title){
    // Function used to display the map

    var map = new google.maps.Map(document.getElementById("map_" + id), {
        // Initializes Google Maps and sets properties
        center: coord,
        zoom: 17,
        mapTypeControl: false,
        scrollwheel: false,
        navigationControl: false,
        draggable: false,
        zoomControl: true,
    });
    new google.maps.Marker({
        // Adds Google Maps Marker
        position: coord,
        map,
        title: title,
    });
	return map
}

function updateScroll(){
    // Chatbox autoscroll function
	chatbox.scrollTop = chatbox.scrollHeight;
}

function loadingAnim(state=false){
    var loadingChat = 
    '<div id="loading2" class="row">' +
        '<br></br>' +
        '<div class="col-6 offset mt1 pt-3 pl-4">' +
            '<span class="text-secondary">' +
                '<span class="spinner-border" role="status" aria-hidden="true"></i></span>' +
                '&ensp; Please wait...' +
            '</span>' +
        '</div>' +
    '</div>'

    var load = $("#loading")
    if (state === true) {
        load.removeClass('invisible').addClass('visible');
        chatbox.innerHTML += loadingChat
    } else {
        load.removeClass('visible').addClass('invisible');
        $('div[id^="loading2"]').remove();
    }
}


$(document).ready(function(){
    // Disabled or enabled input send button
	$("#input").keyup(function(){
		if($(this).val().length > 1){
            $("#send_btn").attr('disabled', false);
		} else {
			$("#send_btn").attr('disabled', true);
		}
    })
})

$(document).on({
    ajaxStart: function() { 
        loadingAnim(true)
        updateScroll(); // Autoscroll function
     },
    ajaxStop: function() { 
        loadingAnim(false) 
        updateScroll(); // Autoscroll function
    },
});


// First bot message
addMessageToChat("Bonjour et bienvenue !!!", 'bot');

$("#send_btn").click(function(){
    var userText = $("#input").val();  // Returns user's input value
    console.log("INPUT : " + userText);
    addMessageToChat(userText); // Adds user's input to a chat message
    $.ajax({
        method : "POST",
		url : '/process',
		data : { message : userText }, // POST request for user's input
		dataType : 'json',
		success: function(response){
            var respons = response.result; // Gets response from views.py
            
            // Adds datas to bot messages
			var this_url = null;
			if (respons['url'] != null){
				this_url = respons['url'];
				console.log(this_url);
			}
            addMessageToChat(respons['first_message'], 'bot', map=false, url=this_url);
            if (respons['gmap_coord'] != null){
                idNumber++;
                addMessageToChat(respons['second_message'], 'bot', map=true);
                initMap(idNumber, respons['gmap_coord'], respons['title']);
            }
		},
		failure: function(response){
			alert("failure");
		}
    })
	$("#input").val(""); // Cleans input field
    $("#send_btn").attr('disabled', true); // Disables input send button
    idNumber++;
})