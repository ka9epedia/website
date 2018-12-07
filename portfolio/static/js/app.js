/* Script for preloader begin */
var preloader = document.getElementById('preloader');

window.addEventListener('load', function () {
    document.getElementById("preloader").style.opacity = 0;
    document.getElementById("wrapper").style.opacity = 1;
    document.getElementsByTagName('html')[0].style.overflow = "auto";
    setTimeout(function () {
        document.getElementById("preloader").remove();
    }, 1000);
});
/* Script for preloader end */

/* Script for sidenav begin */
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {
        edge: 'right',
    });
});
/* Script for sidenav end */

/* Script for typing effect begin */
$(window).on('load', function () {
    var typed = new Typed('#type', {
        strings: [
            "Welcome to OdaLab Website",
            "Start scrolling to study more about us",
        ],
        typeSpeed: 60,
        backSpeed: 60,
        loop: true,
        loopCount: Infinity
    });
});
/* Script for typing effect begin */

/* Smooth scroll to a section begin */
$(document).ready(function () {
    $("nav li a, .sidenav a, #scroll-btn li a").click(function (event) {
        event.preventDefault();
        var url = this.getAttribute('href');
        if (url !== '#') {
            var offset = 60;
            if ($(url).length) {
                $('html, body').stop().animate({
                    scrollTop: $(url).offset().top - offset
                }, 1000);
            }
        }
    });
});
/* Smooth scroll to a section end */

/* Script for active link switching begin */
$(document).ready(function () {
    $(window).scroll(function () {
        var currentLocation = window.pageYOffset;
        var navLinks = $("nav li a");
        var offset = 64;
        navLinks.each(function () {
            var url = $(this.hash);
            if ($(url).length) {
                var sectionOffset = $(url).offset().top - offset;
                if (sectionOffset <= currentLocation) {
                    $(this).addClass('active');
                    $(this).parent().siblings().children().removeClass('active');
                }
            }
        });
    });
});
/* Script for active link switching end */

/* Script for animated scrolling navbar begin */
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(document).scrollTop() >= $('#about').offset().top - 64) {
            $('nav').addClass('shrink');
            // Sidenav close button position change on scroll for mobile devices
            if (window.matchMedia('(max-width: 600px)').matches) {
                $('#sidenav-close').css('top', '-20px');
            }
        } else {
            $('nav').removeClass('shrink');
            // Sidenav close button position change on scroll for mobile devices
            if (window.matchMedia('(max-width: 600px)').matches) {
                $('#sidenav-close').css('top', '0px');
            }
        }
    });
});
/* Script for animated scrolling navbar end */

/* Script for forcing page scroll position to top at page refresh begin*/
$(document).ready(function () {
    $(this).scrollTop(0);
});
/* Script for forcing page scroll position to top at page refresh begin*/

/* Script for animating social links begin */
$(document).ready(function () {
    $('.zoomableLink').click(function () {
        $(this).css('transform', 'scale(1)');
    });

    $('.zoomableLink').hover(function () {
        $(this).css('transform', 'scale(1.2)');
    }, function () {
        $(this).css('transform', 'scale(1)');
    });
    // Stop resume link from doing anything
    $('#resumeLink').click(function (e) {
        e.preventDefault();
    });
});
/* Script for animating social links end */

/* Script for carousel begin */
$(document).ready(function () {
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: false,
    });

    $('.moveNextCarousel').click(function (e) {
        e.preventDefault();
        e.stopPropagation();
        $('.carousel').carousel('next');
    });

    $('.movePrevCarousel').click(function (e) {
        e.preventDefault();
        e.stopPropagation();
        $('.carousel').carousel('prev');
    });
});
/* Script for carousel end */

/* Script for modal begin */
$(document).ready(function () {
    $('.modal').modal();
});
/* Script for modal end */

/* Script for removing helper text of contact form begin */
$(document).ready(function () {
    $('.input-field input, .input-field textarea').focus(function () {
        $(this).siblings('.helper-text').text('');
    });
});
/* Script for removing helper text of contact form end */

/* Script for form submission using ajax begin */
$(document).ready(function () {
    var $myForm = $('#contactForm');
    $myForm.submit(function (e) {
        e.preventDefault()
        var $formData = $(this).serialize()
        var $thisURL = window.location.href
        $.ajax({
            method: "POST",
            url: $thisURL,
            data: $formData,
            success: function (data) {
                if (data.success) {
                    $('#flashMessage').animate({
                        opacity: 1
                    }, 1000);
                    $('#contactForm')[0].reset();
                } else {
                    var errors = data.errors;
                    $('.input-field input, .input-field textarea').removeClass("valid invalid");
                    for (var field in errors) {
                        $(`.input-field input[name=${field}], .input-field textarea[name=${field}]`).siblings('.helper-text').text(errors[field][0]);
                    }
                }
            },
        });
    });
});
/* Script for form submission using ajax end */

/* Script for closing flash message begin */
$(document).ready(function () {
    $('#flashClose').click(function () {
        $('#flashMessage').animate({
            opacity: 0
        }, 0);
    });
});
/* Script for closing flash message end */

/* Script for text blinking begin */
$(document).ready(function () {
    function blink_text() {
        $('.blink').fadeOut(1000);
        $('.blink').fadeIn(1000);
    }
    setInterval(blink_text, 1000);
});
/* Script for text blinking end */
