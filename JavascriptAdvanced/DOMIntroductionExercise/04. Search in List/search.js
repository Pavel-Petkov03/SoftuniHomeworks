function search() {
   let counter = 0
   const searchText = document.getElementById('searchText').value
   let listItems = [...document.querySelectorAll('ul li')]
   listItems.forEach((el ) => {
      el.style.textDecoration = ''
      el.style.fontWeight = ''
   })
   for (const listItem of listItems) {
      if(listItem.textContent.includes(searchText)){
         listItem.style.textDecoration = 'underline'
         listItem.style.fontWeight = 'bold'
         counter++
      }
   }
   document.getElementById('result').textContent = `${counter} matches found`
}

