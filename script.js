// JavaScript for Mobile Menu
document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const closeMobileMenuButton = document.getElementById('close-mobile-menu');
    const mobileMenu = document.getElementById('mobile-menu');

    // Toggle mobile menu visibility
    mobileMenuButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('is-open');
    });

    // Close mobile menu explicitly with the close button
    closeMobileMenuButton.addEventListener('click', () => {
        mobileMenu.classList.remove('is-open');
    });

    // Close mobile menu when a link is clicked (for smooth scrolling)
    document.querySelectorAll('#mobile-menu a').forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.remove('is-open');
        });
    });
});

// Function to close mobile menu, called by inline onclick on menu links
function closeMobileMenu() {
    const mobileMenu = document.getElementById('mobile-menu');
    mobileMenu.classList.remove('is-open');
}