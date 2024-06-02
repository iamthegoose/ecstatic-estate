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