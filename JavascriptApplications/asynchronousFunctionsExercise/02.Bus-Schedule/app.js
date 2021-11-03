function solve() {
    let currentId = "depot"
    const field = document.getElementById("info")
    const departButton = document.getElementById("depart")
    const arriveButton = document.getElementById("arrive")

    async function depart() {
        let data = await getById()
        field.textContent = `Next stop ${data.name}`
    }

    async function arrive() {
        let data = await getById()
        field.textContent = `Arriving at ${data.name}`
        currentId = data.next
    }

    async function getById() {
        toggleButton()
        let res = await fetch(`http://localhost:3030/jsonstore/bus/schedule/${currentId}`)
        return await res.json()
    }
    function toggleButton(){
        if(arriveButton.disabled){
            arriveButton.disabled = false
            departButton.disabled = true
        }else{
            arriveButton.disabled = true
            departButton.disabled = false
        }
    }
    return {
        depart,
        arrive
    };
}

let result = solve();