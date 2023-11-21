document.getElementById('login').addEventListener('submit', function(el){
    el.preventDefault();
    var loginForm = document.getElementById('login');
    var errorLine = document.getElementById('error_line');
    var name = loginForm.name.value;
    var password = loginForm.password.value;

    fetch('http://127.0.0.1:8000/auth/login/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'username': name, 'password': password})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data['token']) {
            deleteCookie('token')
            setCookie('token', data['token'], 100);
            return;
        }
            errorLine.innerHTML = `${data['message']}`;
        })
})


function setCookie(name, value, daysToLive){
    var date = new Date();
    date.setTime(date.getTime() + daysToLive * 24 * 60 * 60 * 1000);
    let expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value}; ${expires}; path=/`;
}

function deleteCookie(name){
    setCookie(name, null, null)
}