function attachEventsListeners() {
    Array.from(document.querySelectorAll('div input:last-child')).forEach(btn => {
        btn.addEventListener('click', (ev) => {
            const placeText = ev.target.id
            const value = Number(ev.target.parentNode.querySelector('input').value)
            function convertToDays(measurement, value) {
                switch (measurement) {
                    case 'hoursBtn' :
                        return value / 24
                    case 'daysBtn' :
                        return value
                    case 'minutesBtn' :
                        return value / 1440
                    case 'secondsBtn' :
                        return value / 86400
                }
            }

            let convertedToDays = convertToDays(placeText, value)
            document.getElementById('days').value = convertedToDays
            document.getElementById('hours').value = convertedToDays * 24
            document.getElementById('minutes').value = convertedToDays * 1440
            document.getElementById('seconds').value = convertedToDays * 86400
        })
    })
}
