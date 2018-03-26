
class Table {
    constructor(rows, cols, data) {
        this.rows = rows
        this.cols = cols
        this.data = data
        this.cells = new Array()
        this.spots = new Set()

        this.table = document.createElement("table");
        document.body.appendChild(this.table)

        this.sync()
    }

    sync() {
        for (let r = 0; r < this.rows; r++) {
            const currentRow = this.table.insertRow()
            for (let c = 0; c < this.cols; c++) {
                const cell = document.createElement('td')
                cell.id = this.getCellID(r, c)
                cell.style.backgroundColor = Number(this.data[cell.id]) ? 'white' : 'black'

                this.cells.push(cell)
                this.spots.add(cell.id)

                currentRow.appendChild(cell)
            }
        }
    }

    getCellID(r, c) {
        return r * this.cols + c
    }

    getRowAndColFromID(id) {
        return [Math.floor(id / this.cols), id % this.cols]
    }

    getCell(id) {
        return document.getElementById(id)
    }

}
