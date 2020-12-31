/**
 *	www.templatemo.com
 */

/* HTML document is loaded. DOM is ready.
-----------------------------------------*/
$(document).ready(function () {

  // Mobile menu
  $('.mobile-menu-icon').click(function () {
    $('.tm-nav').slideToggle();
  });

  $(window).resize(function () {
    if ($(window).width() > 767) {
      $('.tm-nav').show();
    } else {
      $('.tm-nav').hide();
    }
  });

  // http://stackoverflow.com/questions/2851663/how-do-i-simulate-a-hover-with-a-touch-in-touch-enabled-browsers
  $('body').bind('touchstart', function () { });

  // Smooth scroll
  // https://css-tricks.com/snippets/jquery/smooth-scrolling/
  $('a[href*=#]:not([href=#])').click(function () {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });

});

$(window).load(function () {
  // Remove preloader
  // https://ihatetomatoes.net/create-custom-preloading-screen/
  $('body').addClass('loaded');
});

//active elements
$(document).on('click', '.tm-nav ul li', function () {
  $(this).addClass('active').siblings().removeClass('active');
  console.log($(this));
  localStorage.setItem("clicked", $(this).index());
})

window.onload = function () {
  var clicked = localStorage.getItem('clicked');
  console.log(clicked);
  $('.tm-nav ul li.active').removeClass('active');
  $('.tm-nav ul li').eq(clicked).addClass('active');
}
