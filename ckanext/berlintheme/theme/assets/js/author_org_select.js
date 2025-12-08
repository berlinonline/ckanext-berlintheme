// configure the author_uri select field using select2.js v3.5
// see https://select2.github.io/select2/

function mapOrgItem(item) {
    var text = item.label
    if (item.parent_abbreviation) {
        text = item.parent_abbreviation + " / " + item.label;
    }
    return {
        id: item.id,
        text: text
    };
}


document.addEventListener("DOMContentLoaded", function () {
    $('#field-author_uri').select2({
        placeholder: "Bitte eine Organisation auswählen.",
        ajax: {
            url: '/api/action/author_orgs_autocomplete',
            type: 'GET',
            dataType: 'json',
            quietMillis: 300,
            data: function (term) {
                return { q: term };
            },
            results: function (data) {
                return {
                    results: $.map(data.result, mapOrgItem)
                };
            }
        },
        minimumInputLength: 0,
        formatInputTooShort: function (input, min) {
            return "Bitte eine Organisation auswählen.";
        },
        initSelection: function (element, callback) {
            var id = $(element).val();
            if (id) {
            $.getJSON("/api/action/author_orgs_autocomplete", { id: id })
                .done(function (data) {
                var item = data.result[0];
                callback(mapOrgItem(item));
                });
            }
        }
    });
});
