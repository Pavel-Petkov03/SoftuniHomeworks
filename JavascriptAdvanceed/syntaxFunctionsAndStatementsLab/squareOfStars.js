function m(num){
    for (let row = 0; row < num; row++){
        let result = []
        for(let col= 0; col < num; col++){
            result.push('*')
        }
        console.log(result.join(' '))
    }
}


m(2)

