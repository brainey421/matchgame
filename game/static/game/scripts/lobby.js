var partyID;
var lobbySocket;

window.onload = onWindowLoaded;

function onWindowLoaded()
{
	partyID = JSON.parse(document.getElementById('partyID').textContent);
	
	lobbySocket = new WebSocket(
		'ws://'
		+ window.location.host
		+ '/ws/lobby/'
		+ partyID
		+ '/'
	);
	
	lobbySocket.onopen = onLobbySocketOpened;
	lobbySocket.onmessage = onLobbySocketMessage;
}

function onLobbySocketOpened()
{
	lobbySocket.send('');
}

function onLobbySocketMessage()
{
	spanJoinedMessage = document.getElementById('spanJoinedMessage');
	spanJoinedMessage.textContent = spanJoinedMessage.textContent + 'Someone joined! ';
}
