document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('calculadora-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Impede o envio do formulário
        
        var numeros = [];
        var inputs = document.querySelectorAll('input[name^="numero"]');
        
        inputs.forEach(function(input) {
            var valor = parseFloat(input.value);
            numeros.push(isNaN(valor) ? 0.0 : valor);
        });
        
        // Agora, você pode enviar 'numeros' para a sua view Django usando AJAX
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/calibracao/views.py', true); // Substitua pelo caminho correto
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
        
        xhr.onload = function() {
            if (xhr.status >= 200 && xhr.status < 400) {
                // A requisição foi bem-sucedida
                var resposta = JSON.parse(xhr.responseText);
                console.log(resposta);
            } else {
                // Houve um erro na requisição
                console.error('Erro na requisição:', xhr);
            }
        };
        
        xhr.onerror = function() {
            console.error('Erro na requisição:', xhr);
        };
        
        xhr.send(JSON.stringify({ numeros: numeros }));
    });
});
