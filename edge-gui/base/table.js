
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


        this.header = document.createElement("h1")
        this.header.style.fontSize = "150px"


        this.legend = document.createElement('div')
        this.legend.style.width = "350px"
        this.legend.style.height = "25px"
        this.legend.style.marginTop = "450px"
        this.legend.style.marginLeft = "450px"
        this.legend.style.marginBottom = "450px"
        this.legend.style.backgroundColor = "black"

        document.body.appendChild(this.header)
        document.body.appendChild(this.table)
        document.body.appendChild(this.legend)

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
        const listener = async (event) => {
            const [r, c] = this.getRowAndColFromID(event.target.id)
            const paintings = fn(this, r, c)

            this.visited = new Set()
            this.color = randomColor()

            let count = 0
            const cumCell = [0, 0]
            let lastCell = null

            for (let painting of paintings) {
                count++

                const [cell, backgroundColor] = painting
                const [row, col] = this.getRowAndColFromID(cell.id)

                if (lastCell) {
                    const [row2, col2] = lastCell
                    const angle = Math.round(180 * Math.atan((row - row2) / (col - col2)) / Math.PI)
                    this.legend.style.transform = `rotate(${angle}deg)`
                }

                const centerCell = this.getCell(this.getCellID(
                    Math.floor((cumCell[0] += row) / count),
                    Math.floor((cumCell[1] += col) / count)
                ))

                cell.style.backgroundColor = backgroundColor
                // centerCell.style.backgroundColor = 'Orange'

                await new Promise(resolve => setTimeout(resolve, 700))

                if (count > 11) {
                    const [cell, backgroundImg] = paintings[count - 12]
                    // cell.style.backgroundColor = "Orange"
                    lastCell = this.getRowAndColFromID(cell.id)
                }
            }
        }

        for (let cell of this.cells) {
            cell.addEventListener('click', listener)
            cell.addEventListener('mouseover', (event) => {
                this.header.innerText = this.getRowAndColFromID(event.target.id)
            })
        }

        return this
    }


}
