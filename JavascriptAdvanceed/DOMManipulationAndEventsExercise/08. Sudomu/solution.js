function solve() {
    function arrayOfInputs() {
        let final = []
        Array.from(document.querySelectorAll('tbody tr')).forEach(tr => {
            final.push(Array.from(tr.children).map(td => td.children[0].value))
        })
        return final
    }

    function horizontal(length, matrix) {
        let isWin = true
        let isBreak = false
        for (let row of matrix) {
            row = row.map(col => Number(col))
            for (let col = 1; col <= length; col++) {
                if (!row.includes(col)) {
                    isWin = false
                    isBreak = true
                    break
                }
                if (isBreak) {
                    break
                }
            }
        }
        return isWin
    }


    function vertical(length, matrix) {
        let isWin = true
        let isBreak = false
        for (let index = 0; index < length; index++) {
            let row = []
            for (const m of matrix) {
                row.push(Number(m[index]))
            }
            for (let col = 1; col <= length; col++) {
                if (!row.includes(col)) {
                    isWin = false
                    isBreak = true
                    break
                }
            }
            if (isBreak) {
                break
            }
        }
        return isWin
    }

    const allRows = arrayOfInputs()
    let [checkButton, clearButton] = Array.from(document.querySelectorAll('button'))
    let table = document.querySelector('table')
    let insertP = document.getElementById('check').children[0]
    checkButton.addEventListener('click', (ev) => {
        const allRows = arrayOfInputs()
        const length = allRows.length
        if (horizontal(length, allRows) && vertical(length, allRows)) {
            table.style.border = '2px solid green'
            insertP.textContent = "You solve it! Congratulations!"
            insertP.style.color = 'green'
        }else{
            table.style.border = '2px solid red'
            insertP.textContent = "NOP! You are not done yet..."
            insertP.style.color = 'red'
        }
    })
    clearButton.addEventListener('click', ()=> {
         let trs = Array.from(document.querySelectorAll('tbody tr'))
        trs.forEach(tr => {
            Array.from(tr.children).forEach(td => td.firstElementChild.value = '')
            table.style.border = ''
            insertP.textContent = ''
        })
    })
}

