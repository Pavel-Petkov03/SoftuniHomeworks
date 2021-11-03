function solve() {
    let wholeTextMassive = document.getElementById('input').value.split('.').filter(el => el.length > 0);
    let result = document.getElementById('output');
    while (wholeTextMassive.length > 0) {
        if (wholeTextMassive.length >= 3) {
            let text = [wholeTextMassive.shift(), wholeTextMassive.shift(), wholeTextMassive.shift()].join('.')
            const p = document.createElement("p")
            p.textContent = text
            result.append(p)
        } else {
            let text = '';
            let len = wholeTextMassive.length
            for (let i = 0; i < len; i++ ){
                text += wholeTextMassive.shift()
            }
            const p = document.createElement("p")
            p.textContent = text
            result.append(p)
        }
    }
}