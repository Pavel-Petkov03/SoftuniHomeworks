function loadRepos() {
   const http = new XMLHttpRequest()
   http.addEventListener("readystatechange" , () => {
      console.log(document.getElementById("res"))
      document.getElementById("res").textContent = http.response
   })

   http.open("GET", "https://api.github.com/users/testnakov/repos")
   http.send()
}