ckan.module('berlin-link-input', function (jQuery) {
  // assuming we have a link to an error in the error overview
  // above a form:
  // 
  // <li data-field-label="title">
  //    <a href="#field-title" data-module="berlin-link-input" data-module-field="title">Titel</a>:
  //      Bitte geben sie dem Datensatz einen Titel.
  // </li>
  // 
  // This module will focus on '#field-{field}' if the link is clicked on.
  
  return {
    options: {
      field: ''
    },
    initialize: function () {
      this.el.on("click", e => {
        $('#field-' + this.options.field).focus();
      });
    }
  };
});

$(function () {
    const $invalid = $(".is-invalid").first();
    if ($invalid.length) {
      console.log("there is an invalid element");
      // focus on the first error
      // $invalid[0].focus({ preventScroll: true });
      $invalid.focus();
    }
});
