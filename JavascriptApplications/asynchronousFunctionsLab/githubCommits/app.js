function loadCommits() {
    const commits = document.getElementById("commits")
    const repo = document.getElementById("repo").value
    const username = document.getElementById("username").value
    fetch(`https://api.github.com/repos/${username}/${repo}/commits`).then(res => res.json()).then(data => {
        data.forEach(el => {
            const li = document.createElement("li")
            console.log(el)
            li.textContent = `${el.commit.author.name}: ${el.commit.message}`
            commits.appendChild(li)
        })
    })
}