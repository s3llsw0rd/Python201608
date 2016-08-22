var response = {};

$(document).ready(function(){

	$('form').submit(function(){
		$('#directions').html('');
		$.post($(this).attr('action'), $(this).serialize(), function(res){
			var html_string = '<ol>';
			if (res.routes.length == 0){
				html_string = '<h3>Locations not found.</h3>'
			} else {
				for (var i = 0; i < res.routes[0].legs.length; i++){
					for (var j = 0; j < res.routes[0].legs[i].steps.length; j++){
						html_string += '<li>' + res.routes[0].legs[i].steps[j].html_instructions + '</li>';
					}
				}
			}
			html_string += '</ol>';
			$('#directions').html(function(){
				return html_string;
			})
		}, 'json');
		return false;
	});
})
