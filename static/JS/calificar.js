var app = new Vue({
    el: '#app',
    data: {
        aula: '0',
        materia_selected: '0',
        unidad_selected: '0',

        materia: {},
        unidades: {},
        calificaciones: {},
        disable_button: true,
        disable_buttonPDF: true

    },
    delimiters: ["[[", "]]"],

    methods: {
        onChange() {
            this.disable_button = true;
            this.disable_buttonPDF = true;
            axios
                .get('/maestro/get/materias/?aula=' + this.aula)
                .then(response => (
                    this.materia = response.data.materia,
                    this.unidades = {},
                    this.calificaciones = {}
                ))
        },
        onChangueMateria() {
            this.disable_button = true;
            this.disable_buttonPDF = true;
            axios
                .get('/maestro/get/materias/?materia=' + this.materia_selected)
                .then(response => (
                    this.unidades = response.data.unidades,
                    this.calificaciones = {}
                ))
        },
        onChangueUnidad() {
            this.disable_button = false;
            this.disable_buttonPDF = true;
            this.calificaciones = {};
        },

        PromediarUnidad() {
            axios
                .get('/maestro/promd/unidad/?aula=' + this.aula + '&materia=' + this.materia_selected + '&unidad=' + this.unidad_selected)
                .then(response => (
                    this.calificaciones = response.data.calificaciones,
                    this.disable_buttonPDF = false
                ))
        },

        DowloadPDF(){
            var pdf = new jsPDF();
            pdf.autoTable({html: '#unidad-table'});       
            var unidad=this.unidades.find(unidad => unidad.unidad_id==this.unidad_selected);
            var materia=this.materia.find(materia => materia.materia_id==this.materia_selected);     
            pdf.text("Calificacion de unidad", 20, 10);
            pdf.save(materia.materia_nombre+'-'+unidad.unidad_nombre+'.pdf');
        }



    },
    computed: {
        isDisabled: function () {
            return !this.terms;
        }

    }

})