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