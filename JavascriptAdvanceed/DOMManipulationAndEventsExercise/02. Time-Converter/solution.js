function attachEventsListeners() {
    Array.from(document.querySelectorAll('div input:last-child')).forEach(btn => {
        btn.addEventListener('click' , (ev)=> {
            let finalHours = 0
            let finalMinutes = 0
            let finalDays = 0
            let finalSeconds = 0
            const placeText = ev.target.id
            const value = Number(ev.target.parentNode.querySelector('input').value)
            switch (placeText){
                case 'hoursBtn' :
                    finalDays = value / 24
                    finalHours = value
                    finalMinutes = finalHours * 60
                    finalSeconds = finalMinutes * 60
                    break
                case 'daysBtn':
                    finalDays = value
                    finalHours = value * 24
                    finalMinutes = finalHours * 60
                    finalSeconds = finalMinutes * 60
                    break
                case 'minutesBtn':
                    finalDays = value / 3600
                    finalHours = value / 60
                    finalMinutes = value
                    finalSeconds = finalMinutes * 60
                    break
                case 'secondsBtn' :
                    finalDays = value / 86400
                    finalHours = value / 3600
                    finalMinutes = value / 60
                    finalSeconds = value
                    break
            }
            document.getElementById('days').value = finalDays
            document.getElementById('hours').value = finalHours
            document.getElementById('minutes').value = finalMinutes
            document.getElementById('seconds').value = finalSeconds
        })
    })
}