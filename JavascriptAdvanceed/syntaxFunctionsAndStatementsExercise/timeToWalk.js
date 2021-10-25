function solveTime(steps, footstep, kmPerHour) {
    let meters = steps * footstep
    let additionalMinutes = Math.floor(meters / 500)
    let km = meters / 1000
    let hours = km / kmPerHour
    let seconds = hours * 3600 + 60 * additionalMinutes
    let finalHours = Math.floor(hours) <= 9 ? `0${Math.floor(hours)}` : `${Math.floor(hours)}`
    let finalMinutes = Math.floor(seconds / 60) <= 9 ? `0${Math.floor(seconds / 60)}` : `${Math.floor(seconds / 60)}`
    let finalSeconds = seconds % 60 <= 9 ? `0${(seconds % 60).toFixed()}` : `${(seconds % 60).toFixed()}`
    console.log(`${finalHours}:${finalMinutes}:${finalSeconds}`)
}