
  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyC2Xk8j_uw6cGfUifzFGgLgc8RaeG6ufgw",
    authDomain: "nurseclass-41523.firebaseapp.com",
    databaseURL: "https://nurseclass-41523.firebaseio.com",
    projectId: "nurseclass-41523",
    storageBucket: "nurseclass-41523.appspot.com",
    messagingSenderId: "1033901766145",
    appId: "1:1033901766145:web:529fdc6cef7f67b1"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  var db = firebase.firestore();
  
  

  $('#chat_container').hide();
  $('#icons_chat').show();

function cerrar_ventana() {
    $('#chat_container').hide("linear");
    $('#icons_chat').show("linear");
}
function open_chat() {
    $('#icons_chat').hide("swing");
    $('#chat_container').show("swing");

    var div = document.getElementById('box-body');
        div.scrollTop = '9999';
}



function enviar_msn() {
    var options = {year: "numeric", month: "long", day: "numeric"};
    var fecha = new Date()
    var fechaLocal = new Date()
    fecha=fecha.toLocaleDateString("es-mx", options)

    db.collection("chat").add({
        usuario: user,
        nombre: user_name_full,
        avatar: user_foto,
        mensaje: $('#message').val(),
        creado:fecha,
        creado_local:fechaLocal
    })
    .then(function(docRef) {
        console.log("Document written with ID: ", docRef.id);
        $('#message').val('');
    })
    .catch(function(error) {
        console.error("Error adding document: ", error);
    });
}


db.collection("chat").orderBy('creado_local')
    .onSnapshot(function(querySnapshot) {
        contenido="";

        querySnapshot.forEach(function(doc) {

          if (doc.data().usuario == user) {
            contenido += `
             
            <!-- Message to the right -->
            <div class="direct-chat-msg right">
              <div class="direct-chat-info clearfix">
                <span class="direct-chat-name pull-right">${doc.data().nombre}</span>
                <span class="direct-chat-timestamp pull-left">${doc.data().creado}</span>
              </div>
              <!-- /.direct-chat-info -->
              <img class="direct-chat-img" src="${doc.data().avatar}" alt="Message User Image"><!-- /.direct-chat-img -->
              <div class="direct-chat-text">
                ${doc.data().mensaje}
              </div>
              <!-- /.direct-chat-text -->
            </div>
            <!-- /.direct-chat-msg -->
          
            `;
            
          }else{

            contenido += `

            <div class="direct-chat-msg">
              <div class="direct-chat-info clearfix">
                <span class="direct-chat-name pull-left">${doc.data().nombre}</span>
                <span class="direct-chat-timestamp pull-right">${doc.data().creado}</span>
              </div>
              <!-- /.direct-chat-info -->
              <img class="direct-chat-img" src="${doc.data().avatar}" alt="Message User Image"><!-- /.direct-chat-img -->
              <div class="direct-chat-text">
              ${doc.data().mensaje}
              </div>
              <!-- /.direct-chat-text -->
            </div>
          
            `;

          }
            

            
        });

        $('#box-body').html(contenido)
        var div = document.getElementById('box-body');
        div.scrollTop = '9999';
        
    });


    