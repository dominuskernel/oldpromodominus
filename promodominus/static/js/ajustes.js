var j;
j= $(document);
j.ready(function(){
    /**carousel para las imagenes de las entradas**/
    j = $(".carousel");
    j.carousel({
        interval: 3000
    });
    /**Ajustes de ancho para los iframes del POST para responsive de movil y tablet**/
    p = $(".textoentradamobile iframe");
    p.css({width:"300px", height:"300px"});
    
    /**bocadillos en los elementos del footer**/

    b = $("#datospie");
    b.mouseover(function(){
		$("#datospie").popover('show');
	});
	b.mouseout(function(){
		$("#datospie").popover('hide');
	});
	
	b = $("#proppie");
    b.mouseover(function(){
		$("#proppie").popover('show');
	});
	b.mouseout(function(){
		$("#proppie").popover('hide');
	});
	b = $("#avisopie");
    b.mouseover(function(){
		$("#avisopie").popover('show');
	});
	b.mouseout(function(){
		$("#avisopie").popover('hide');
	});
	b = $("#linkpie");
    b.mouseover(function(){
		$("#linkpie").popover('show');
	});
	b.mouseout(function(){
		$("#linkpie").popover('hide');
	});
	b = $("#emailpie");
    b.mouseover(function(){
		$("#emailpie").popover('show');
	});
	b.mouseout(function(){
		$("#emailpie").popover('hide');
	});
    
    var options = {
        clearForm: true,
        success: function(){
            location.reload();
        }
    };
    
    $('#formcom').ajaxForm(options);
    
    $(".fancybox").fancybox({
    	openEffect	: 'elastic',
    	closeEffect	: 'elastic',

    	helpers : {
    		title : {
    			type : 'inside'
    		}
    	}
    });    
});

