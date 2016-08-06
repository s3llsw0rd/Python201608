$(document).ready(function(){
	$("form").submit(function(){
		$("#users").append("<tr>" +
								"<td>" + $("#fname").val() + "</td>" +
								"<td>" + $("#lname").val() + "</td>" +
								"<td>" + $("#email").val() + "</td>"+
								"<td>" + $("#contact").val() + "</td>"+
							"</tr>")
				$(".info").val("");
		return false;
	});

});	
