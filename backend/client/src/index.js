const submit = () => {
    const url = "http://localhost:5000/login/submitasync";

    const body = {
        "username": document.getElementById("username").value,
        "password": document.getElementById("password").value
    };

    fetch(url, {
        "method": "POST",
        "body": JSON.stringify(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }).then((resp) => resp.json())
    .then((data) => showResults(data));
}

const showResults = data => {
    if (data.success) {
        document.getElementById("resultadoPositivo").innerHTML = "Login correcto";
        document.getElementById("resultadoNegativo").innerHTML = "";
    } else {
        document.getElementById("resultadoNegativo").innerHTML = "Login incorrecto";
        document.getElementById("resultadoPositivo").innerHTML = "";
    }
}