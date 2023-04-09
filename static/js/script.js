document.addEventListener('DOMContentLoaded', function() {
  // Add event listeners to the buttons
  document.querySelector('#pick-excuse').addEventListener('click', function() {
    alert("Sorry, I'm all out of excuses!");
  });
  document.querySelector('#random-excuse').addEventListener('click', function() {
    alert("I couldn't make it because I had to attend a virtual meeting.");
  });
  document.querySelector('#feeling-lucky').addEventListener('click', function() {
    alert('Congratulations, you are feeling lucky!');
  });
});
