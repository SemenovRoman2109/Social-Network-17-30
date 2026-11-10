let isSending = false
function sendingForm(form, resultFunc){
    form.addEventListener('submit', async function (event){
        event.preventDefault()
        if(isSending == false){
            isSending = true 
            const response = await fetch(form.action, {
                method: "POST",
                headers: {
                    "X-CSRFToken": form.querySelector("input[name='csrfmiddlewaretoken']").value
                },
                body: new FormData(form)
            })
            const data = await response.json()
            resultFunc(data)
            isSending = false
        }
    } )
}

