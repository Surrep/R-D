
function startFlood(set, r, c) {
    const id = Table.getPixelID(r, c, 28)

    if (cells[id] && !set.has(id)) {

        Table.getCell(id).style.backgroundColor = 'aqua'
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
