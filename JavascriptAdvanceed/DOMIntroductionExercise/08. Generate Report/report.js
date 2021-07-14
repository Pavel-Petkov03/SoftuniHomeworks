function generateReport() {
    let result = []
    let allValues = [...document.querySelectorAll('th input')]
    let checkedValues = allValues.filter(el => el.checked)
    let fillIndex = () =>{
        let result = []
        checkedValues.forEach(el => result.push(allValues.indexOf(el)))
        return result
    }
    let allColumns = fillIndex()
    let allRows = [...document.querySelectorAll('tbody tr')]
    for (const row of allRows) {
        let rowData = row.children
        let obj = {}
        for(let i = 0; i < rowData.length; i++){
            if(allColumns.includes(i)){
                let key = allValues[i].parentNode.textContent.toLowerCase().slice(0,-1)
                obj[key] = rowData[i].textContent
            }
        }

        result.push(obj)
    }
    document.getElementById('output').value = JSON.stringify(result)
}
