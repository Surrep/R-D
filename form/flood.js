
function flood(region, r, c, dir = "") {
    const id = region.getCellID(r, c)

    if (region.data[id] && !region.visited.has(id)) {

        region.getCell(id).style.backgroundColor = region.color
        region.visited.add(id)

        console.log(r, c, dir)
        flood(region, r - 1, c - 1, "\\")
        flood(region, r - 1, c, "|")
        flood(region, r - 1, c + 1, "/")

        flood(region, r, c - 1, "-")
        flood(region, r, c + 1, "-")

        flood(region, r + 1, c - 1, "/")
        flood(region, r + 1, c, "|")
        flood(region, r + 1, c + 1, "\\")
    }
}
