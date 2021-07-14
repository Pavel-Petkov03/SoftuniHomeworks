function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const search = document.getElementById('searchField').value.toLowerCase()
      let allData = [...document.querySelectorAll('tbody tr')]
      allData.forEach(el => el.textContent.toLowerCase())
      console.log(allData[0].innerText)
      allData.forEach(el => {
         if(el.textContent.toLowerCase().includes(search) && search !== ''){
            el.setAttribute('class', 'select')
         }else{
            el.removeAttribute('class' , 'select')
         }
      })
   }
}