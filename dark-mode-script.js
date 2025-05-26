<script>
document.addEventListener('DOMContentLoaded', function() {
  // Create dark mode toggle button
  const toggleBtn = document.createElement('button');
  toggleBtn.className = 'theme-toggle';
  toggleBtn.setAttribute('aria-label', 'Toggle dark mode');
  toggleBtn.innerHTML = '<svg class="theme-toggle-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59-8 8-8z"></path><path d="M12 17c2.76 0 5-2.24 5-5s-2.24-5-5-5v10z"></path></svg>';

  // Add the button to the navbar
  const navbar = document.querySelector('.navbar-container');
  if (navbar) {
    const navContainer = document.createElement('div');
    navContainer.className = 'nav-item theme-toggle-container';
    navContainer.appendChild(toggleBtn);
    navbar.appendChild(navContainer);
  }

  // Check for saved theme preference or system preference
  const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
  const currentTheme = localStorage.getItem('theme') || (prefersDarkScheme.matches ? 'dark' : 'light');
  
  // Set initial theme
  document.documentElement.setAttribute('data-theme', currentTheme);
  
  if (currentTheme === 'dark') {
    document.body.classList.add('quarto-dark');
    document.body.classList.remove('quarto-light');
    toggleBtn.classList.add('dark');
  } else {
    document.body.classList.add('quarto-light');
    document.body.classList.remove('quarto-dark');
  }
  
  // Toggle theme function
  toggleBtn.addEventListener('click', function() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    document.body.classList.toggle('quarto-dark');
    document.body.classList.toggle('quarto-light');
    toggleBtn.classList.toggle('dark');
    
    localStorage.setItem('theme', newTheme);
    
    // Update MathJax rendering if available
    if (window.MathJax) {
      window.MathJax.Hub.Queue(['Rerender', window.MathJax.Hub]);
    }
    
    // Update Prism highlighting if available
    if (window.Prism) {
      Prism.highlightAll();
    }
  });
});
</script>
