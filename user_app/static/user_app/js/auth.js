const registerForm = document.querySelector('#registerForm') 
const loginForm = document.querySelector('#loginForm') 
const verificateForm = document.querySelector('#verificateForm') 

const backToRegister = document.querySelector('#backToRegister')
const openRegister = document.querySelector('#openRegister')
const openLogin = document.querySelector('#openLogin')

openLogin.addEventListener('click',() => {
    loginForm.classList.add('opened-form')
    registerForm.classList.remove('opened-form')
})

openRegister.addEventListener('click',() => {
    loginForm.classList.remove('opened-form')
    registerForm.classList.add('opened-form')
})

backToRegister.addEventListener('click',() => {
    verificateForm.classList.remove('opened-form')
    registerForm.classList.add('opened-form')
})

// В Js подія submit - коли відправляють форму
// форма.addEventListener('submit', функція)

// В функції події - (event)=>{}
// Параметр event зберігає всю інформацію про подію
// event.preventDefault() - зупиняю стандартні події браузера (відправка форми, скролл та ін)

registerForm.addEventListener('submit', async function (event){
    event.preventDefault()
    const response = await fetch(registerForm.action, {
        method: "POST",
        headers: {
            "X-CSRFToken": registerForm.querySelector("input[name='csrfmiddlewaretoken']").value
        },
        body: new FormData(registerForm)   
    })
    const data = await response.json()
    if (data.success){
        verificateForm.classList.add('opened-form')
        registerForm.classList.remove('opened-form')
    }else{
        console.log(data.errors);
    }
} )

// Щоб відправити POST запит в async функції:

// const response = await fetch(форма.action, {
//        method: "POST", - вказує вид запиту
//        headers: {
//            "X-CSRFToken": csrfToken
//        },
//        body: new FormData(форма) - отримує всі дані з форми
//    })

// Щоб отримати csrfToken - форма.querySelector("input[name='csrfmiddlewaretoken']").value

// const data = await response.json() - отримує дані з відповіді сервера