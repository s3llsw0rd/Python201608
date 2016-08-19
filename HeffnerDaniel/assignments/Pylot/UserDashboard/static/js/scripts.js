$(document).ready(function(){

	$('.remove').on('click', function(){
		url = $(this).attr('url');
		alertify.confirm('Are you sure you want to delete this user?', function(e){
			if (e) {
				window.location.href = url;
			} else {
				return false;
			}
		});

	});

})