$(document).ready(function() {
	$('.file-upload label').on('click', function(event) {
		event.preventDefault();
		/* Act on the event */
		$(this).parents('.file-upload').find('.form-control-file').trigger('click');
	});
	$('.form-control-file').on('change', function(event) {
		event.preventDefault();
		/* Act on the event */
		var fileName = event.target.files[0].name;
		$('.file-upload label').text(fileName);
	});
});