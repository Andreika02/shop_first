const btnChangeTheme = document.querySelector('#btn-change-theme')
const body = document.querySelector("body")

btnChangeTheme.addEventListener("click", toggleTheme)
let currentTheme = true
loadTheme()

function setTheme(value) {
    if (value === true) {
        btnChangeTheme.src = '/static/Shop/img/sun.png'
        document.body.setAttribute("data-bs-theme", "light") 
        localStorage.setItem("theme", value)
    }
    else{
        btnChangeTheme.src = '/static/Shop/img/moon.png'
        document.body.setAttribute("data-bs-theme", "dark") 
        localStorage.setItem("theme", value)
    }
    
}

function loadTheme(){
    const loaded_theme = localStorage.getItem("theme")
    if (loaded_theme !== null){
        if (loaded_theme === "true"){
            setTheme(true)
            currentTheme = true
        }
        else{
            setTheme(false)
            currentTheme = false
        }
    }
}


function toggleTheme() {
    currentTheme = !currentTheme
    setTheme(currentTheme)
}
