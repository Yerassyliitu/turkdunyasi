const universities = document.querySelectorAll('.university');

universities.forEach((university) => {
  const img = university.querySelector('img');
  const altImgSrc = img.getAttribute('alt') + '.jpg';

  university.addEventListener('mouseenter', () => {
    img.setAttribute('src', altImgSrc);
  });

  university.addEventListener('mouseleave', () => {
    img.setAttribute('src', img.getAttribute('src'));
  });
});

$(document).ready(function() {
  $(".content").hide();

  $("#button1").click(function() {
    $(".content").hide();
    $("#content1").show();
  });

  $("#button2").click(function() {
    $(".content").hide();
    $("#content2").show();
  });

  $("#button3").click(function() {
    $(".content").hide();
    $("#content3").show();
  });
});