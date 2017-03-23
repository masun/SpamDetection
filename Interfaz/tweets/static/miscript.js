jQuery(document).ready(function() {

	//var miniloader="<div class='miniloader'></div>";

	// Tweets table

	var idiomaEspañol={
		"sProcessing":     "Procesando...",
		"sLengthMenu":     "Mostrar _MENU_ registros",
		"sZeroRecords":    "No se encontraron resultados",
		"sEmptyTable":     "Ningún dato disponible en esta tabla",
		"sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
		"sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
		"sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
		"sInfoPostFix":    "",
		"sSearch":         "Buscar:",
		"sUrl":            "",
		"sInfoThousands":  ",",
		"sLoadingRecords": "Cargando...",
		"oPaginate": {
			"sFirst":    "Primero",
			"sLast":     "Último",
			"sNext":     "Siguiente",
			"sPrevious": "Anterior"
		},
		"oAria": {
		"sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
		"sSortDescending": ": Activar para ordenar la columna de manera descendente"
		}
	};

	$('#tweets-table').DataTable({
		"language": idiomaEspañol,
		"columnDefs": [ {
		"targets"  : 'no-sort',
		"orderable": false,
		}]
	});

  	// Load Tweets for account

  	var loadTweetsForAccount=function(twitterAccount){
  		$.post("get_tweets_for_account/",{account: twitterAccount}).done(function(data) {
	  		loadTweetsInTable(JSON.parse(data));
		});
  	}

  	var loadTweetsInTable=function(tweets){
  		var table = $('#tweets-table').DataTable();

 		for(var i in tweets){
			console.log(tweets[i])
 			var color="#26A65B";
			var rowNode = table
			    .row.add([tweets[i]["text"], tweets[i]["probabilidad"]])
			    .draw()
			    .node();
			console.log(tweets[i]);
			if (tweets[i]["spam"]){
				color="#EC644B";
			}

			$(rowNode).css({'background-color': color,color: 'white'}).animate({color: 'blue'});
		}

		$('#submit-account').prop('disabled', false);
	};

  	$("#form-twitter-account").submit(function(event) {
	  	event.preventDefault();
	  	var twitterAccount=$("#twitter-account").val();
	  	if (twitterAccount){

	  		//$('#submit-account').prop('disabled', true);

	  		// Clean table
	  		var table = $('#tweets-table').DataTable();
  			table.clear().draw();

	  		loadTweetsForAccount(twitterAccount);
	  	}
	});

});
