function validate() {
    document.getElementById('email').addEventListener('change', (ev) => {
        if(/^[a-z]+@[a-z]+\.[a-z]+$/.test(ev.target.value)){
            ev.target.className = ''
        }else{
            ev.target.className = 'error'
        }
    })
}