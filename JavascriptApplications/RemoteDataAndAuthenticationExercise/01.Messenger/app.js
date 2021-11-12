import {generateRequest} from "../utils.js";

function attachEvents() {
    document.getElementById("submit").addEventListener("click" , post)
    document.getElementById("refresh").addEventListener("click", get)
}

async function post(ev) {
    ev.preventDefault()
    let author = document.querySelector('input[name="author"]')
    let content = document.querySelector('input[name="content"]')
    try {
        await generateRequest("http://localhost:3030/jsonstore/messenger", "post", {
            author : author.value, content : content.value
        })
    }catch (er){
        alert(er.message)
    }
    author.value = ''
    content.value = ''
}

async function get(){
    let res = await fetch("http://localhost:3030/jsonstore/messenger")
    let data = await res.json()
    document.getElementById("messages").value = Object.values(data).reduce((acc , cur) => {
        let {author , content} = cur
        acc.push(`${author}: ${content}`)
        return acc
    }, []).join("\n")
}



attachEvents();