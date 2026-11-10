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

sendingForm(registerForm, (data)=>{
    if (data.success){
        verificateForm.classList.add('opened-form')
        registerForm.classList.remove('opened-form')
        verificateForm.querySelector("b").textContent = `(${data.email})`

    }else{
        console.log(data.errors);
    }
})
sendingForm(loginForm, (data)=>{
    if (data.success){
        window.location.href = '/main'
    }else {
        console.log(data.errors)
    }
}) 
sendingForm(verificateForm, (data)=>{
    if (data.success){
        verificateForm.classList.remove('opened-form')
        loginForm.classList.add('opened-form')
    }else {
        console.log(data.errors)
    }
}) 



