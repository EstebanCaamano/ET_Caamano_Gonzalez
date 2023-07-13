$(function(){
    $("#formulario").validate({ 
        rules:{
            id:"required",
            nombre: "required",
            imagen: "required",
            precio: "required",
            categoria: "required",
            
        },
        messages:{
            id:{
                required: 'Ingresar ID del Producto',
            },
            nombre:{
                required: 'Ingresar nombre del producto',
            },
            imagen: {
                required: 'Ingresar Imagen del Producto',
            },
            precio:{
                required: 'Ingresar Precio del Producto',
            },
            categoria:{
                required: 'Seleccione una categoria',
            },
        }
    })
});