Vue.component('wigget_form', {
    data: function () {

        return {
            raiio_data: [],
            data_select: '',
        }
    },
    delimiters: ["[[", "]]"],
    props: ['data_item'],
    correcto: '',
    template: `
    <ul>
        <div v-for="(item, index) in data_item">
            <div class="form-check" >
                <input class="form-check-input" v-model="data_select" type="radio" name="gridRadios">
                <label class="form-check-label" :for="index">[[item.text]]</label>
                <button type="button" class="btn btn-link btn-sm" v-on:click="delete_item(index)"><span class="oi oi-trash"></span></button>
            </div>
        </div>
    </ul>`,
    methods:{
        onChange(event) {
            console.log(event.target.value)
        },
        delete_item:function (index) {
            this.data_item.splice(index,1)
        }
    }

})



Vue.component('input_text_widget', {
    data: function () {
        return {
            text_valor: '',
        }
    },
    delimiters: ["[[", "]]"],

   
    watch: {
        text_valor: function (val) {
            this.$emit('return_text_valor', val)
          },
    },
    template: `
    <div class="row">
        <div class="col-sm-6">
            <input class="form-control form-control-lg" type="text" placeholder="">
        </div>
        <div class="col-sm-6">
            <input class="form-control form-control-lg" v-model="text_valor" type="text" placeholder="Escriba la respuesta correcta">
        </div>
    </div>`,

})


Vue.component('input_textarea_widget', {
    data: function () {
        return {
            text_area_valor: '',
        }
    },
    watch: {
        text_area_valor: function (val) {
            this.$emit('return_text_valor', val)
          },
    },
    delimiters: ["[[", "]]"],
    props: ['value_textarea'],
    template: `
    <div class="row">
        <div class="col-sm-6">
            <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
        </div>
        <div class="col-sm-6">
            <textarea class="form-control" id="exampleFormControlTextarea1" v-model="text_area_valor" rows="3" placeholder="Escriba la respuesta correcta"></textarea>
        </div>
    </div>`,

})