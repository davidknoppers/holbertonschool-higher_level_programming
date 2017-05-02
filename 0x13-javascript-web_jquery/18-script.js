$('#toggle_header').ready(function () {
  $('#toggle_header').addClass('green');
});
$('#toggle_header').click(function () {
  if ($('#toggle_header').hasClass('green')) {
    $('#toggle_header').addClass('red').removeClass('green');
  } else if ($('#toggle_header').hasClass('red')) {
    $('#toggle_header').addClass('green').removeClass('red');
  }
});
