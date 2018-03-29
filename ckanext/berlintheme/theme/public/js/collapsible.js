(function($) {
  $(document).ready(function(){
    /* MAIN NAVIGATION DROPDOWN */
    $(function(){
      $(".content-navi-top ul.level1 li").hover(function(){
          $(this).addClass("hover");
          $('ul:first',this).css('visibility', 'visible');
      }, function(){
          $(this).removeClass("hover");
          $('ul:first',this).css('visibility', 'hidden');
      });
      //$(".content-navi-top ul.level1 li ul li:has(ul)").find("a:first").append(" <span class='arrow'>&raquo;</span>");
      $(".content-navi-top ul.level1 li ul li:has(ul)").addClass("arrow");
    });

    /* Filter form collapsible */
    $('.opener').css('cursor', 'pointer');

    $('.opener').bind('click', function(){
        toggleForm(200);
    });

    if (getParameterByName("state") == "open") {
      toggleForm(0);
    }

    function toggleForm(speed) {
        $('.collapsible-form').slideToggle(speed);
        if ($('.opener .symbol-chevron-circle-down').length > 0) {
          // opening
            $('.opener .symbol-chevron-circle-down').replaceWith("<span class='symbol-chevron-circle-up'></span>");
            $("#collapse_form_check").prop("checked", true);
        } else if ($('.opener .symbol-chevron-circle-up').length > 0) {
            // closing
            $('.opener .symbol-chevron-circle-up').replaceWith("<span class='symbol-chevron-circle-down'></span>")
            $("#collapse_form_check").prop("checked", false);
            $(".pagination li a").each(function() { 
              var href= $(this).attr("href").replace("&state=open", "");
              $(this).attr("href", href); 
            });
        }
    };

    function getParameterByName(name) {
        url = window.location.href;
        name = name.replace(/[\[\]]/g, "\\$&");
        var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
            results = regex.exec(url);
        if (!results) return null;
        if (!results[2]) return '';
        return decodeURIComponent(results[2].replace(/\+/g, " "));
    }

  });
})(jQuery);
