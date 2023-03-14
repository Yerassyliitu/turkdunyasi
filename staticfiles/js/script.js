function myFunction1() {
    document.getElementById("myDropdown1").classList.toggle("show");
  }
  
  // Закройте выпадающее меню, если пользователь щелкает за его пределами
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn1')) {
      var dropdowns = document.getElementsByClassName("dropdown-content1");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }



  function myFunction2() {
    document.getElementById("myDropdown2").classList.toggle("show");
  }
  
  // Закройте выпадающее меню, если пользователь щелкает за его пределами
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn2')) {
      var dropdowns = document.getElementsByClassName("dropdown-content2");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

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