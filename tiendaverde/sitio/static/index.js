// for some reason you cant import json without the function defs going to hell
const recyclables = {
    "Plastico"    : ["Botellas", "Envases", "Bolsas"],
    "Papel"       : ["Periodicos", "Carton", "Papel de oficina"],
    "Vidrio"      : ["Botellas", "Frascos", "Cristaleria"],
    "Metal"       : ["Latas", "Cables", "Electrodomesticos pequeños"],
    "Electronico" : ["Telefonos moviles", "Baterias", "Componentes de computadoras"]
}

let wasteText = ''
let subwasteText = ''

function insertIntoDropdown(dropdown, name, onclick){
    let li = document.createElement("li")
    let a = document.createElement("a")

    a.setAttribute("class", "dropdown-item")
    a.setAttribute("href", "#")
    a.setAttribute("onClick", onclick)
    a.text = name

    dropdown.insertAdjacentElement("afterbegin", li)
    li.insertAdjacentElement("afterbegin", a)
}

// preferably this wouldnt be called every time you click the dropdown
// but thankfully the performance cost is neglibible
// so i guess we get away with it this time??
function waste(){
    let wasteDropdown = document.getElementById("waste-dropdown")

    wasteDropdown.innerHTML = ''

    for(let key in recyclables){
        insertIntoDropdown(wasteDropdown, key, "subwaste(this)")
    } 
}

function subwaste(component){
    wasteText = component.text
    document.getElementById("waste-label").innerHTML = component.text
    document.getElementById("subwaste-label").innerHTML = "Desecho"
    subwasteText = ''

    let subwasteDropdown = document.getElementById("subwaste-dropdown")

    // clear subwaste dropdown
    subwasteDropdown.innerHTML = ''

    // generate subwaste dropdown
    for(let i = 0; i < recyclables[component.text].length; i++){
        let listElement = recyclables[component.text][i]

        insertIntoDropdown(subwasteDropdown, listElement, "select(this)")
    }

    verify()
}

function select(component){
    subwasteText = component.text
    document.getElementById("subwaste-label").innerHTML = subwasteText
    verify()
}

function verify(){
    let button = document.getElementById("form-submit")
    let ids = ["inputName", "inputEmail", "inputAddress"]

    if(subwasteText == ''){
        button.disabled = true
        return
    }

    for(let i = 0; i < ids.length; i++){
        if(document.getElementById(ids[i]).value.trim().length <= 0){
            button.disabled = true
            return
        }
    }

    button.disabled = false
}