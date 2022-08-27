/********************************
 * Custom Jeopardy
 * CustomJeopardy.js
 * Created by Justin Leonard
********************************/

/**
* Clear the selected button
*/
function buttonClear(id) {
	// Disable button
	document.getElementById(id).style.background = "url(images/block_blank.png)";
	document.getElementById(id).disabled = true;
}

/**
* Display question and answer
*/
function buttonMessage(question, answer) {
	// Question
	alert(question);

	// Answer
	alert(answer);
}