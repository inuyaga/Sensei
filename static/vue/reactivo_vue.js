Vue.component('wigget_form', {
    data: function () {

        return {
            raiio_data: []
        }
    },
    delimiters: ["[[", "]]"],
    props: ['data_item'],
    correcto: '',
    template: `
    <ul>
        <div v-for="(item, index) in data_item">
            <div class="form-check" >
                <input style="display: inline-block;" class="form-check-input" v-model="index" type="radio" name="gridRadios" :id="index" :value="index">
                <label style="display: inline-block;" class="form-check-label" :for="index">[[item.text]]</label>
                <button style="display: inline-block;" type="button" class="btn btn-link btn-sm" v-on:click="delete_item(index)"><span class="oi oi-trash"></span></button>
                
            </div>
        </div>
    </ul>`,
    methods:{
        delete_item:function (index) {
            this.data_item.splice(index,1)
        }
    }

})
Vue.component('wigget_select', {
    data: function () {

        return {
            raiio_data: []
        }
    },
    delimiters: ["[[", "]]"],
    props: ['data_item'],
    template: `
            <div class="form-group">
                <label for="exampleFormControlSelect1">Selecciones</label><a href="#" class="text-dange"><span class="oi oi-trash"></span></a>
                <select class="form-control" id="exampleFormControlSelect1">
                <option  v-for="(item, index) in data_item" :value="index">[[item.text]]</option>
                </select>
            </div>`,
})

Vue.component('wigget_check', {
    data: function () {

        return {
            raiio_data: []
        }
    },
    delimiters: ["[[", "]]"],
    props: ['data_item'],
    template: `
            <div class="form-group">
                <div class="form-group form-check" v-for="(item, index) in data_item">
                    <input type="checkbox" class="form-check-input" id="exampleCheck1" :value="index">
                    <label class="form-check-label" for="exampleCheck1">[[item.text]]</label>
                    <a href="#" class="text-dange"><span class="oi oi-trash"></span></a>
                </div>
            </div>`,

})
var app = new Vue({
    el: '#app',
    data: {
        visivilidad: false,
        v_opcion: '',
        question_text: null,
        tipo_widget: null,
        tipo_iput: null,
        visible_radio: false,
        visible_select: false,
        visible_check: false,
        preguntas:[],
        tipo_reactivo:[],
        items: [
        ]
    },
    methods: {
        onChange(event) {
            this.tipo_iput = event.target.value

            switch (event.target.value) {
                case 'text':
                    this.tipo_widget = '<input class="form-control form-control-lg" type="text" placeholder="">'
                    this.visivilidad = false
                    this.visible_radio = false
                    this.visible_check = false
                    this.visible_select = false
                    break;
                case 'textarea':
                    this.tipo_widget = '<textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>'
                    this.visivilidad = false
                    this.visible_radio = false
                    this.visible_check = false
                    this.visible_select = false
                    break;
                case 'radio':
                    this.tipo_widget = ''
                    this.visivilidad = true
                    this.visible_radio = true
                    this.visible_check = false
                    this.visible_select = false
                    break;
                case 'checkbox':
                    this.tipo_widget = ''
                    this.visivilidad = true
                    this.visible_check = true
                    this.visible_radio = false
                    this.visible_select = false
                    break;
                case 'option':
                    this.tipo_widget = ''
                    this.visivilidad = true
                    this.visible_select = true
                    this.visible_radio = false
                    this.visible_check = false
                    break;
                default:
                    this.tipo_widget = ''
                    this.visivilidad = false
                    this.visible_radio = false
                    this.visible_check = false
                    this.visible_select = false
                    break;
            }
        },
        add_items_data: function (event) {
            if (this.v_opcion != '') {
                this.items.push({ text: this.v_opcion });
                this.v_opcion = null
            }
        },

        post_item:function (){
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
            axios.post('', {
                tipo_iput: this.tipo_iput,
                items: this.items,
                question_text: this.question_text,
              })
              .then(function (response) {
                app.preguntas=response.data.preguntas
              })
              .catch(function (error) {
                // preg = error.response.data.preguntas
                // this.preguntas.push(preg);
                // swal("Mal!", error.response.data.IntegrityError, "success");
              });
        }
    },
    delimiters: ["[[", "]]"]
})