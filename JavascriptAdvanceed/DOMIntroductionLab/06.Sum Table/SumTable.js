function sumTable() {
    let result = document.getElementById('sum')
    let neededNums = [...document.querySelectorAll('tr td:nth-child(2)')].slice(0,-1)
        result.textContent = neededNums.reduce((acc, cur) => acc += Number(cur.textContent), 0)


}