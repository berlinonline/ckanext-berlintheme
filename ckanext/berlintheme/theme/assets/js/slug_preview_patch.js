// Monkey patch of the slug-preview jQuery plugin that 
// changes the template

$(function () {
    var old = $.fn.slugPreview;

    $.fn.slugPreview = function (options) {
        options = options || {};

        options.template = `
            <div class="slug-preview">
                <strong></strong>
                <span class="slug-preview-prefix"></span>
                <span class="slug-preview-value"></span>
                <button class="btn btn-primary btn-xs" aria-label="Datensatz-URL bearbeiten"></button>
            </div>
        `;

        return old.call(this, options);
    };
});