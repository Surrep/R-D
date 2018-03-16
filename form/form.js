

const table = document.createElement("table");
const squareRoot = 28
const cells = mnist[8].get()

function clickListener(event) {
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
    cell.style.backgroundColor = cells[cell.id] ? 'aqua' : 'white'

    return cell
}

function squaredDist(coord1, coord2) {
    return coord1.reduce(function (dist, coord1i, i) {
        return dist + Math.pow(coord1i - coord2[i], 2)
    }, 0)
}

function computeDistances() {
    let distances = new Set()

    for (let i = 0; i < cells.length; i++) {
        for (let j = 0; j < cells.length; j++) {
            if (cells[i] && cells[j] && i != j) {
                const iCoord = [Math.floor(i / squareRoot), i % squareRoot]
                const jCoord = [Math.floor(j / squareRoot), j % squareRoot]

                distances.add(squaredDist(iCoord, jCoord))
            }
        }
    }

    let max = 0
    let sum = 0
    for (let dist of Array.from(distances)) {
        sum += dist
        if (dist > max)
            max = dist
    }

    return sum

}






for (let r = 0; r < squareRoot; r++) {
    const currentRow = table.insertRow()
    for (let c = 0; c < squareRoot; c++) {
        currentRow.appendChild(createCell(r, c))
    }

}

document.body.appendChild(table)

