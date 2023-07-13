
//función que valida un formulario
 $(function(){
    $("#mi-formulario").validate({
        rules:{
            nom:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },
            pass:{
                required:true
            },
            fono:{
                required:true,
                number:true
            },
            fecha:{
                required:true
            },
           
        },//rules
        messages:{
            nom:{
                required:'Ingrese nombre del usuario',
                minlength:'Caracteres insuficientes (3)'
            },
            correo:{
                required:'Ingrese correo del usuario',
                email:'Formato incorrecto del correo'
            },
            pass:{
                required:'Ingrese una contraseña',
                minlength: 'Caracteres insuficientes(8)'
            },
            fono:{
                required:'Ingrese un teléfono válido',
                minlength: 'Cantidad de digitos insuficientes'
            },
            fecha:{
                required:'Seleccione una fecha válida',
                min:'Fecha no corresponde'
            },
           
        }//messages
    });
});

function Checkinfo(){
    alert("Esta sera la información asignada a su cuenta: \nNombre: "+document.getElementById("nom").value+"\nCorreo: "+document.getElementById("correo").value+"\nTeléfono: "+document.getElementById("fono").value+"\nFecha de nacimiento: "+document.getElementById("fecha").value);
}