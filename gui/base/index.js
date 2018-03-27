

let table, data, rawFile

rawFile = new XMLHttpRequest()
rawFile.open("GET", "arr.txt", false)

const angle_bin_count = 8
const angles = linspace(0, Math.PI, angle_bin_count)
const colors = getColorPallete(angle_bin_count + 1)
const recepSize = 2
const history = {}

rawFile.onreadystatechange = async function () {
    data = rawFile.responseText.split('\n')
    const [height, width, channels] = data.slice(-2)[0].split(' ')
    table = new Table(height, width, data)

    for (const spot of table.spots) {
        const [r, c] = table.getRowAndColFromID(spot)

        let angle = 0
        let spotCount = 0
        const cells = []

        for (let rOff = -recepSize; rOff <= recepSize; rOff++) {
            for (let cOff = -recepSize; cOff <= recepSize; cOff++) {
                const newSpot = table.getCellID(r + rOff, c + cOff)
                const cell = table.getCell(newSpot)

                if (Number(table.data[cell.id])) {
                    cells.push(cell)
                    table.spots.delete(newSpot)
                    angle += mod(Math.atan2(cOff, rOff), Math.PI)
                    spotCount++
                }
            }
        }

        if (spotCount) {
            const finalAngle = digitize(angle / spotCount, angles)
            const outline = drawBox(table, r, c, recepSize + 1)

            for (const cell of cells) {
                history[cell.id] = history[cell.id] || []
                history[cell.id].push(finalAngle)

                cell.style.backgroundColor = colors[mode(history[cell.id])]
                await new Promise(resolve => setTimeout(resolve));
            }

            eraseCells(outline)
        }

    }
}

rawFile.send(null);
