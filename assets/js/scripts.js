// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
    // Select the menu toggle button and the navigation menu
    const menuToggle = document.querySelector(".menu-toggle");
    const navMenu = document.querySelector(".nav-menu");

    // Add a click event listener to the menu toggle button
    menuToggle.addEventListener("click", () => {
        // Toggle the "active" class on the navigation menu
        navMenu.classList.toggle("active");

        // Optionally change the button's appearance (e.g., toggle a class)
        menuToggle.classList.toggle("open");
    });
});

  // Wait for the page to load
  window.addEventListener('DOMContentLoaded', () => {
    // Select the audio element
    const audio = document.querySelector('.audio');

    // Play the audio automatically
    audio.play().catch(error => {
      console.error('Audio playback failed:', error);
    });
  });