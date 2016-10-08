$(function(){
	$('#join-game-button').click(function(){
		var token = $('#game-token-value').val();
		window.location.replace("/"+token);
	});
	
	$('#create-new-game').click(function(){
		$.post("/create", function(data){
			alert(0);
		});
	});
});