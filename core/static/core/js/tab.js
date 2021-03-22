$(document).ready(function () {
  $('#tabs li').on('click', function () {
    var tab = $(this).data('tab');
    
    $('#tabs li').removeClass('is-active');
    $(this).addClass('is-active');
    
    $('#tab-content div.tab-content-item').removeClass('is-hidden');
    $('#tab-content div.tab-content-item').addClass('is-hidden');
    $('div[data-content="' + tab + '"]').removeClass('is-hidden');
  });
});