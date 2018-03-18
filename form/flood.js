
function flood(region, r, c, dir = "") {
    const id = region.getCellID(r, c)

    if (region.data[id] && !region.visited.has(id)) {

        region.getCell(id).style.backgroundImage = `url(/Users/tru/Desktop/photos/${dir}.png)`
        region.visited.add(id)

        console.log(r, c, dir)
        result = flood(region, r - 1, c - 1, "diag-left")
        result = flood(region, r - 1, c, "up-down")
        result = flood(region, r - 1, c + 1, "diag-right")

        result = flood(region, r, c - 1, "left-right")
        result = flood(region, r, c + 1, "left-right")

        result = flood(region, r + 1, c - 1, "diag-right")
        result = flood(region, r + 1, c, "up-down")
        result = flood(region, r + 1, c + 1, "diag-left")

    }

}
