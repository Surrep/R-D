
function flood(region, r, c, dir = "") {
    const id = region.getCellID(r, c)

    if (region.data[id] && !region.visited.has(id)) {

        region.getCell(id).style.backgroundColor = region.color
        region.visited.add(id)

        let result = false
        console.log(r, c, dir)
        result = flood(region, r - 1, c - 1, "\\")
        if (result) return true
        result = flood(region, r - 1, c, "|")
        if (result) return true
        result = flood(region, r - 1, c + 1, "/")
        if (result) return true

        result = flood(region, r, c - 1, "-")
        if (result) return true
        result = flood(region, r, c + 1, "-")
        if (result) return true

        result = flood(region, r + 1, c - 1, "/")
        if (result) return true
        result = flood(region, r + 1, c, "|")
        if (result) return true
        result = flood(region, r + 1, c + 1, "\\")
        if (result) return true

        return true

    }

}
