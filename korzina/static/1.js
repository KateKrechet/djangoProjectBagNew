let fin = document.getElementById('fin')
let forma = document.getElementById('forma')
let forma1 = document.getElementById('forma1')
let pythonbut = document.getElementById('myformbut')
fin.onclick = f1
// forma.onsubmit = f3
// pythonbut.onclick=f3

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
    let adres = $('#id_adres').val();
    let name = $('#id_name').val();
    let tel = $('#id_tel').val();
    let re = /^[+][\d]{10}\d$/
    let valid = re.test(tel)
    console.log('Считываем данные введенные пользователем:', adres, name, tel);
    let url = '/cart/pobeda/'
    if (adres && name && tel && valid) {
        console.log('ok')
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

function f11(event, id) {
    event.preventDefault()
    // alert('hi')
    console.log(event.target)
    img = event.target
    img1 = img.getElementsByClassName('.serdce')
    console.log(img1)
    // img1.src='img/red.png'
    let color=''
    if (img.src.includes('static/img/white.png')) {
        img.setAttribute('src', 'static/img/red.png')
        color = 'red'
    } else {
        img.setAttribute('src', 'static/img/white.png')
        color = 'white'
    }
    let url = '/toizbran/'

    $.ajax(url, {
            method: 'POST',
            data: {k1: id, k2: color},

            success: function (response) {
                console.log(response.mes)
                // window.location.href = response.link
            },
            error: function (response) {
                console.log(response)
                console.log(this.error)
                console.log(url)
            },

        }
    )


}