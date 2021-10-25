function requestValidator(obj) {
    const validMethods = ["GET", "POST", "DELETE", "CONNECT"];
    const validVersion = ["HTTP/0.9", "HTTP/1.0", "HTTP/1.1", "HTTP/2.0"];
    let errorMessage = "Invalid request header: Invalid "
    let error = false
    let uriValidation = /^[\w.]+$/;
    let messageValidation = /^[^<>\\&'"]*$/;
    if (!(obj.method && validMethods.includes(obj.method))) {
        error = true
        errorMessage += "Method"
    }
    else if (!(obj.uri && (uriValidation.test(obj.uri) || obj.uri === "*"))) {
        error = true
        errorMessage += "URI"
    }
    else if (!(obj.version && validVersion.includes(obj.version))) {
        error = true
        errorMessage += "Version"
    }
    else if (!(obj.hasOwnProperty("message") && (messageValidation.test(obj.message) || obj.message === ""))) {
        error = true
        errorMessage += "Message"
    }

    if(error){
        throw new Error(errorMessage)
    }

    return obj;
}