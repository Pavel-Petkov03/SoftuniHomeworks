function week(text) {
    let result;
    switch (text) {
        case 'Monday':
            result = 1;
            break
        case 'Tuesday':
            result = 2;
            break
        case 'Wednesday':
            result = 3;
            break
        case 'Thursday':
            result = 4;
            break
        case 'Friday':
            result = 5;
            break
        case 'Saturday':
            result = 5;
            break
        case 'Sunday':
            result = 6;
            break
        default:
            result = 'error'
    }
    console.log(result)
}