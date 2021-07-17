function attachGradientEvents() {
    document.getElementById('gradient').addEventListener('mousemove' ,(event) => {
        document.getElementById('result').textContent = `${Math.floor(event.offsetX / event.target.clientWidth * 100)}%`
    })
}