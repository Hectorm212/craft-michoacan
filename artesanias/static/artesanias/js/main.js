document.addEventListener("DOMContentLoaded", function() {
    
    const cartBtn = document.getElementById("cartBtn");
    if (cartBtn) {
        cartBtn.addEventListener("click", function() {
            console.log("Abrir el menú lateral del carrito...");
        });
    }

    const currentUrl = window.location.pathname;
    const navLinks = document.querySelectorAll(".nav-item");
    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentUrl) {
            link.style.fontWeight = "700";
            link.style.borderBottom = "2px solid #8c5333";
        }
    });

    const btnMinus = document.getElementById('btn-minus');
    const btnPlus = document.getElementById('btn-plus');
    const inputQty = document.getElementById('input-qty');

    
    if (btnMinus && btnPlus && inputQty) {
        btnMinus.addEventListener('click', () => {
            let val = parseInt(inputQty.value);
            if (isNaN(val) || val <= 1) {
                inputQty.value = 1;
            } else {
                inputQty.value = val - 1;
            }
        });

        btnPlus.addEventListener('click', () => {
            let val = parseInt(inputQty.value);
            if (isNaN(val) || val < 1) {
                inputQty.value = 1;
            } else {
                inputQty.value = val + 1;
            }
        });
    }
});