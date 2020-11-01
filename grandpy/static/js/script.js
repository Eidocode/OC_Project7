// Add Two digits to hours and minutes
// Check UserInput

var date = new Date();
var hours = date.getHours() + ":" + date.getMinutes();
const chatbox = $("#chatbox")[0];


function createBubble(text="dummy text", type='user'){
	var date = new Date();
	var hours = date.getHours() + ":" + date.getMinutes();

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

	return bubble = 
		'<div class="media-body ' + textPosition + '">' +
		    '<small>' + hours + '</small><h5>' + who + '</h5>' +
		    '<div class="col-6 ' + offset + ' mt-1 rounded-pill border shadow ' + bg + ' ' + text_color + ' pt-3 pl-4">' +
		        '<p>' + text + '</p>' +
		    '</div>' +
		'</div>';
}


$("#send_btn").click(function(){
	var userText = $("#input").val();  // Return user input value
	newBubble = createBubble(userText);
	chatbox.innerHTML += newBubble;
})