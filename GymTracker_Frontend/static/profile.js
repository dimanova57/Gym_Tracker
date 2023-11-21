var yourToken = getCookie('token')
var userInfo = document.getElementById('user_info')
var statisctic = document.getElementById('statistic')
console.log(document.cookie)
console.log(yourToken)

fetch('http://127.0.0.1:8000/get_weeks_statistic/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({'token': yourToken})
})
    .then(response => response.json())
    .then(data => {
        console.log(data)
        var data = data['workout_data_list']
        console.log(data)
        var dates = Object.keys(data);
        var values = Object.values(data);

        var ctx = document.getElementById('myChart').getContext('2d');

        var myChart = new Chart(ctx, {
        type: 'bar', // Тип графіка (у цьому випадку, стовпчаста діаграма)
        data: {
            labels: dates, // Вісь X
            datasets: [{
                label: 'Numbers', // Назва набору даних
                data: values, // Вісь Y
                backgroundColor: 'rgba(3, 150, 136, 0.65)', // Оранжевий колір стовпців (непрозорий)
                borderWidth: 1 // Ширина межі стовпців
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                      grid: {
                          display: true // Відключення внутрішніх ліній мережі для вісі X
                    }
                },
                y: {
                      grid: {
                          display: true // Відключення внутрішніх ліній мережі для вісі Y
                      }
                  }
            }
        }
    });
    })


function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    }