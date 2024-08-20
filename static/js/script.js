document.getElementById('comandoBtn').addEventListener('click', function(){
    fetch('/comando', 
        {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('resposta').innerText = data.resposta;
        });
});