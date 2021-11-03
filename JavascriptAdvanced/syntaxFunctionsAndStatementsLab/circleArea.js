function calculateArea(type){
    let result;
    if (typeof type == "number"){
        result = (Math.pow(type, 2) * Math.PI).toFixed(2)
    }
    else{
        result = `We can not calculate the circle area, because we receive a ${typeof type}.`
    }
    console.log(result)
}