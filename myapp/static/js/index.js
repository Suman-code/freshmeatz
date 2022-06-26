$(document).ready(function (){
    $('.owl-carousel').owlCarousel({
        items:1,
        loop:true, 
        autoplay:true,
        autoplayTimeout:3000,
        autoplayHoverPause:true,
        nav : false,
        dots : false,
    });
    $('.play').on('click',function(){
        owl.trigger('play.owl.autoplay',[1000])
    })
    $('.stop').on('click',function(){
        owl.trigger('stop.owl.autoplay')
    })


})


$('#slider1').owlCarousel({
    items:3,
    loop:true,
    margin : 10,
    nav : true,
    dots:false,
    navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],

    responsiveClass:true,
    
    responsive:{
        0:{
            items:1,
            nav:true,
            autoplay:true,
            autoplayTimeout:3000,
            loop: true
        },
        600:{
            items:3,
            nav:false
        },
        1000:{
            items:3,
            nav:true,
            loop:true
        }
    }

    
})


$('#slider3').owlCarousel({
    items:3,
    loop:true,
    margin : 15,
    nav : false,
    dots:false,
    //navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],

    responsiveClass:true,
    
    responsive:{
        0:{
            items:1,
            nav:true,
            autoplay:true,
            autoplayTimeout:3000,
            loop: true
        },
        600:{
            items:3,
            nav:false
        },
        1000:{
            items:3,
            nav:true,
            loop:true
        }
    }

 
})

 
$('#slider4').owlCarousel({
    items:3,
    loop:true,
    margin : 15,
    nav : false,
    dots:false,
    //navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],

    responsiveClass:true,
    
    responsive:{
        0:{
            items:1,
            nav:true,
            autoplay:true,
            autoplayTimeout:3000,
            loop: true
        },
        600:{
            items:3,
            nav:false
        },
        1000:{
            items:3,
            nav:true,
            loop:true
        }
    }

    
})


$('#slider4 , #slider5 ').owlCarousel({
    items:3,
    loop:true,
    margin : 15,
    nav : false,
    dots:false,
    //navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],

    responsiveClass:true,
    
    responsive:{
        0:{
            items:2,
            nav:false,
            autoplay:true,
            autoplayTimeout:3000,
            loop: true
        },
        600:{
            items:3,
            nav:false,
            autoplay:true,
            autoplayTimeout:3000,
        },
        1000:{
            items:3,
            nav:true,
            autoplay:true,
            autoplayTimeout:3000,
            loop:true
        }
    }

    
})




/*  live sale countdown clock

// Set the date we're counting down to
var countDownDate = new Date("Mar 22, 2023 2:55:25").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();
    
  // Find the distance between now and the count down date
  var distance = countDownDate - now;
    
  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    
  // Output the result in an element with id="demo"
  document.getElementById("livesale").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";
    
  // If the count down is over, write some text 
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("demo").innerHTML = "EXPIRED";
  }}, 1000);
*/


  

  /* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function profileDropdown() {
    document.getElementById("dropDown-content").classList.toggle("show");
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.profileDropbtn')) {
      var dropdowns = document.getElementsByClassName("profileDropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }








