

let table, data, rawFile

rawFile = new XMLHttpRequest()
rawFile.open("GET", "out99.txt", false)


rawFile.onreadystatechange = function () {
    data = rawFile.responseText.split('\n')
    const [height, width, channels] = data.slice(-2)[0].split(' ')
    table = new Table(height, width, data)

    table.spots.forEach(function (spot) {
        const [r, c] = table.getRowAndColFromID(spot)

        let angle = 0
        let spotCount = 0
        for (let rOff = -3; rOff <= 3; rOff++) {
            for (let cOff = -3; cOff <= 3; cOff++) {

                const newSpot = table.getCellID(r + rOff, c + cOff)
                angle += mod(Math.atan2(cOff, rOff), Math.pi)
                spotCount++
            }
        }

        const finalAngle = digitize()
    })
}

rawFile.send(null);
