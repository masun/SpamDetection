
$(document).ready(function(){
  
  // Modelado scrolspy

  var nosotros = $("#about").offset().top
  var servicios = $("#services").offset().top
  var portafolio = $("#portfolio").offset().top
  var contacto = $("#contact").offset().top


  $(".navigation nav ul li a.inicio").addClass("activo");

  $(window).scroll(function() {      
      var barra = $(".cf").offset().top + $(".cf").innerHeight();
      
      if (barra < nosotros) {
        $(".navigation nav ul li a.inicio").addClass("activo"); 
      }else{
        $(".navigation nav ul li a.inicio").removeClass("activo");   
      }

      if (barra >= nosotros && barra < servicios) {
        $(".navigation nav ul li a.nosotros").addClass("activo"); 
      }else{
        $(".navigation nav ul li a.nosotros").removeClass("activo");   
      }

      if (barra >= servicios && barra < portafolio) {
        $(".navigation nav ul li a.servicios").addClass("activo"); 
      }else{
        $(".navigation nav ul li a.servicios").removeClass("activo");   
      }

      if (barra >= portafolio && barra < contacto) {
        $(".navigation nav ul li a.portafolio").addClass("activo"); 
      }else{
        $(".navigation nav ul li a.portafolio").removeClass("activo");   
      }

      if (barra >= contacto) {
        $(".navigation nav ul li a.contacto").addClass("activo"); 
      }else{
        $(".navigation nav ul li a.contacto").removeClass("activo");   
      }

     /* var barraTop = $(".cf").scrollTop();
        if (pos < winTop) {
          $(".navigation nav ul li a").addClass("activo");
        }*/
   
  });

  // Hover encima de slider muestra las flechas.
  $("#myCarousel").hover(function(){
      $(".carousel-control.right, .carousel-control.left").css("display", "block");
      }, function(){
      $(".carousel-control.right, .carousel-control.left").css("display", "none");
  });


  // Add smooth scrolling to all links in navbar + footer link
  $(".mobimenu a, footer a[href='#myPage']").on('click', function(event) {

    // Prevent default anchor click behavior
    event.preventDefault();

    // Store hash
    var hash = this.hash;

    // Using jQuery's animate() method to add smooth page scroll
    // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
    $('html, body').stop(true,true).animate({
      scrollTop: $(hash).offset().top
    }, 1000, function(){
   
      // Add hash (#) to URL when done scrolling (default click behavior)
      window.location.hash = hash;
    });
  });
  
  // Slide in elements on scroll
  $(window).scroll(function() {
    $(".slideanim").each(function(){
      var pos = $(this).offset().top;

      var winTop = $(window).scrollTop();
        if (pos < winTop + 600) {
          $(this).addClass("slide1");
        }
    });
  });

    // Initialize Tooltip
  $('[data-toggle="tooltip"]').tooltip(); 
  

})