function deleteByEmail() {
    const allData = Array.from(document.querySelectorAll("tbody tr td:nth-child(2)"))
    const wantedText = document.getElementsByTagName('input')[0].value
    let result = 'Not found.'
    for (const data of allData) {
        if(data.textContent === wantedText){
            result = 'Deleted'
            let row = data.parentNode
            row.parentNode.removeChild(row)
        }
    }
    document.getElementById('result').textContent = result
}