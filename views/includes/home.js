$(function(){
	$('#join-game-button').click(function(){
		var token = $('#game-token-value').val();
		window.location.replace("/"+token);
	});
	
});