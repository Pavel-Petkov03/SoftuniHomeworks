function attachEventsListeners() {

    let inputUnits = document.querySelector('#inputUnits')
    let outputUnits = document.querySelector('#outputUnits')
    let distance = document.getElementById('inputDistance')

    function returnValueFromAnyKindToMeters(measurement, value) {
        switch (measurement) {
            case 'km' :
                return value * 1000
            case  'mm' :
                return value * 0.001
            case 'cm' :
                return value * 0.01
            case 'm' :
                return value
            case "mi" :
                return 1609.34 * value
            case 'yrd' :
                return value * 0.9144
            case 'ft' :
                return value * 0.3048
            case 'in' :
                return value * 0.0254
        }
    }

    document.getElementById('convert').addEventListener('click', (ev) => {
        let first  = returnValueFromAnyKindToMeters(inputUnits.value, Number(distance.value))
        let second = returnValueFromAnyKindToMeters(outputUnits.value, 1)
        document.getElementById('outputDistance').value = first / second
    })
}