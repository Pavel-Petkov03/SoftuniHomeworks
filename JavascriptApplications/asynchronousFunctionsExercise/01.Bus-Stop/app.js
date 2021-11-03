function getInfo() {
    let id = document.getElementById("stopId").value
    const stopName = document.getElementById("stopName")
    const busesUl = document.getElementById("buses")
    fetch(`http://localhost:3030/jsonstore/bus/businfo/${id}`).then(res => res.json()).then(data => {
        stopName.textContent = data.name
        Object.entries(data.buses).forEach(array => {
            let [bus , time] = array
            let li = document.createElement("li")
            li.textContent = `Bus ${bus} arrives in ${time} minutes`
            busesUl.appendChild(li)
        })
    }).catch(er => {
        stopName.textContent = "Error"
    })
}