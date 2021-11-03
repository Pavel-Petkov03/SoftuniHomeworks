window.addEventListener('load', solution);

function solution() {
    const firstName = document.getElementById("fname")
    const email = document.getElementById("email")
    const phone = document.getElementById("phone")
    const address = document.getElementById("address")
    const code = document.getElementById("code")
    const submitButton = document.getElementById("submitBTN")
    const editBtn = document.getElementById("editBTN")
    const continueBtn = document.getElementById("continueBTN")
    const arrayOfInput = [firstName , email , phone , address , code]
    submitButton.addEventListener("click", (ev) => {
        if (email.value !== "" && firstName.value !== "") {
            const allLi = createArrayOfLi()
            const ul = document.getElementById("infoPreview")
            allLi.forEach(el => ul.appendChild(el))
            ev.target.disabled = true
            editBtn.disabled = false
            continueBtn.disabled = false
            arrayOfInput.forEach(el => el.value = "")
        }
    })

    editBtn.addEventListener("click" , () => {
        const allLi = Array.from(document.querySelectorAll("li"))

        arrayOfInput.forEach((el , index) => {
            el.value = allLi[index].textContent.split(": ")[1]
            allLi[index].remove()
        })
        submitButton.disabled = false
        editBtn.disabled = true
        continueBtn.disabled = true
    })

    continueBtn.addEventListener("click" , () => {
        const div = document.getElementById("block")
        div.innerHTML = ""
        const h3 = document.createElement("h3")
        h3.textContent = "Thank you for your reservation!"
        div.appendChild(h3)
    })

    function createArrayOfLi() {
        const arrayOfLi = []
        for (let index = 0; index < 5; index++) {
            arrayOfLi.push(document.createElement("li"))
        }
        const arrayOfNames = ["Full Name: ", "Email: ", "Phone Number: ", "Address: ", "Postal Code: "]
        const arrayOfData = [firstName.value, email.value, phone.value, address.value, code.value]
        arrayOfLi.forEach((el, index) => {
            el.textContent = arrayOfNames[index] + arrayOfData[index]
        })
        return arrayOfLi
    }
}
