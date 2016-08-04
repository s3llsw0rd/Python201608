$(function(){

    // Do Stuff
    $('.dp').datepicker();
    $('form p').hide();

    // Stop Form Submission
    $('form').submit(function(){
      
      /*
      [x] Make sure your page doesn't allow the form to submit in any case.
      [x] Design a simple registration form with validation.
      [ ] If the required information is there when the form is submitted, an alert box will pop up with the valid information being displayed.
      [ ] If the name is not included, have an error message appear.
      */

      var from = $('#from').val().trim();
      var to = $('#to').val().trim();
      var name = $('#name').val().trim();
      $('form p').hide();

      if (from.length == 0) {
        $('form p:first').show();
        return false;
      }

      if (to.length == 0) {
        $('form p:nth-of-type(2)').show();
        return false;
      }

      if (name.length == 0) {
        $('form p:last').show();
        return false;
      }


      var msg = "Thanks " + name + "!  Your Cruise leaves on "+ from +" and returns "+to+"!";
      alert(msg);

      return false;
    });

  });