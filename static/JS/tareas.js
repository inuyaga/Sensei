var ID_TAREA
    $('#id_materia').on('change', function () {
        // $("#id_unidad_materia").val(this.value);
        $("#btn_nuevo").attr("disabled", true);
        $('#contenido_tabla').html('');

        $.ajax({
            type: "POST",
            url: "{% url 'control_escolar:maestro_tarea_json' %}",
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                id_materia: this.value,
                tipo_post: 'materia',
            },
            success: function (data) {
                var contenido = data.content.contenido
                var tipo_mensaje = data.content.tipo_mensaje 
                if (tipo_mensaje == 'materia') {
                    $('#id_unidad').html(contenido)

                } else {
                    //   alertify.error(message);
                }
            },
            error: function (data) {
                console.log('An error occurred.');

                console.log(data);
            },
        });
    });

    $('#id_unidad').on('change', function () {
        // $("#id_unidad_materia").val(this.value);
        $("#btn_nuevo").attr("disabled", false);
        $("#id_tarea_unidad").val(this.value);

        $.post("{% url 'control_escolar:maestro_tarea_json' %}", {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                UnidadID: this.value,
                tipo_post: 'tareas',
            },
            function (data, status) {
                var message = data.content.contenido;
                $('#contenido_tabla').html(message);
            });
    });




    var frm = $('#form_tarea');

    frm.submit(function (e) {

        e.preventDefault();

        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                var message = data.content.cont
                alertify.success('Listo');
                $('#contenido_tabla').html(message)
                $('#id_tarea_nombre').val('')
                $('#id_tarea_descripcion').val('')
                $('#id_tarea_fecha_inicio').val('')
                $('#id_tarea_fecha_termino').val('')
                $('#id_tarea_tipo').val('')
            },
            error: function (data) {
                console.log('An error occurred.');
                console.log(data);
                alertify.error('Un error al intentar guardar');
            },
        });
    });


function get_update_tarea(id_tarea) {
 
    $.ajax({
        url: '/maestro/Tarea/update/'+id_tarea+'/',
        type: 'GET',
        success: function (data) {
            // alertify.alert('Alert Title', data);
            console.log(data)
            var valor=data[0]
            $.each(valor, function(i, item) {
                $('#id_'+i).val(item)
                            
            });
            $('#btn_nuevo').click();
            ID_TAREA=id_tarea;
        }
    });

}

function ActualizarTarea() {
    $.ajax({
            type: 'POST',
            url: '/maestro/Tarea/updateCamio/'+ID_TAREA+'/'+$('#id_unidad').val()+'/',
            data: $('#form_tarea').serialize(),
            success: function (data) {
                alertify.success('Listo');
                $('#id_tarea_nombre').val('')
                $('#id_tarea_descripcion').val('')
                $('#id_tarea_fecha_inicio').val('')
                $('#id_tarea_fecha_termino').val('')
                $('#id_tarea_tipo').val('')
                var filas;
                $('#contenido_tabla').html('')
                $.each(data.Tareas, function(i, item) {
                filas='<tr>'+
                        '<th scope="row">'+item.tarea_nombre+'</th>'+
                        '<td>'+item.tarea_descripcion+'</td>'+
                        '<td>'+item.tarea_fecha_inicio+'</td>'+
                        '<td>'+item.tarea_fecha_termino+'</td>'+
                        '<td>'+item.tarea_tipo+'</td>'+
                        '<td>'+
                            '<a class="btn btn-info" onclick="get_update_tarea('+item.tarea_id+')" role="button"><span class="fas fa-pen-square"></span></a>'+
                            ''+
                        '</td>'+
                      '</tr>';                  
                $('#contenido_tabla').append(filas)
                });

                console.log(data);
            },
            error: function (data) {
                console.log('An error occurred.');
                console.log(data);
                alertify.error('Un error al intentar guardar');
            },
        });
    
}