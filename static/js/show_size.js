$('#dog_breed').on('change',function(){
    if( $(this).val().toLowerCase()==="beagle" || 
    $(this).val().toLowerCase()==="bull terrier" || 
    $(this).val().toLowerCase()==="dobermann" || 
    $(this).val().toLowerCase()==="poodle" || 
    $(this).val().toLowerCase()==="schnauzer" || 
    $(this).val().toLowerCase()==="srd" ||
    $(this).val().toLowerCase()==="vira-lata" ||
    $(this).val().toLowerCase()==="vira lata")
    {
    $("#dog_size").show()
    }
    else
    {
    $("#dog_size").hide()
    }
});