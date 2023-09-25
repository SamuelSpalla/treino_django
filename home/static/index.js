function mostrar_tabela() {
    var table = document.getElementById("data-table")
    if (table.style.display === "none" || table.style.display === "") {
        table.style.display = "table"
    } else {
        table.style.display = "none"
    }
}

var button = document.getElementById("button")
button.addEventListener("click", mostrar_tabela)