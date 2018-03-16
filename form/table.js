

class Cell {
    constructor(id, action) {
        this.cell = document.createElement('td')
        this.cell.id = id
        this.cell.style = style
        this.cell.addEventListener('click', action)
    }
}

class Table {
    constructor(rows, cols, action) {
        this.rows = rows
        this.cols = cols

        this.table = document.createElement("table");

        for (let r = 0; r < this.rows; r++) {
            const currentRow = this.table.insertRow()
            for (let c = 0; c < this.cols; c++) {
                const cell = new Cell(this.getPixelID(r, c), action)
                currentRow.appendChild(cell)
            }
        }

        document.body.appendChild(this.table)

    }

    getPixelID(r, c) {
        return r * this.cols + c
    }

    getRowAndColFromID(id) {
        return [Math.floor(id / this.cols), id % this.cols]
    }

    getCell(id) {
        return document.getElementById(id)
    }
}

