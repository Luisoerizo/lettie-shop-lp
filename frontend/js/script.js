document.addEventListener('DOMContentLoaded', () => {

    // --- 1. DYNAMIC HEADER ON SCROLL (Su código original) ---
    const header = document.getElementById('main-header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // --- 2. MOBILE MENU LOGIC (Su código original) ---
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const closeMobileMenuButton = document.getElementById('close-mobile-menu');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuLinks = document.querySelectorAll('#mobile-menu a');

    const openMenu = () => {
        if (mobileMenu) mobileMenu.classList.add('is-open');
        document.body.style.overflow = 'hidden';
    };

    const closeMenu = () => {
        if (mobileMenu) mobileMenu.classList.remove('is-open');
        document.body.style.overflow = '';
    };

    if (mobileMenuButton && mobileMenu && closeMobileMenuButton) {
        mobileMenuButton.addEventListener('click', openMenu);
        closeMobileMenuButton.addEventListener('click', closeMenu);
        mobileMenuLinks.forEach(link => {
            link.addEventListener('click', closeMenu);
        });
    }

    // --- 3. FADE-IN ANIMATION ON SCROLL (Su código original) ---
    const scrollObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        rootMargin: '0px 0px -100px 0px'
    });

    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        scrollObserver.observe(el);
    });

    // --- 4. DYNAMIC PRODUCT LOADING (Nueva Lógica) ---
    const productListContainer = document.getElementById('product-list');

    /**
     * Crea el string de HTML para una sola tarjeta de producto.
     * @param {object} product - El objeto del producto con name, price, etc.
     * @returns {string} El HTML de la tarjeta del producto.
     */
    const renderProduct = (product) => {
        // NOTA: Usamos una imagen de placeholder. En el futuro, el modelo 'Product'
        // en la base de datos deberá tener un campo para la URL de la imagen.
        const imageUrl = "/images/vestido.webp"; // Placeholder temporal

        return `
            <div class="category-card animate-on-scroll">
                <img src="${imageUrl}" alt="${product.name}" loading="lazy" class="js-zoomable-image">
                <div class="category-name">
                    <span>${product.name.toUpperCase()}</span>
                    <span class="text-lg font-sans font-semibold block mt-1">$${product.price.toFixed(2)}</span>
                </div>
            </div>
        `;
    };

    /**
     * Obtiene los productos de la API y los muestra en la página.
     */
    const loadProducts = async () => {
        // Si el contenedor de productos no existe en esta página, no hacemos nada.
        if (!productListContainer) {
            return;
        }

        try {
            // Hacemos la petición a la API usando async/await para un código más limpio.
            const response = await fetch('http://127.0.0.1:8000/api/productos');

            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }

            const products = await response.json();

            // Limpiamos el contenedor antes de añadir nuevos elementos.
            productListContainer.innerHTML = '';

            if (products.length === 0) {
                productListContainer.innerHTML = '<p class="col-span-full text-center text-gray-600">No hay productos disponibles en este momento.</p>';
            } else {
                // Por cada producto, creamos su HTML y lo añadimos al contenedor.
                products.forEach(product => {
                    const productCardHTML = renderProduct(product);
                    productListContainer.insertAdjacentHTML('beforeend', productCardHTML);
                });
            }

        } catch (error) {
            console.error('Fallo al cargar los productos:', error);
            productListContainer.innerHTML = '<p class="col-span-full text-center text-red-500">Hubo un error al cargar los productos. Por favor, intente más tarde.</p>';
        }
    };

    // Finalmente, llamamos a la función para que se ejecute al cargar la página.
    loadProducts();

});