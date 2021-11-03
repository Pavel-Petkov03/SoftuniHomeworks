function loadRepos() {
    const repos = document.getElementById("repos")
    const username = document.getElementById("username")
    const value = username.value
    fetch(`https://api.github.com/users/${value}/repos`).then(res => {
        if(res.status === 404){
            throw new Error("This user is not found")
        }
        return res.json()
    }).then(data => {
        repos.innerHTML = ""
        data.forEach((cur) => {
            const li = document.createElement("li")
            const a = document.createElement("a")
            a.href = cur.html_url
            a.textContent = cur.full_name
            li.appendChild(a)
            repos.appendChild(li)
        })
    })
}