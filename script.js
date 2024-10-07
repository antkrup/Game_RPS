function sendMove(move) {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:12345', true);
    xhr.setRequestHeader('Content-Type', 'text/plain');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(xhr.responseText, "application/xml");
            const result = xmlDoc.getElementsByTagName("result")[0].textContent;
            document.getElementById('result').innerText = result;
            document.getElementById('player_move').innerText = xmlDoc.getElementsByTagName("player_move")[0].textContent;
            document.getElementById('server_move').innerText = xmlDoc.getElementsByTagName("server_move")[0].textContent;
        }
    }
    xhr.send(move);
}