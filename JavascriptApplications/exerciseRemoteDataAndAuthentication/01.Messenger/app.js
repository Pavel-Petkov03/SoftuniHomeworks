function attachEvents() {
    document.getElementById("submit").addEventListener("click" , post)
    document.getElementById("refresh").addEventListener("click", get)
}

async function post(ev) {
    ev.preventDefault()
    let author = document.querySelector('input[name="author"]')
    let content = document.querySelector('input[name="content"]')
    await fetch("http://localhost:3030/jsonstore/messenger", {
        method : "post",
        headers: {"content-type": "application/json"},
        body : JSON.stringify({author : author.value , content : content.value})
    })

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