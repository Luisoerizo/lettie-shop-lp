// JavaScript for Mobile Menu
document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const closeMobileMenuButton = document.getElementById('close-mobile-menu');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuButton && mobileMenu && closeMobileMenuButton) {
        mobileMenuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('is-open');
            // Optional: Prevent body scroll when mobile menu is open
            // document.body.style.overflow = mobileMenu.classList.contains('is-open') ? 'hidden' : '';
        });

        closeMobileMenuButton.addEventListener('click', () => {
            mobileMenu.classList.remove('is-open');
            // document.body.style.overflow = '';
        });

        document.querySelectorAll('#mobile-menu a').forEach(link => {
            link.addEventListener('click', () => {
                closeMobileMenu(); 
            });
        });
    }

    // JavaScript for Image Zoom Modal
    const imageZoomModal = document.getElementById('imageZoomModal');
    const zoomedImage = document.getElementById('zoomedImage');
    const closeZoomModalButton = document.getElementById('closeZoomModal');
    
    // Updated selector to include all images intended for zoom.
    // This now includes images within .category-card and any img with class .js-zoomable-image
    const zoomableImages = document.querySelectorAll('.category-card img, img.js-zoomable-image');

    if (imageZoomModal && zoomedImage && closeZoomModalButton && zoomableImages.length > 0) {
        zoomableImages.forEach(image => {
            // Make the image itself clickable if it's a .js-zoomable-image
            // For .category-card, the card itself is usually the click target, but we target the img for consistency.
            let clickTarget = image.closest('.category-card') || image;
            
            clickTarget.style.cursor = 'pointer'; // Add pointer cursor to indicate clickability

            clickTarget.addEventListener('click', function(event) {
                // Prevent default if the click target is an anchor tag (like category-card was originally)
                if (this.tagName === 'A') {
                    event.preventDefault();
                }
                
                const imgElement = this.tagName === 'IMG' ? this : this.querySelector('img'); // Get the image element

                if (imgElement && imgElement.src) {
                    zoomedImage.src = imgElement.src;
                    imageZoomModal.classList.remove('hidden');
                    document.body.style.overflow = 'hidden'; // Prevent background scrolling
                }
            });
        });

        closeZoomModalButton.addEventListener('click', () => {
            imageZoomModal.classList.add('hidden');
            zoomedImage.src = ""; // Clear image src
            document.body.style.overflow = ''; // Restore background scrolling
        });

        imageZoomModal.addEventListener('click', (event) => {
            if (event.target === imageZoomModal) { 
                imageZoomModal.classList.add('hidden');
                zoomedImage.src = "";
                document.body.style.overflow = '';
            }
        });

        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape' && !imageZoomModal.classList.contains('hidden')) {
                imageZoomModal.classList.add('hidden');
                zoomedImage.src = "";
                document.body.style.overflow = '';
            }
        });
    }
});

function closeMobileMenu() {
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileMenu) {
        mobileMenu.classList.remove('is-open');
        // document.body.style.overflow = ''; 
    }
}
