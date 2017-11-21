/*********function that generate a random id ***********************/
function generateRandomId() {
	var id = '';
	var charSet='ABCDEFJHIJKLMNOPQRSTUVWXYZ0123456789';
	for (var i = 1; i <= 6; i++) {
	var randPos = Math.floor(Math.random() * charSet.length);
	id += charSet[randPos];
	}
	return id;
};
/*********************************************************/
		
$('document').ready(function(){
	//initialise the module toastr
	toastr.options = {
	"closeButton": true,
	"debug": false,
	"newestOnTop": false,
	"progressBar": false,
	"positionClass": "toast-bottom-center",
	"preventDuplicates": true,
	"onclick": null,
	"showDuration": "500",
	"hideDuration": "1000",
	"timeOut": "2000",
	"extendedTimeOut": "1000",
	"showEasing": "swing",
	"hideEasing": "linear",
	"showMethod": "fadeIn",
	"hideMethod": "fadeOut"
	};

	// generate a random() value for the field identifiant
	$('#id_identifiant').val(generateRandomId);
	$.ajax({
		url:'/qrcode/',
		dataType:'json',
		data:{
			'trigger': $('#id_identifiant').val(),
			},
		success: function(){
			$('.qrcode').attr('src', '/static/img/'+$('#id_identifiant').val()+'.jpeg')
		},

		})

	$("input[name='visa']").on('change',function(){
		val= $("input[name='visa']:checked").val()
		if (val == 'non'){
			$('.hidde').fadeOut('slow');
			
		}
		else{
			$('.hidde').fadeIn('slow');
		}
	})

	$("input[type='text']").change(function(){
		id=$(this).attr('id')
		val=$(this).val();
		//AJAX request to check if field are filled up correctly
		$.ajax({
			url: '/checkinput/',
			dataType: 'json',
			data: {
				'trigger': id,
				'value': val,

			},
			success: function(bundle){
				if (bundle.is_ok){
					$('#'+id).parent().removeClass('has-error')
					$('#'+id).parent().addClass('has-success')
					toastr.success(bundle.message)
				}
				else{
					$('#'+id).parent().removeClass('has-success')
					$('#'+id).parent().addClass('has-error')
					toastr.error(bundle.message)
				}
			}
		})
	})
})