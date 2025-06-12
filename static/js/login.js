document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    // Simulação de login
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    if (username && password) {
        alert('Login realizado com sucesso!');
    } else {
        alert('Preencha todos os campos.');
    }
});