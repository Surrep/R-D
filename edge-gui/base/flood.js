
function flood(region, r, c, dir = "", acc = []) {
    const id = region.getCellID(r, c)

    if (Number(region.data[id]) && !region.visited.has(id)) {

        if (dir) {
            const cell = region.getCell(id)

            if (cell) acc.push([cell, `url(${dir}.png)`])
        }
        region.visited.add(id)

        result = flood(region, r - 1, c - 1, "diag-left-color", acc)
        result = flood(region, r - 1, c, "up-down-color", acc)
        result = flood(region, r - 1, c + 1, "diag-right-color", acc)

        result = flood(region, r, c - 1, "left-right-color", acc)
        result = flood(region, r, c + 1, "left-right-color", acc)

        result = flood(region, r + 1, c - 1, "diag-right-color", acc)
        result = flood(region, r + 1, c, "up-down-color", acc)
        result = flood(region, r + 1, c + 1, "diag-left-color", acc)
    }

    return acc
}
