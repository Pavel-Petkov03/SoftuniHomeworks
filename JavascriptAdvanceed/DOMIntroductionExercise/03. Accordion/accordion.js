function toggle() {
    let extraText = document.getElementById('extra')
    let btn = document.getElementsByClassName('button')[0]
    if(extraText.style.display === 'block'){
        extraText.style.display = 'none'
        btn.textContent = 'More'
    }else{
        extraText.style.display = 'block'
        btn.textContent = 'Less'
    }

}