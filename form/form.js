const table = document.createElement("table");
const squareRoot = 15
const cells = new Array(squareRoot * squareRoot)

function clickListener(event) {
    console.log(event.target.id)
    cells[event.target.id] = !cells[event.target.id]

    event.target.style.backgroundColor =
        cells[event.target.id]
            ? 'aqua'
            : 'white'
}

function createCell(r, c) {
    const cell = document.createElement('td')
    cell.id = r * squareRoot + c
    cell.addEventListener('click', clickListener)

    return cell
}

for (let r = 0; r < squareRoot; r++) {
    const currentRow = table.insertRow()

    for (let c = 0; c < squareRoot; c++)
        currentRow.appendChild(createCell(r, c))

}

document.body.appendChild(table)
