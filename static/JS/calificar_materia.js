 function dowLoadPDF() {
    var pdf = new jsPDF();
    pdf.autoTable({html: '#tabla_materia'});
    var materia=$('#materia_h3').text();
    pdf.text("Calificación de Materia: "+materia, 20, 10);
    pdf.save(materia+'.pdf');
 }