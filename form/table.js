
class Table {
    constructor(rows, cols, data) {
        this.rows = rows
        this.cols = cols
        this.data = data
        this.table = document.createElement("table");

        document.body.appendChild(this.table)
    }

    sync() {
        for (let r = 0; r < this.rows; r++) {
            const currentRow = this.table.insertRow()
            for (let c = 0; c < this.cols; c++) {
                const cell = document.createElement('td')
                cell.id = this.getPixelID(r, c)
                cell.style.backgroundColor = this.data[cell.id] ? 'white' : 'black'

                currentRow.appendChild(cell)
            }
        }
    }

    getPixelID(r, c) {
        return r * this.cols + c
    }

    getRowAndColFromID(id, numCols) {
        return [Math.floor(id / numCols), id % numCols]
    }

    getCell(id) {
        return document.getElementById(id)
    }

}
