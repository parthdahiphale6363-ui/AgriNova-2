/**
 * Agrinova - Main JavaScript File
 * Created by Parth Dahiphale
 */

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS (Animate on Scroll)
    AOS.init({
        duration: 1000,
        once: true,
        offset: 100
    });

    // Initialize all components
    initPreloader();
    initNavigation();
    initTheme();
    initLanguage();
    initBackToTop();
    initForms();
    initSmoothScroll();
});

/**
 * Preloader
 */
function initPreloader() {
    const preloader = document.querySelector('.preloader');

    window.addEventListener('load', function() {
        setTimeout(() => {
            preloader.classList.add('fade-out');
        }, 500);
    });
}

/**
 * Navigation
 */
function initNavigation() {
    const navbar = document.getElementById('navbar');
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navMenu');
    const navLinks = document.querySelectorAll('.nav-links a');

    // Scroll effect
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Active link based on scroll position
        updateActiveLink();
    });

    // Mobile menu toggle
    menuToggle.addEventListener('click', function() {
        navMenu.classList.toggle('active');
        menuToggle.innerHTML = navMenu.classList.contains('active') ?
            '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
    });

    // Close menu when clicking a link
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navMenu.classList.remove('active');
            menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
        });
    });

    // Update active link based on scroll
    function updateActiveLink() {
        const sections = document.querySelectorAll('section[id]');
        const scrollPosition = window.scrollY + 100;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }
}

/**
 * Theme Toggle (Light/Dark Mode)
 */
function initTheme() {
    const themeToggle = document.getElementById('themeToggle');
    const icon = themeToggle.querySelector('i');

    // Check for saved theme preference
    const savedTheme = localStorage.getItem('agrinova_theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    }

    themeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');

        if (document.body.classList.contains('dark-mode')) {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
            localStorage.setItem('agrinova_theme', 'dark');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
            localStorage.setItem('agrinova_theme', 'light');
        }
    });
}

/**
 * Language Selector
 */
function initLanguage() {
    const languageSelect = document.getElementById('languageSelect');

    // Load saved language
    const savedLanguage = localStorage.getItem('agrinova_language') || 'en';
    languageSelect.value = savedLanguage;

    languageSelect.addEventListener('change', function() {
        const selectedLanguage = this.value;
        localStorage.setItem('agrinova_language', selectedLanguage);
        changeLanguage(selectedLanguage);
    });
}

function changeLanguage(lang) {
    // This will be expanded with actual translations
    console.log(`Changing language to: ${lang}`);

    // Example translations (expand based on needs)
    const translations = {
        en: {
            'welcome': 'Welcome to Agrinova',
            // Add more translations
        },
        hi: {
            'welcome': 'अग्रिनोवा में आपका स्वागत है',
            // Add more translations
        },
        ta: {
            'welcome': 'அக்ரினோவாவுக்கு வரவேற்கிறோம்',
            // Add more translations
        }
    };

    // Update text content for elements with data-i18n attribute
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            element.textContent = translations[lang][key];
        }
    });
}

/**
 * Back to Top Button
 */
function initBackToTop() {
    const backToTop = document.getElementById('backToTop');

    window.addEventListener('scroll', function() {
        if (window.scrollY > 500) {
            backToTop.classList.add('show');
        } else {
            backToTop.classList.remove('show');
        }
    });

    backToTop.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/**
 * Form Handling
 */
function initForms() {
    // Link range sliders with number inputs
    const rangeInputs = document.querySelectorAll('input[type="range"]');

    rangeInputs.forEach(range => {
        const numberInput = document.getElementById(range.id.replace('Range', ''));

        if (numberInput) {
            // Update number input when range changes
            range.addEventListener('input', function() {
                numberInput.value = this.value;
            });

            // Update range when number input changes
            numberInput.addEventListener('input', function() {
                range.value = this.value;
            });
        }
    });

    // Get location button
    const getLocationBtn = document.getElementById('getLocation');
    if (getLocationBtn) {
        getLocationBtn.addEventListener('click', function() {
            if (navigator.geolocation) {
                getLocationBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Getting location...';
                getLocationBtn.disabled = true;

                navigator.geolocation.getCurrentPosition(
                    function(position) {
                        const lat = position.coords.latitude;
                        const lon = position.coords.longitude;

                        // Reverse geocoding to get location name
                        fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`)
                            .then(response => response.json())
                            .then(data => {
                                const location = data.address;
                                const locationString = [
                                    location.village || location.town || location.city,
                                    location.state,
                                    location.country
                                ].filter(Boolean).join(', ');

                                document.getElementById('location').value = locationString;

                                // Also update weather with this location
                                if (typeof updateWeather === 'function') {
                                    updateWeather(lat, lon);
                                }
                            })
                            .catch(error => {
                                console.error('Error getting location name:', error);
                                document.getElementById('location').value = `${lat}, ${lon}`;
                            })
                            .finally(() => {
                                getLocationBtn.innerHTML = '<i class="fas fa-crosshairs"></i> Use My Location';
                                getLocationBtn.disabled = false;
                            });
                    },
                    function(error) {
                        alert('Error getting location: ' + error.message);
                        getLocationBtn.innerHTML = '<i class="fas fa-crosshairs"></i> Use My Location';
                        getLocationBtn.disabled = false;
                    }
                );
            } else {
                alert('Geolocation is not supported by your browser');
            }
        });
    }
}

/**
 * Smooth Scroll for Anchor Links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * Utility Functions
 */
function showToast(message, type = 'info') {
    // Create toast element
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
        <i class="fas ${type === 'success' ? 'fa-check-circle' : 
                         type === 'error' ? 'fa-exclamation-circle' : 
                         'fa-info-circle'}"></i>
        <span>${message}</span>
    `;

    document.body.appendChild(toast);

    // Show toast
    setTimeout(() => toast.classList.add('show'), 100);

    // Remove toast after 3 seconds
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

function formatDate(date) {
    return new Date(date).toLocaleDateString('en-IN', {
        day: 'numeric',
        month: 'short',
        year: 'numeric'
    });
}

function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(amount);
}

// Export utilities for use in other scripts
window.Agrinova = {
    showToast,
    formatDate,
    formatCurrency
};