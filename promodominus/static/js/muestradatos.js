var j;
j = $(document);
j.ready(function(){
    j = $("#todo");
    j.click(function(){
        v = $(".Viajes");
        v.show("slow");
        p = $(".Libros");
        p.show("slow");
        c = $(".Cursos");
        c.show("slow")
        a = $(".Aplicaciones");
        a.show("slow");
        s = $(".Empresas");
        s.show("slow");
        e = $(".Eventos");
        e.show("slow");
        h = $("#buscahoteles");
        h.hide("slow");
        m = $(".Multimedia")
        m.show("slow");
        });
    j = $("#aplicaciones");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Aplicaciones"){
            j = $(".Aplicaciones");
            j.show("slow");
        }
        else{
            v = $(".Viajes");
            v.hide("slow");
            p = $(".Libros");
            p.hide("slow");
            c = $(".Cursos");
            c.hide("slow")
            a = $(".Aplicaciones");
            a.show("slow");
            s = $(".Empresas");
            s.hide("slow");
            e = $(".Eventos");
            e.hide("slow");
            h = $("#buscahoteles");
            h.hide("slow");
            m = $(".Multimedia")
			m.hide("slow");
        }
    });
    j = $("#viajes");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Viajes"){
            j = $(".Viajes");
            j.show("slow");
            h = $("#buscahoteles");
            h.show("slow");
        }
        else{
            a = $(".Aplicaciones");
            a.hide("slow");
            p = $(".Libros");
            p.hide("slow");
            c = $(".Cursos");
            c.hide("slow");
            v = $(".Viajes");
            v.show("slow");
            s = $(".Empresas");
            s.hide("slow");
            e = $(".Eventos");
            e.hide("slow");
            h = $("#buscahoteles");
            h.show("slow");
            m = $(".Multimedia")
			m.hide("slow");
        }
    });
    
    j = $("#libros");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Productos"){
            j = $(".Libros");
            j.show("slow");
        }
        else{
            v = $(".Viajes");
            v.hide("slow");
            a = $(".Aplicaciones");
            a.hide("slow");
            c = $(".Cursos");
            c.hide("slow");
            p = $(".Libros");
            p.show("slow");
            s = $(".Empresas");
            s.hide("slow");
            e = $(".Eventos");
            e.hide("slow");
            h = $("#buscahoteles");
            h.hide("slow");
        }
    });
    j = $("#cursos");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Cursos"){
            j = $(".Cursos");
            j.show("slow");
        }
        else{
            v = $(".Viajes");
            v.hide("slow");
            p = $(".Productos");
            p.hide("slow");
            a = $(".Aplicaciones");
            a.hide("slow");
            c = $(".Cursos");
            c.show("slow");
            s = $(".Empresas");
            s.hide("slow");
            e = $(".Eventos");
            e.hide("slow");
            h = $("#buscahoteles");
            h.hide("slow");
            m = $(".Multimedia")
			m.hide("slow");
        }
    });    
    j = $("#empresas");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Empresas"){
            j = $(".Empresas");
            j.show("slow");
        }
        else{
            v = $(".Viajes");
            v.hide("slow");
            p = $(".Libros");
            p.hide("slow");
            a = $(".Aplicaciones");
            a.hide("slow");
            c = $(".Cursos");
            c.hide("slow");
            s = $(".Empresas");
            s.show("slow");
            e = $(".Eventos");
            e.hide("slow");
            h = $("#buscahoteles");
            h.hide("slow");
            m = $(".Multimedia")
			m.hide("slow");
        }
    });    
    j = $("#eventos");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Eventos"){
            j = $(".Eventos");
            j.show("slow");
        }
        else{
            v = $(".Viajes");
            v.hide("slow");
            p = $(".Libros");
            p.hide("slow");
            a = $(".Aplicaciones");
            a.hide("slow");
            c = $(".Cursos");
            c.hide("slow");
            s = $(".Empresas");
            s.hide("slow");
            e = $(".Eventos");
            e.show("slow");
            h = $("#buscahoteles");
            h.hide("slow"); 
            m = $(".Multimedia")
			m.hide("slow");
            
        }
    });  
    j = $("#multimedia");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Eventos"){
            j = $(".Multimedia");
            j.show("slow");
        }
        else{
            v = $(".Viajes");
            v.hide("slow");
            p = $(".Libros");
            p.hide("slow");
            a = $(".Aplicaciones");
            a.hide("slow");
            c = $(".Cursos");
            c.hide("slow");
            s = $(".Empresas");
            s.hide("slow");
            e = $(".Eventos");
            e.hide("slow");
            h = $("#buscahoteles");
            h.hide("slow"); 
            m = $(".Multimedia")
			m.show("slow");
            
        }
    });  
    
    
    /**botones de mostrar categoria para moviles y tablets**/  
   j = $("#todo-mobile");
    j.click(function(){
        v = $(".Viajes");
        v.show("slow");
        p = $(".Libros");
        p.show("slow");
        c = $(".Cursos");
        c.show("slow")
        a = $(".Aplicaciones");
        a.show("slow");
        s = $(".Empresas");
        s.show("slow");
        e = $(".Eventos");
        e.show("slow");
        h = $("#buscahoteles");
        h.hide("slow");
        m = $(".Multimedia")
        m.hide("slow");
        });
    j = $("#aplicaciones-mobile");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Aplicaciones"){
            j = $(".Aplicaciones");
            j.show("slow");
        }
        else{
            v = $(".Viajes");
            v.hide("slow");
            p = $(".Libros");
            p.hide("slow");
            c = $(".Cursos");
            c.hide("slow")
            a = $(".Aplicaciones");
            a.show("slow");
            s = $(".Empresas");
            s.hide("slow");
            e = $(".Eventos");
            e.hide("slow");
            h = $("#buscahoteles");
            h.hide("slow");
            m = $(".Multimedia")
			m.hide("slow");
        }
    });
    j = $("#viajes-mobile");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Viajes"){
            j = $(".Viajes");
            j.show("slow");
            h = $("#buscahoteles");
            h.show("slow");
        }
        else{
            a = $(".Aplicaciones");
            a.hide("slow");
            p = $(".Libros");
            p.hide("slow");
            c = $(".Cursos");
            c.hide("slow");
            v = $(".Viajes");
            v.show("slow");
            s = $(".Empresas");
            s.hide("slow");
            e = $(".Eventos");
            e.hide("slow");
            h = $("#buscahoteles");
            h.show("slow");
            m = $(".Multimedia")
			m.hide("slow");
        }
    });
    
    j = $("#libros-mobile");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Productos"){
            j = $(".Libros");
            j.show("slow");
        }
        else{
            v = $(".Viajes");
            v.hide("slow");
            a = $(".Aplicaciones");
            a.hide("slow");
            c = $(".Cursos");
            c.hide("slow");
            p = $(".Libros");
            p.show("slow");
            s = $(".Empresas");
            s.hide("slow");
            e = $(".Eventos");
            e.hide("slow");
            h = $("#buscahoteles");
            h.hide("slow");
        }
    });
    j = $("#cursos-mobile");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Cursos"){
            j = $(".Cursos");
            j.show("slow");
        }
        else{
            v = $(".Viajes");
            v.hide("slow");
            p = $(".Productos");
            p.hide("slow");
            a = $(".Aplicaciones");
            a.hide("slow");
            c = $(".Cursos");
            c.show("slow");
            s = $(".Empresas");
            s.hide("slow");
            e = $(".Eventos");
            e.hide("slow");
            h = $("#buscahoteles");
            h.hide("slow");
            m = $(".Multimedia")
			m.hide("slow");
        }
    });    
    j = $("#empresas-mobile");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Empresas"){
            j = $(".Empresas");
            j.show("slow");
        }
        else{
            v = $(".Viajes");
            v.hide("slow");
            p = $(".Libros");
            p.hide("slow");
            a = $(".Aplicaciones");
            a.hide("slow");
            c = $(".Cursos");
            c.hide("slow");
            s = $(".Empresas");
            s.show("slow");
            e = $(".Eventos");
            e.hide("slow");
            h = $("#buscahoteles");
            h.hide("slow");
            m = $(".Multimedia")
			m.hide("slow");
        }
    });    
    j = $("#eventos-mobile");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Eventos"){
            j = $(".Eventos");
            j.show("slow");
        }
        else{
            v = $(".Viajes");
            v.hide("slow");
            p = $(".Libros");
            p.hide("slow");
            a = $(".Aplicaciones");
            a.hide("slow");
            c = $(".Cursos");
            c.hide("slow");
            s = $(".Empresas");
            s.hide("slow");
            e = $(".Eventos");
            e.show("slow");
            h = $("#buscahoteles");
            h.hide("slow"); 
            m = $(".Multimedia")
			m.hide("slow");
            
        }
    });  
    j = $("#multimedia-mobile");
    j.click(function(){
        j= $(".categoria");
        if(j.text() == "Eventos"){
            j = $(".Multimedia");
            j.show("slow");
        }
        else{
            v = $(".Viajes");
            v.hide("slow");
            p = $(".Libros");
            p.hide("slow");
            a = $(".Aplicaciones");
            a.hide("slow");
            c = $(".Cursos");
            c.hide("slow");
            s = $(".Empresas");
            s.hide("slow");
            e = $(".Eventos");
            e.hide("slow");
            h = $("#buscahoteles");
            h.hide("slow"); 
            m = $(".Multimedia")
			m.show("slow");
            
        }
    });  
})




    
