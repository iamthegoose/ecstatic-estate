window.addEventListener('scroll', function() {
  const header = document.getElementById('header');
  if (window.scrollY > 0) {
    header.classList.add('scrolled');
    header.classList.remove('top');
  } else {
    header.classList.add('top');
    header.classList.remove('scrolled');
  }
});

document.addEventListener('DOMContentLoaded', function() {
  const languageToggle = document.getElementById('language-toggle');
  const languageOptions = document.querySelector('.language-options');

  languageToggle.addEventListener('click', function(event) {
    event.preventDefault();
    event.stopPropagation();
    toggleLanguageOptions();
  });

  // Додання обробника події для закриття випадаючого списку при натисканні поза ним
  document.addEventListener('click', function(event) {
    let isClickInside = languageToggle.contains(event.target) || languageOptions.contains(event.target);
    if (!isClickInside) {
      languageOptions.style.display = 'none';
    }
  });

  // Функція для перемикання відображення випадаючого списку
  function toggleLanguageOptions() {
    if (languageOptions.style.display === 'block') {
      languageOptions.style.display = 'none';
    } else {
      languageOptions.style.display = 'block';
    }
  }
});