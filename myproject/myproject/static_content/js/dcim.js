        $(document).ready( function() {





           $(document).on('change', '.btn-file :file', function() {
              var input = $(this),
              label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
              input.trigger('fileselect', [label]);
          });




           $('.btn-file :file').on('fileselect', function(event, label) {

              var input = $(this).parents('.input-group').find(':text'),
              log = label;

              if( input.length ) {
                  input.val(log);
              } else {
                  if( log ) alert(log);
              }

          });


          $('#use_zoom').change(function() {
                if ($('#use_zoom').is(':checked')) {

                    wheelzoom(document.querySelector("#img_upload"), {zoom: 0.1, maxZoom: 10});
                }else{
                    document.querySelector('#img_upload').dispatchEvent(new CustomEvent('wheelzoom.destroy'));
                }});

           function cleantables()
           {
              $('#file_data').children('tr').remove();
              $('#med_data').children('tr').remove();

          }


          function processdata(d){

            var json = JSON.parse(d)


            for (key in json.generic){
                $('#file_data').append('<tr><td>'+key+'</td><td>'+json.generic[key]+'</td></tr>')
            }

            for (key in json.med){
                $('#med_data').append('<tr><td>'+key+'</td><td>'+json.med[key]+'</td></tr>')
            }

            if (json.url!=null){

                $('#img_upload').attr('src', json.url['base64']);
            }else
            {
             $('#img_upload').attr('src', '/static/img/dot.gif');
             $('#modal_dialog').modal('toggle');

            }
        }

        $("#imgInp").change(function(){
          cleantables()

          var formData = new FormData(document.getElementById("form_one"));

          var xhr = new XMLHttpRequest();
          xhr.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                processdata(this.responseText);
            }
        };

        xhr.open('POST', 'process.ajax', true);
        xhr.send(formData);

    });
    });
