function contactForm() {
    var csrf = $('input[name="csrfmiddlewaretoken"]').attr("value");
        $.ajax({
        type: "POST",
        url: "/contact/",
        data: $('form').serializeArray(),
        headers: {
            'X-CSRFToken': csrf,
        },
        contentType: "application/javascript",
        dataType: "json",
    });
};
  
function validateEmail(email) {
    const res = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return res.test(String(email).toLowerCase());
};

$(document).ready(function(){
    var count = 0;
    $('#contact-button').on('click', function() {
      if (count == 1) {
        //do nothing
      } else if ($("input[name='first-name']").val() == "") {
        //do nothing
      } else if ($("input[name='last-name']").val() == "") {
        //do nothing
      } else if ($("input[name='subject']").val() == "") {
        //do nothing
      } else if ($("textarea[name='message']").val() == "") {
        //do nothing
      } else if ($("input[name='email']").val() == "") {
        //do nothing
      } else {
        var emailIsValid = validateEmail($("input[name='email']").val());
        if (emailIsValid) {
            count = count + 1;
            contactForm();
            $("#contact-button").replaceWith('<div class="success-animation"><svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52"><circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none" /><path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8" /></svg></div>');
        } else {
        //do nothing
        };
      };
    });
});