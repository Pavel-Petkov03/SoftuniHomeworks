class Me{
    constructor(me) {
        console.log("da")
        this.me = me
    }

    help(){
        const btn = document.querySelector("button")
        console.log(1)
        btn.addEventListener("click" , () => {
            console.log(this)
        })
    }
}