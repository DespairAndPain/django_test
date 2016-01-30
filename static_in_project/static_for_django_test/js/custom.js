
$( '#po' ).submit(function( event ) {
 
  // Stop form from submitting normally
  event.preventDefault();
 
  // Send the data using post
  var posting = $.post( 'views.py', { s: term } );
  console.log('WORK');
  posting;

});

$(document).ready(function() {
$('#po').on('submit', function(event){
    console.log("form submitted!")  // sanity check
});});