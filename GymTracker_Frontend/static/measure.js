let one_rep_max_form = document.getElementById("one_rep_max");
let main_div = document.getElementsByClassName("main")[0]

one_rep_max_form.addEventListener("submit", (e) => {
    e.preventDefault();

    let weight = document.getElementById("weight").value;
    let reps = document.getElementById("reps").value;

    if (weight && reps && !isNaN(weight) && !isNaN(reps)) {
        let result = Math.round(parseFloat(weight) / (1.0278 - 0.0278 * parseFloat(reps))) + " kg";
        alert(result.toString())
    }
    else {
        alert("The data you entered is incorrect")
    };
});