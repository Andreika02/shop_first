const btnChangeTheme = document.querySelector('#btn-change-theme')
const body = document.querySelector("body")

btnChangeTheme.addEventListener("click", toggleTheme)
let currentTheme = true


function setTheme(value) {
    if (value === true) {
        btnChangeTheme.src = '/static/Shop/img/sun.png'
        body.setAttribute("data-bs-theme", "light") 
    }
    else{
        btnChangeTheme.src = '/static/Shop/img/moon.png'
        body.setAttribute("data-bs-theme", "dark") 
    }
}


function toggleTheme() {
    currentTheme = !currentTheme
    setTheme(currentTheme)
}
