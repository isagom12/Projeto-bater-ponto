// Exemplo: esconder mensagens após alguns segundos
document.addEventListener("DOMContentLoaded", function () {
    const messages = document.querySelectorAll(".msg-success, .msg-danger");
  
    messages.forEach(msg => {
      setTimeout(() => {
        msg.style.display = "none";
      }, 5000); // Esconde depois de 5 segundos
    });
  });