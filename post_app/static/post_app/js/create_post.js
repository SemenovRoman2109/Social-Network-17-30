// Відкриття/Закриття форми
const postForm = document.querySelector('#createPostBG');
const createPostButton = document.querySelector('#createPostButton');
const closePostButton = document.querySelector('#closeCreatePostForm');

createPostButton.addEventListener('click', ()=>{
    postForm.classList.remove('hidden');
})

closePostButton.addEventListener('click',()=>{
    postForm.classList.add('hidden');
})

postForm.addEventListener('click', (event) =>{
    if (event.target == postForm){
        postForm.classList.add('hidden');
    }
})

// Ввімкнення, створення тегів
const tagAddButton = document.getElementById("addTag")
const newTagContainer = document.getElementById("newTagContainer")
const tags = document.querySelectorAll(".tag-element")
const acceptTag = document.getElementById("acceptTag")
const newTagInput = document.querySelector("#newTagInput")

tags.forEach((tag)=> {
    tag.addEventListener("click", ()=>{
        tag.classList.toggle("active-tag")
        tag.querySelector("input").checked = ! tag.querySelector("input").checked
    })
})

tagAddButton.addEventListener("click", ()=>{
    tagAddButton.classList.add("hidden")
    newTagContainer.classList.remove("hidden")
})

acceptTag.addEventListener("click", ()=>{
    if (newTagInput.value.trim() != "") {
        const newTag = document.createElement("div")
        newTag.classList.add("tag-element")
        newTag.classList.add("active-tag")
        newTag.innerHTML = `
            <input type="checkbox" class="hidden" value = "${newTagInput.value.trim()}"  name="new_tags" checked>
            <p>${newTagInput.value.trim()}</p>
        `
        document.querySelector(".tags-container").insertBefore(newTag, newTagContainer)
        newTagInput.value = ''
    }
    newTagContainer.classList.add("hidden")
    tagAddButton.classList.remove("hidden")
})

// Посилання

const addLink = document.getElementById("addLink")
const removeLink = document.getElementById("removeLink")

addLink.addEventListener("click", ()=>{
    removeLink.classList.remove("hidden")
    const newLink = document.createElement("input")
    newLink.type = "url"
    newLink.name = "links"
    newLink.placeholder = "Введіть посилання"
    
    document.querySelector(".links-container").insertBefore(newLink, addLink)
})

removeLink.addEventListener("click", ()=>{
    const links = document.querySelectorAll(".links-container input")
    if (links.length <= 2){
        removeLink.classList.add("hidden")
    }
    links[links.length -1].remove()
})

// Відправка форми

document.addEventListener("DOMContentLoaded", ()=>{
    const createPostForm = document.querySelector('#createPostForm')
    
    sendingForm(createPostForm, (data) => {
        if (data.success) {
            window.location.reload()
        } else {
            console.log(data.errors)
        }
    })
})


