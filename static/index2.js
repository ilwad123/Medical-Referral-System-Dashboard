const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
const themeToggler = document.querySelector(".theme-toggler");

// show sidebar
menuBtn.addEventListener('click', () => {
    sideMenu.style.display = 'block';
})

// close sidebar
closeBtn.addEventListener('click', () => {
    sideMenu.style.display = 'none';
})
//used to show the right link 
document.addEventListener("DOMContentLoaded", function() {
    const currentLocation = window.location.pathname;
    const sidebarLinks = document.querySelectorAll(".sidebar a");

    sidebarLinks.forEach(link => {
        link.classList.remove("active");
        if (link.getAttribute("href") === currentLocation) {
            link.classList.add("active");
        }
    });
});



document.addEventListener('DOMContentLoaded', function() {
    // Check if the theme mode preference is stored in local storage
    const storedThemeMode = localStorage.getItem('themeMode');
    const themeToggler = document.querySelector('.theme-toggler');

    // Apply the stored theme mode
    if (storedThemeMode === 'dark') {
        toggleDarkMode();
    } else {
        toggleLightMode();
    }

    if (themeToggler) {
        themeToggler.addEventListener('click', toggleThemeMode);
    }

    function toggleThemeMode() {
        if (document.body.classList.contains('dark-theme-variables')) {
            toggleLightMode();
        } else {
            toggleDarkMode();
        }
    }

    function toggleDarkMode() {
        document.body.classList.add('dark-theme-variables');
        localStorage.setItem('themeMode', 'dark');
        updateThemeTogglerIcons(true);
    }

    function toggleLightMode() {
        document.body.classList.remove('dark-theme-variables');
        localStorage.setItem('themeMode', 'light');
        updateThemeTogglerIcons(false);
    }

    function updateThemeTogglerIcons(isDarkMode) {
        const themeTogglerSpans = themeToggler.querySelectorAll('span');
        themeTogglerSpans[0].classList.toggle('active', !isDarkMode);
        themeTogglerSpans[1].classList.toggle('active', isDarkMode);
    }
});

