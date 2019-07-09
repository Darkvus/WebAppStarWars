// Fichero js personalizado.
$(document).ready(function () {
   $('#table').DataTable();
});


$(document).ready(function () {
   $("#id_search").autocomplete({
      source: function (request, response) {
         $.ajax({
            url: "/search/",
            dataType: "json",
            data: "term=" + request.term,
            success: function (data) {
               response($.map(data, function (item) {
                  if (item.type == 'film') {
                     var type = 'film'
                  } else if (item.type == 'personaje') {
                     var type = 'user'
                  } else {
                     var type = 'triangle-right';
                  }
                  return {
                     label: '<i style="padding-right: 3px;" class="glyphicon glyphicon-' + type + '"></i>' + item.text,
                     value: item.text
                  };
               }));
            }
         });
      },
      minLength: 2,
      open: function () {
         setTimeout(function () {
            $('.ui-autocomplete').css('z-index', "1031");
         }, 0);
      }
   }).data("ui-autocomplete")._renderItem = function (ul, item) {
      return $("<li></li>")
         .data("item.autocomplete", item)
         .append("<a>" + item.label + "</a>")
         .appendTo(ul);
   };
});