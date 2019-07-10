// Fichero js personalizado.
$(document).ready(function () {
   $('.table').DataTable({
      "lengthMenu": [3, 10, 25, 50, 75, 100]
   });
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
                  var host = window.location.protocol + window.location.hostname + ':' + window.location.port;
                  if (item.type == 'film') {
                     var type = 'film'
                     return {
                        label: '<a href="/portal/film/detail/' + item.pk + '"><i style="padding-right: 3px;" class="glyphicon glyphicon-' + type + '"></i>' + item.text + '</a>',
                        value: item.text
                     };
                  } else if (item.type == 'personaje') {
                     var type = 'user';
                     return {
                        label: '<a href="/portal/personajes/detail/' + item.pk + '"><i style="padding-right: 3px;" class="glyphicon glyphicon-' + type + '"></i>' + item.text + '</a>',
                        value: item.text
                     };
                  };

               }));
            }
         });
      },
      minLength: 1,
      open: function () {
         setTimeout(function () {
            $('.ui-autocomplete').css('z-index', "1031");
         }, 0);
      }
   }).data("ui-autocomplete")._renderItem = function (ul, item) {
      return $("<li></li>")
         .data("item.autocomplete", item)
         .append(item.label)
         .appendTo(ul);
   };
});