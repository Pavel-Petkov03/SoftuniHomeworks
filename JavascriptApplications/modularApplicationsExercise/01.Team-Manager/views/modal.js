import {e} from "../utils.js"
// not using render because it makes DOM again
function buildModal(message, okBool , cancelBool, callback){
    // if cancelButton is defined the callback will be trigerred in it
    // if not in okButton
    let okButton , cancelButton
    if(okBool){
        okButton = e("button" , {textContent : "Continue"})
        okButton.addEventListener("click", onContinue.bind(null , callback))
    }
    if(cancelBool){
        cancelButton = e("button" , {textContent : "Cancel"})
        cancelButton.addEventListener("click", onCancel)
    }
    return modalTemplate(message , okButton , cancelButton)
}

const modalTemplate = (message, okButton , cancelButton) => {
    return e("div" , {className : "overlay"}, [
        e("div" , {className : "modal"}, [
            e("p" , {textContent : message}),
            e("div" , {className : "button-space"} , [
                okButton , cancelButton
            ])
        ])
    ])
}


async function onContinue(callback , ev){
    ev.preventDefault()
    removeModal(ev)
    if(typeof callback === "function"){
        await callback()
    }
}



function onCancel(ev){
    removeModal(ev)
}


function removeModal(ev){
    ev.target.parentNode.parentNode.parentNode.remove()
}

function renderModal(message , okBool , cancelBool, callback){
    document.querySelector("main").appendChild(buildModal(message , okBool , cancelBool,callback))
}


export async function handleModal(message , okBool , cancelBool , callback){
    try{
        if(okBool && !cancelBool){
            await callback()
            return
        }
        renderModal(message , okBool  ,cancelBool , callback)
    }catch(er){
        renderModal(er.message , true)
    }
}