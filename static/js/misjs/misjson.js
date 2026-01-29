"use strict";

var url = window.location;
var baseUrl = url.protocol + "//" + url.host + "/" + url.pathname.split('/')[1]+ "/" ;//+ url.pathname.split('/')[2];
//var baseUrl = url.protocol + "//" + url.host  ;// + "/" + url.pathname.split('/')[1]+ "/" + url.pathname.split('/')[2];

$(document).ready(function () {
    $('#tablaCursos').DataTable({
        paging: true,
        pageLength: 5 ,
        searching: true,
        ordering: true,

        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                text: '📥 Excel',
                title: 'Listado de Cursos'
            },
            {
                extend: 'print',
                text: '🖨 Imprimir'
            }
        ],

        language: {
            url: 'https://cdn.datatables.net/plug-ins/1.13.8/i18n/es-ES.json'
        }
    });
});
