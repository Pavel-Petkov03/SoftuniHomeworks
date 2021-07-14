function extract(content) {
    let result = []
    const text  = document.getElementById(content).textContent
    let rego = /\((.+?)\)/gm
    let m = rego.exec(text)
    while(m !== null){
        result.push(m[1])
        m = rego.exec(text)
    }
    return result.join('; ')

}