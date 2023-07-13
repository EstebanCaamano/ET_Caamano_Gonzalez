$(function(){
    $("#formulario").validate({ 
        rules:{
            id:"required",
            nombre: "required",
            imagen: "required",
            precio: "required",
        },
        messages:{
            id:{
                required: 'Ingresar nueva id',
            },
            nombre:{
                required: 'Ingresar nuevo nombre',
            },
            imagen: {
                required: 'Ingresar nueva imagen',
            },
            precio:{
                required: 'Ingresar nuevo precio',
            }
        }
    })
});