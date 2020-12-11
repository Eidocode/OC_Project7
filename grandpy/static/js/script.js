// Add Two digits to hours and minutes
// Check UserInput

const chatbox = $("#chatbox")[0];
var idNumber = 0;
var loading = false;

function getHour(){
	var date = new Date();
	var hours = date.getHours();
	var minutes = date.getMinutes();
	if(hours < 10){ hours = "0" + hours; }
	if(minutes < 10){ minutes = "0" + minutes; }

	var time = hours + ":" + minutes;
	return time;
}

function createMessage(text, type='user', btn, map=false){
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
    }

    if (map === true) {
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

function addMessageToChat(message, type='user', map=false, url){
    console.log(type + ' : ' + message.length + ' character(s)');
	var btnState = 'disabled';
	var link = null;

	if (message.length > 150){
		messageMin = message.substring(0,150);
		messageMax = message.substring(150,message.length);
		message = messageMin + '<span class="d-inline" id="dots_' + idNumber + '">...</span><span class="d-none" id="more_' + idNumber + '">' + messageMax;
        btnState = 'enabled'
	}

	if (url != null){
		link = ' ' + '<a href="' + url + '">[Page Wikipedia]</a>';
		message += link;
	}

    newMessage = createMessage(message, type, btnState, map); 
    chatbox.innerHTML += newMessage;
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

function initMap(id, coord, title){
    // var test = {lat: 48.85837009999999, lng: 2.2944813};
    var map = new google.maps.Map(document.getElementById("map_" + id), {
        center: coord,
        zoom: 17,
        mapTypeControl: false,
        scrollwheel: false,
        navigationControl: false,
        draggable: false,
        zoomControl: true,
    });
    new google.maps.Marker({
        position: coord,
        map,
        title: title,
    });
    console.log("ID : " + id)
    console.log("COORD : " + coord)

	return map
}

function updateScroll(){
	chatbox.scrollTop = chatbox.scrollHeight;
}


$(document).ready(function(){
	$("#input").keyup(function(){
		if($(this).val().length > 1){
			$("#send_btn").attr('disabled', false);
		} else {
			$("#send_btn").attr('disabled', true);
		}
    })
    $("#send_btn").click(function(){
        if (loading){
            this.innerHTML = '<div class="spinner-border"></div>';
        } else {
            this.innerHTML = 'Envoyer';
        }
    })
})

addMessageToChat("Bonjour et bienvenue !!!", 'bot');

$("#send_btn").click(function(){
    loading = true
    var userText = $("#input").val();  // Return user input value
    addMessageToChat(userText);
	$.ajax({
		type : 'POST',
		url : '/process',
		data : { message : userText },
		dataType : 'json',
		success: function(response){
			var respons = response.result;
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
            updateScroll();
		},
		failure: function(response){
			alert("failure");
		}
    })
	$("#input").val("");
    $("#send_btn").attr('disabled', true);
    idNumber++;
    loading = false;
})