// Wait for the page to finish loading
document.addEventListener('DOMContentLoaded', function() {
  // Function to animate a single counter
  function animateCounter(counter, endValue) {
    var startValue = 0;
    var duration = 2000; // Animation duration in milliseconds

    var range = endValue - startValue;
    var increment = endValue > startValue ? 1 : -1;
    var step = Math.abs(Math.floor(duration / range));

    var timer = setInterval(function () {
      startValue += increment;
      counter.textContent = startValue + "+"; // Add the "+" sign after the counter value

      if ((increment > 0 && startValue >= endValue) || (increment < 0 && startValue <= endValue)) {
        clearInterval(timer);
        counter.textContent = endValue + "+"; // Add the "+" sign after the final value
      }
    }, step);
  }

  // Function to check if the section is in the viewport
  function checkSectionInView() {
    // Get the section element
    var section = document.getElementById('section_2');

    // Get the viewport height
    var viewportHeight = window.innerHeight || document.documentElement.clientHeight;

    // Calculate the position at which the animation should start
    var sectionPosition = section.offsetTop - (viewportHeight / 2);

    // Get the current scroll position
    var scrollPosition = window.pageYOffset || document.documentElement.scrollTop;

    // Check if the scroll position is greater than or equal to the section position
    if (scrollPosition >= sectionPosition) {
      // Animate the counters
      var counters = document.getElementsByClassName('counter');
      for (var i = 0; i < counters.length; i++) {
        var counter = counters[i];
        var endValue = parseInt(counter.getAttribute('data-end-value'));
        animateCounter(counter.querySelector('span'), endValue); // Pass the span element to animate the counter value
      }

      // Remove the event listener once the animation is triggered
      window.removeEventListener('scroll', checkSectionInView);
    }
  }

  // Attach the event listener to the scroll event
  window.addEventListener('scroll', checkSectionInView);
});
