// custom.js
window.matchMedia('(prefers-color-scheme: dark)')
      .addEventListener('change', event => {
  if (event.matches) {
      jtd.setTheme('dark');
  } else {
      jtd.setTheme('light');
  }
});

if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    jtd.setTheme('dark');
}

// Add this code
document.addEventListener('DOMContentLoaded', (event) => {
    const themeSwitch = document.querySelector('#theme-switch');
    const themeIcon = document.querySelector('#theme-icon');

    const lightIcon = '<svg class="theme-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 8a4 4 0 0 0-4 4 4 4 0 0 0 4 4 4 4 0 0 0 4-4 4 4 0 0 0-4-4m0 10a6 6 0 0 1-6-6 6 6 0 0 1 6-6 6 6 0 0 1 6 6 6 6 0 0 1-6 6m8-9.31V4h-4.69L12 .69 8.69 4H4v4.69L.69 12 4 15.31V20h4.69L12 23.31 15.31 20H20v-4.69L23.31 12 20 8.69Z"></path></svg>'; // brightness-4
    const darkIcon = '<svg class="theme-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 18c-.89 0-1.74-.2-2.5-.55C11.56 16.5 13 14.42 13 12c0-2.42-1.44-4.5-3.5-5.45C10.26 6.2 11.11 6 12 6a6 6 0 0 1 6 6 6 6 0 0 1-6 6m8-9.31V4h-4.69L12 .69 8.69 4H4v4.69L.69 12 4 15.31V20h4.69L12 23.31 15.31 20H20v-4.69L23.31 12 20 8.69Z"></path></svg>'; // brightness-5

    themeSwitch.addEventListener('change', (event) => {
        if (event.target.checked) {
            jtd.setTheme('dark');
            themeIcon.innerHTML = darkIcon;
        } else {
            jtd.setTheme('light');
            themeIcon.innerHTML = lightIcon;
        }
    });

    // Set the switch position and icon according to the current theme
    const currentTheme = jtd.getTheme();
    themeSwitch.checked = currentTheme === 'dark';
    themeIcon.innerHTML = currentTheme === 'dark' ? darkIcon : lightIcon;
});