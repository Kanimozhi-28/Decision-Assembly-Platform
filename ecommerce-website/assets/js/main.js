document.addEventListener('DOMContentLoaded', () => {
    const cartBtn = document.querySelector('.cart-btn');
    const cartCountElement = document.querySelector('.cart-count');
    const addToCartButtons = document.querySelectorAll('.add-to-cart');

    let cartCount = 0;

    // Add to cart functionality (UI only)
    addToCartButtons.forEach(button => {
        button.addEventListener('click', () => {
            cartCount++;
            cartCountElement.textContent = cartCount;

            // Subtle animation feedback
            button.textContent = 'Added!';
            button.style.backgroundColor = '#10b981'; // Green
            button.style.color = '#fff';

            setTimeout(() => {
                button.textContent = 'Add to Cart';
                button.style.backgroundColor = '';
                button.style.color = '';
            }, 1000);

            // Simple bounce effect on cart icon
            cartBtn.style.transform = 'scale(1.2)';
            setTimeout(() => {
                cartBtn.style.transform = 'scale(1)';
            }, 200);
        });
    });

    // Smooth scroll for nav links (if any)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});
