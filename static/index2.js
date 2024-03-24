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


document.addEventListener('DOMContentLoaded', function() {
    // Check if the theme mode preference is stored in local storage
    const storedThemeMode = localStorage.getItem('themeMode');
    if (storedThemeMode === 'dark') {
        // If the theme mode is set to dark, apply dark mode styles
        document.body.classList.add('dark-theme-variables');
        // Update the theme toggler icon to reflect the dark mode
        themeToggler.querySelector('span:nth-child(1)').classList.add('active');
        themeToggler.querySelector('span:nth-child(2)').classList.add('active');
    }

    // Add event listener to the theme toggler button
    const themeToggler = document.querySelector('.theme-toggler');
    if (themeToggler) {
        themeToggler.addEventListener('click', toggleThemeMode);
    }

    function toggleThemeMode() {
        document.body.classList.toggle('dark-theme-variables');

        themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
        themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');

        const currentThemeMode = document.body.classList.contains('dark-theme-variables') ? 'dark' : 'light';
        localStorage.setItem('themeMode', currentThemeMode);
    }

});
