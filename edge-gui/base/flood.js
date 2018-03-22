
function flood(region, r, c, color = "", acc = []) {
    const id = region.getCellID(r, c)

    if (Number(region.data[id]) && !region.visited.has(id)) {

        if (color) {
            const cell = region.getCell(id)
            if (cell) acc.push([cell, color])
        }

        region.visited.add(id)

        flood(region, r - 1, c - 1, "purple", acc)
        flood(region, r - 1, c, "green", acc)
        flood(region, r - 1, c + 1, "yellow", acc)

        flood(region, r, c - 1, "pink", acc)
        flood(region, r, c + 1, "pink", acc)

        flood(region, r + 1, c - 1, "yellow", acc)
        flood(region, r + 1, c, "green", acc)
        flood(region, r + 1, c + 1, "purple", acc)


    }

    return acc
}
