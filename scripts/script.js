window.addEventListener('scroll', function() {
  var header = document.getElementById('header');
  if (window.scrollY > 0) {
    header.classList.add('scrolled');
    header.classList.remove('top');
  } else {
    header.classList.add('top');
    header.classList.remove('scrolled');
  }
});

document.addEventListener('DOMContentLoaded', function() {
  var languageToggle = document.getElementById('language-toggle');
  var languageOptions = document.querySelector('.language-options');

  languageToggle.addEventListener('click', function(event) {
    event.preventDefault(); // Зупинити типову поведінку посилання
    event.stopPropagation(); // Зупинити подальше поширення події, щоб не сховати випадаючий список одразу
    toggleLanguageOptions();
  });

  // Додання обробника події для закриття випадаючого списку при натисканні поза ним
  document.addEventListener('click', function(event) {
    var isClickInside = languageToggle.contains(event.target) || languageOptions.contains(event.target);
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