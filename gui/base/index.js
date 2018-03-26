

let table, data, rawFile

rawFile = new XMLHttpRequest()
rawFile.open("GET", "a.txt", false)

angle_bin_count = 12
angles = linspace(Math.PI, 0, angle_bin_count)
colors = getColorPallete(angle_bin_count + 1)

rawFile.onreadystatechange = async function () {
    data = rawFile.responseText.split('\n')
    const [height, width, channels] = data.slice(-2)[0].split(' ')
    table = new Table(height, width, data)

    for (const spot of table.spots) {
        const [r, c] = table.getRowAndColFromID(spot)

        let angle = 0
        let spotCount = 0
        const cells = []
        for (let rOff = -3; rOff <= 3; rOff++) {
            for (let cOff = -3; cOff <= 3; cOff++) {
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
            console.log(angle / spotCount)
            await new Promise(resolve => setTimeout(resolve, 10));

            for (const cell of cells) {
                cell.style.backgroundColor = colors[finalAngle]
            }
        }

    }




}

rawFile.send(null);
