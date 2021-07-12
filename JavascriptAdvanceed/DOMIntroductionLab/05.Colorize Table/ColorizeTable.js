function colorize() {
    [...document.querySelectorAll('tr:nth-child(even)')].forEach(el => el.style.backgroundColor = 'Teal')
}