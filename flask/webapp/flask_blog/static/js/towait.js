$(document).ready(function() {

	$('#xxx').click(function xxx() {
		$.ajax({
			data : {
				name : "from js"
			},
			type : 'POST',
			url : '/process_grid'
		})
		.done(function(data) {
			if (data.error) {
				//$('#errorAlert').text(data.error).show();
				//$('#successAlert').hide();
			}
			else {
				var html = data.data;
				//$('#successAlert').text(data.name).show();
				//$('#errorAlert').hide();
				document.getElementById("parentElement").innerHTML = html;
			}
		});
		event.preventDefault();
	});

});