function roadRadar(km, place) {
    let maxSpeed;
    switch (place) {
        case 'motorway':
            maxSpeed = 130;
            break;
        case 'interstate':
            maxSpeed = 90;
            break;
        case 'city':
            maxSpeed = 50;
            break;
        case 'residential':
            maxSpeed = 20;
            break;
    }
    if (km <= maxSpeed) {
        console.log(`Driving ${km} km/h in a ${maxSpeed} zone`);
    } else {
        let overDrive = km - maxSpeed;
        let status;
        if (overDrive <= 20) {
            status = 'speeding'
        } else if (overDrive <= 40) {
            status = 'excessive speeding'
        } else {
            status = 'reckless driving'
        }
        console.log(`The speed is ${overDrive} km/h faster than the allowed speed of ${maxSpeed} - ${status}`)
    }
}