let fin = document.getElementById('fin')
let forma = document.getElementById('forma')
fin.onclick = f1

function f1() {
    forma.hidden = false

}

function f2() {
    let adres = $('#adres').val();
    let name = $('#name').val();
    let tel = $('#tel').val();
    console.log('Считываем данные введенные пользователем:', adres, name, tel);

    if ((adres === '') || (name === '') || (tel === '')) {
        alert('Данные не заполнены')
    }

    $.ajax({
        method: 'POST',
        url: '/cart/',
        data: {
            'city': adres,
            'name': name,
            'tel': tel,
            'type': 'params',

        },

        success: function (data) {
            console.log('Ответ с сервера получен', data)
            window.location = data;

        },
        error: function (error) {
            console.log('Error retrieving dependent options:', error)
        }


    })

}

//вариант f2 на уроке
function f3() {
    let adres = $('#adres').val();
    let name = $('#name').val();
    let tel = $('#tel').val();
    console.log('Считываем данные введенные пользователем:', adres, name, tel);
    let url = '/cart/pobeda/'
    if (adres && name && tel) {
        $.ajax(url, {
                method: 'POST',
                data: {k1: adres, k2: name, k3: tel},

                success: function (response) {
                    console.log(response.mes)
                    window.location.href = response.link
                },
                error: function (response) {
                    console.log(response)
                },

            }
        )
    } else {
        alert('ne zapolneno')
    }

}
