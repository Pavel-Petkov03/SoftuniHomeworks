function create(words) {
   let final = []
   let content = document.getElementById('content')
   words.forEach(w => {
      const div = document.createElement('div')
      const p = document.createElement('p')
      p.textContent = w
      p.style.display = 'none'
      div.appendChild(p)
      div.addEventListener('click', (ev) => {
         if(ev.target.children[0].style.display ===  'block'){
            ev.target.children[0].style.display = 'none'
         }else{
            ev.target.children[0].style.display = 'block'
         }
      })
      final.push(div)
   })
   final.forEach(el => content.appendChild(el))
}