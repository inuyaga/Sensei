var app = new Vue({
    el: '#app',
    data: {
        // variables de opciones multiples
        radio_selec:'',
        // ----------------------------------
        visivilidad: false,
        v_opcion: '',
        question_text: null,
        
        
        visible_radio: false,
        visible_text: false,
        visible_textarea: false,
        value_text_verdadero: '',
        value_textarea_verdadero: '',
        
        items: [
        ]
    },
    methods: {
        onChange(event) {
            this.tipo_iput=event.target.value;        

            switch (event.target.value) {
                
                case 'text':
                    this.visivilidad = false
                    this.visible_radio = false
                    this.visible_text = true
                    this.visible_textarea = false
                
                    break;
                case 'textarea':
                    
                    this.visivilidad = false
                    this.visible_radio = false
                    this.visible_text = false
                    this.visible_textarea = true
                    
                    break;
                case 'radio':
                    this.visivilidad = true
                    this.visible_radio = true
                    this.visible_text = false
                    this.visible_textarea = false
                    
                    break;
                
                default:
                    
                    this.visivilidad = false
                    this.visible_radio = false
                    this.visible_text = false
                    this.visible_textarea = false
                    
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
            var valor_post=""
            if (this.tipo_iput == "text") {
                valor_post = this.value_text_verdadero
                console.log(valor_post)
            }else if (this.tipo_iput == "textarea") {
                valor_post = this.value_textarea_verdadero
                
            } else {
                valor_post = ""
            }
            axios.post('', {
                tipo_iput: this.tipo_iput,
                items: this.items,
                question_text: this.question_text,
                el_value: valor_post,
              })
              .then(function (response) {
                location.reload();
              })
              .catch(function (error) {
                swal("Mal!", error.response.data.IntegrityError, "error");
              });
        }
    },
    delimiters: ["[[", "]]"]
})