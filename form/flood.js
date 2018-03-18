
function startFlood(region, r, c, dir) {
    const id = region.getPixelID(r, c)

    if (region.data[id] && !region.visited.has(id)) {

        region.getCell(id).style.backgroundColor = 'aqua'
        region.visited.add(id)
        console.log(dir)

        startFlood(region, r - 1, c - 1, "\\")
        startFlood(region, r - 1, c, "|")
        startFlood(region, r - 1, c + 1, "/")

        startFlood(region, r, c - 1, "-")
        startFlood(region, r, c + 1, "-")

        startFlood(region, r + 1, c - 1, "/")
        startFlood(region, r + 1, c, "|")
        startFlood(region, r + 1, c + 1, "\\")
    }
}
