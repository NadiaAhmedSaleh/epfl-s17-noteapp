 

 const userName=document.getElementById("person");


  const submit=document.getElementById("submit")

  submit.addEventListener('submit', function(e){

    e.preventDefault();

   const firstNameValue=userName.value;

   localStorage.setItem('myObject',firstNameValue)


   window.location.href("main.html")
   
   
   

   


 })