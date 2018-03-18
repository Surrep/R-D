
const colors = ['aqua', 'magenta', 'green', 'red', 'blue', 'orange', 'yellow', 'brown']

function randomColor() {
    return colors[Math.floor(Math.random() * colors.length)]
}

class Table {
    constructor(rows, cols, data) {
        this.rows = rows
        this.cols = cols
        this.data = data
        this.cells = new Array()
        this.visited = new Set()
        this.color = randomColor()

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
                cell.style.backgroundColor = this.data[cell.id] ? 'white' : 'black'
                this.cells.push(cell)

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

    addListener(fn) {
        const listener = event => {
            const [r, c] = this.getRowAndColFromID(event.target.id)

            fn(this, r, c)

            this.visited = new Set()
            this.color = randomColor()
        }

        for (let cell of this.cells)
            cell.addEventListener('click', listener)

        return this
    }


}
