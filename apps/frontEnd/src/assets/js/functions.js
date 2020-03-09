$(document).ready(function(){
    $("#regForm").hide();
})

function sldTogg(control){
    getControl = document.getElementById(control);
    $(getControl).slideToggle("slow");
}

function deleteMessage()
{
    // If answer is Cancelar or False this code cancel the link
    if(!confirm("Are you sure to delete this message?"))
        event.preventDefault()
}

function validateForm()
{
    validation = true
    if(document.getElementById('firstName').value.length < 3){
        validation = false
        document.getElementById("firstNameError").innerHTML = "The first name must be greater than 3 characters."
    }
    else{
        document.getElementById("fnameError").style="display:none";
    }

    if(document.getElementById('email').value.length < 10){
        validation = false
        document.getElementById("emailError").innerHTML = "The email is required."
    }
    else
        document.getElementById("emailError").style="display:none";
}

function backColor(){
    var control = document.getElementById("navBar");
    control.classList.add("dark");
}