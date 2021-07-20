function solve() {
  const validData = ['onclick', 'JSON.stringify()', 'A programming API for HTML and XML documents'];
  let arrayOfSections = Array.from(document.querySelectorAll('section'))

    let counter = 0
    Array.from(document.querySelectorAll('.answer-text')).forEach(btn => {
        btn.addEventListener('click', (ev) => {
            let section = ev.target.parentNode.parentNode.parentNode.parentNode
            if(validData.includes(ev.target.textContent)){
                counter++
            }
            section.style.display = 'none'
            try {
                let nextSection = arrayOfSections[arrayOfSections.indexOf(section) + 1]
                nextSection.style.display = 'block'
            }catch (TypeError){
                let result = document.getElementsByTagName('h1')[1]
                result.parentNode.parentNode.style.display = 'block'
                result.textContent = counter === 3 ? "You are recognized as top JavaScript fan!" : `You have ${counter} right answers`
            }
        })
    })
}
