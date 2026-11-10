const detailUserFormElement = document.querySelector("#detailUserModel")
const modalBG = document.querySelector("#firstEntryModalBG")

sendingForm(detailUserFormElement, (data) => {
    if (data.success) {
        modalBG.remove()
    } else {
        console.log(data.errors)
    }
})