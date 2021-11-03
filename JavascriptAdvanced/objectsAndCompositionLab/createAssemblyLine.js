createAssemblyLine = () => {
    return {
        hasClima(obj) {
            obj.temp = 21
            obj.tempSettings = 21
            obj.adjustTemp = function () {
                if (obj.temp > obj.tempSettings) {
                    obj.temp--
                } else if (obj.tempSettings > obj.temp) {
                    obj.temp++
                }
            }
        },
        hasAudio(track) {
            track.currentTrack = {
                name: null,
                artist: null
            }
            track.nowPlaying = function () {
                if (track.currentTrack.name !== null && track.currentTrack.artist !== null) {
                    console.log(`Now playing '${track.currentTrack.name}' by ${track.currentTrack.artist}`)
                }
            }
        },
        hasParktronic(object) {
            object.checkDistance = function (distance) {
                let result = ''
                if (distance < 0.1) {
                    result = "Beep! Beep! Beep!"
                } else if (distance < 0.25) {
                    result = "Beep! Beep!"
                } else if (distance < 0.5) {
                    result = "Beep!"
                }
                console.log(result)
            }
        }
    }
}