


const squareRoot = 28
const cells = mnist[3].get()

function getPixelID(r, c) {
    return r * squareRoot + c
}

function getRowAndCol(id) {
    return [Math.floor(id / squareRoot), id % squareRoot]
}

function getCell(id) {
    return document.getElementById(id)
}

function startFlood(set, r, c) {
    const id = getPixelID(r, c)

    if (cells[id] && !set.has(id)) {
        getCell(id).style.backgroundColor = 'white'
        set.add(id)

        startFlood(set, r - 1, c - 1)
        startFlood(set, r - 1, c)
        startFlood(set, r - 1, c + 1)

        startFlood(set, r, c - 1)
        startFlood(set, r, c + 1)

        startFlood(set, r + 1, c - 1)
        startFlood(set, r + 1, c)
        startFlood(set, r + 1, c + 1)
    }
}

function createCell(r, c) {
    const cell = document.createElement('td')

    cell.id = getPixelID(r, c)
    cell.addEventListener('click', startFlood)
    cell.style.backgroundColor = 'black'

    return cell
}

function createTable() {

    const table = document.createElement("table");

    for (let r = 0; r < squareRoot; r++) {
        const currentRow = table.insertRow()
        for (let c = 0; c < squareRoot; c++) {
            currentRow.appendChild(createCell(r, c))
        }
    }

    document.body.appendChild(table)
    return table
}

const table = createTable()




