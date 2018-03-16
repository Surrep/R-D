
function startFlood(set, r, c) {
    const id = getPixelID(r, c)

    if (cells[id] && !set.has(id)) {
        getCell(id).style.backgroundColor = 'white'
        set.add(id)

        startFlood(set, r - 1, c - 1)
        startFlood(set, r - 1, c)
        startFlood(set, r - 1, c + 1)

        startFlood(set, r, c - 1)
        startFlood(set, r, c + 1)

        startFlood(set, r + 1, c - 1)
        startFlood(set, r + 1, c)
        startFlood(set, r + 1, c + 1)
    }
}
