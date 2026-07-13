document.addEventListener("DOMContentLoaded", function() {
    // Ejemplo de interactividad: Detectar clic en el botón del carrito
    const cartBtn = document.getElementById("cartBtn");
    
    if (cartBtn) {
        cartBtn.addEventListener("click", function() {
            console.log("Abrir el menú lateral del carrito...");
            // Aquí puedes añadir la lógica de tu e-commerce
        });
    }

    // Opcional: Marcar de forma automática la página activa en la que se encuentra el usuario
    const currentUrl = window.location.pathname;
    const navLinks = document.querySelectorAll(".nav-item");

    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentUrl) {
            link.style.fontWeight = "700";
            link.style.borderBottom = "2px solid #8c5333";
        }
    });
});