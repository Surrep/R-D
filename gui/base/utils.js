
const CSS_COLOR_NAMES = ["AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque", "Black", "BlanchedAlmond", "Blue", "BlueViolet", "Brown", "BurlyWood", "CadetBlue", "Chartreuse", "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson", "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGray", "DarkGrey", "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "Darkorange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray", "DarkSlateGrey", "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DimGrey", "DodgerBlue", "FireBrick", "FloralWhite", "ForestGreen", "Fuchsia", "Gainsboro", "GhostWhite", "Gold", "GoldenRod", "Gray", "Grey", "Green", "GreenYellow", "HoneyDew", "HotPink", "IndianRed", "Indigo", "Ivory", "Khaki", "Lavender", "LavenderBlush", "LawnGreen", "LemonChiffon", "LightBlue", "LightCoral", "LightCyan", "LightGoldenRodYellow", "LightGray", "LightGrey", "LightGreen", "LightPink", "LightSalmon", "LightSeaGreen", "LightSkyBlue", "LightSlateGray", "LightSlateGrey", "LightSteelBlue", "LightYellow", "Lime", "LimeGreen", "Linen", "Magenta", "Maroon", "MediumAquaMarine", "MediumBlue", "MediumOrchid", "MediumPurple", "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed", "MidnightBlue", "MintCream", "MistyRose", "Moccasin", "NavajoWhite", "Navy", "OldLace", "Olive", "OliveDrab", "Orange", "OrangeRed", "Orchid", "PaleGoldenRod", "PaleGreen", "PaleTurquoise", "PaleVioletRed", "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum", "PowderBlue", "Purple", "Red", "RosyBrown", "RoyalBlue", "SaddleBrown", "Salmon", "SandyBrown", "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue", "SlateGray", "SlateGrey", "Snow", "SpringGreen", "SteelBlue", "Tan", "Teal", "Thistle", "Tomato", "Turquoise", "Violet", "Wheat", "White", "WhiteSmoke", "Yellow", "YellowGreen"];


function getColorPallete(num) {
    return new Array(num).fill(null).map(randomColor)
}

function randomColor() {
    return CSS_COLOR_NAMES[Math.floor(Math.random() * CSS_COLOR_NAMES.length)]
}

function mod(n, m) {
    return ((n % m) + m) % m
}

function digitize(num, markers) {
    markers = markers.sort()

    for (let i = 1; i < markers.length; i++) {
        const m1 = markers[i - 1]
        const m2 = markers[i]

        if (num <= m1) return i - 1
        if (num <= m2) return i
    }

    return markers.length
}

function linspace(start, end, steps) {
    const arr = []
    const step = (end - start) / (steps - 1)

    for (let n = start; n.toFixed(5) !== end.toFixed(5); n += step)
        arr.push(n)

    arr.push(end)
    return arr
}

function drawBox(table, r, c, bound) {
    const cells = []
    for (let off = -bound; off < bound; off++) {

        const topCell = table.getCell(table.getCellID(r - bound, c + off))
        const botCell = table.getCell(table.getCellID(r + bound, c + off))
        const lefCell = table.getCell(table.getCellID(r + off, c - bound))
        const rigCell = table.getCell(table.getCellID(r + off, c + bound))

        cells.push(
            [topCell, topCell.style.backgroundColor.slice()],
            [botCell, botCell.style.backgroundColor.slice()],
            [lefCell, lefCell.style.backgroundColor.slice()],
            [rigCell, rigCell.style.backgroundColor.slice()]
        )

        topCell.style.backgroundColor = 'Orange'
        botCell.style.backgroundColor = 'Orange'
        lefCell.style.backgroundColor = 'Orange'
        rigCell.style.backgroundColor = 'Orange'
    }


    return cells
}

function eraseCells(cells) {
    cells.forEach(function (cellInfo) {
        const [cell, color] = cellInfo
        cell.style.backgroundColor = color
    })
}

function mode(array) {
    let mostNumerous = 0
    const occurences = {}

    for (const element of array) {
        occurences[element] = occurences[element] || 0
        occurences[element]++

        if (occurences[element] > mostNumerous)
            mostNumerous = element
    }

    return mostNumerous
}

function floorMean(array) {
    return Math.floor(
        array.reduce(function (sum, element) {
            return sum + element
        }) / array.length
    )
}
