function validateForm()
{
 let name = document.getElementBytd("name").value;
 let email = document.getElementBytd("email").value;
 let password= document.getElementBytd("password").value;

 if(name===""){
  alert("name must be filled out");
  retun false;
 }
 if(email===""){
  alert("email must be filled out");
  retun false;
 } else{}
 
 if(password===""){
  alert("password must be filled out");
  retun false;
 }
 alert("form submitted successfully!");
 retun true;
}
