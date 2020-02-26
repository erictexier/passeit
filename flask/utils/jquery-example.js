



<script type=text/javascript>
    $(function() {
        $('a#fillit_nb_tetrino_id').bind('click', function() {
            $.getJSON('/background_process', {
                nb_element: $('input[name="nb_element"]').val(),
            }, function(data) {
                $("#result").text(data.result);
            });
        return false;
        });
    });
</script>
