function extract(content) {
    let result = []
    const text  = document.getElementById('content')
    let rego = /\((.+?)\)/gm
    console.log(content.match(rego))
    let m = rego.exec(text)
    while(m !== null){
        result.push(m[1])
        m = rego.exec(text)
    }
    return result.join('; ')

}