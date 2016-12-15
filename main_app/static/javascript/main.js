$(document).ready(function() {
	
	$(":file").filestyle({input: false});

	$(".enter-btn#2").click(function() {
		$(".register").css({
			display: 'block',
		});
		$(".enter-btns").css({
			display: 'none',
		});
	});

	$("#delete-btn").click(function() {
		alert("Attention, you are about to delete a Strain. You wont be able to recover it after this.");
	});
});