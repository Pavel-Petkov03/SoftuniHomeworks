function e(type, attributes, children) {
    let element = document.createElement(type)
    Object.entries(attributes).forEach(array => {
        let [prop, val] = array
        element[prop] = val
    })
    if (Array.isArray(children)) {
        children.forEach(el => element.appendChild(el))
    }
    return element
}

let symbolObj = {
    "Sunny" : "☀",
    "Partly sunny" : "⛅",
    "Overcast" : "☁",
    "Rain" : "☂"
}


function buildTodayForecast(data){
    let {name , forecast} = data
    return e("div" , {id : "current"}, [
        e("div" , {className : "label", textContent : "Current Conditions"}),
        e("div", {className: "forecasts"}, [
            e("span" , {className : "condition symbol", textContent: symbolObj[forecast.condition]}),
            e("span" , {className : "condition"}, [
                e("span" , {className : "forecast-data", textContent : name}),
                e("span" , {className : "forecast-data", textContent : `${forecast.low}°/${forecast.high}°`}),
                e("span" , {className : "forecast-data", textContent : forecast.condition})
            ])
        ])
    ])
}

function buildNextDayForecast(data){
    return e("div" , {id : "upcoming"} , [
        e("label" , {className : "label", textContent : "Three-day forecast"}),
        e("div" , {className : "forecast-info"}, [
            ...data.forecast.reduce((acc, cur )  => {
                acc.push(
                    e("span" , {className : "upcoming"}, [
                        e("span" , {textContent : symbolObj[cur.condition]}),
                        e("span" , {className : "forecast-data", textContent : `${cur.low}°/${cur.high}°`}),
                        e("span" , {className : "forecast-data", textContent : cur.condition})
                    ])
                )
                return acc
            }, [])
        ])
    ])
}


async function returnDataByGivenEndpoint(endpoint, code){
    let res = await fetch(`${endpoint}${code}`)
    return await res.json()
}
function replaceContent(todayContent , nextDayContent){
    let forecast = document.getElementById("forecast")
    let current = document.getElementById("current")
    let upcoming = document.getElementById("upcoming")
    current.replaceWith(buildTodayForecast(todayContent))
    upcoming.replaceWith(buildNextDayForecast(nextDayContent))
    forecast.style.display = "block"
}

function attachEvents() {
    const button = document.getElementById("submit")
    const locationInput = document.getElementById("location")
    button.addEventListener("click" ,   async () => {
        let data = await returnDataByGivenEndpoint("http://localhost:3030/jsonstore/forecaster/locations", "")
        let town = data.find(el => el.name === locationInput.value)
        if (town){
            let {code} = town
                let [todayData,upcomingData] = await Promise.all([
                returnDataByGivenEndpoint("http://localhost:3030/jsonstore/forecaster/today/" , code),
                returnDataByGivenEndpoint(`http://localhost:3030/jsonstore/forecaster/upcoming/` , code)
                ]
            )
            replaceContent(todayData , upcomingData)
        }else{
            let forecast = document.getElementById("forecast")
            forecast.textContent = "Error"
            forecast.style.display = "block"
            // note: if error happens the page must be reloaded again because the current nodes are deleted
        }
    })
}


attachEvents();