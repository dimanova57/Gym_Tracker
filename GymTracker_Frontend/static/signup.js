
document.getElementById('signup').addEventListener('submit', function(el){
    el.preventDefault();
    console.log(signupForm)
    var signupForm = document.getElementById('signup');
    let name = signupForm.name.value;
    let email = signupForm.email.value;
    let password = signupForm.password.value;

    fetch('http://127.0.0.1:8000/auth/signup/', {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'username': name, 'email': email, 'password': password, 'about': 'Something'})
    })
    .then(response => response.json())
    .then(data => console.log(data))
})