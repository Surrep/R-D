
const colors = ['aqua', 'magenta', 'green', 'red', 'blue', 'orange', 'yellow', 'brown']

function randomColor() {
    return colors[Math.floor(Math.random() * colors.length)]
}

function mod(n, m) {
    return ((n % m) + m) % m
}

function digitize(num, markers) {
    for (let i = 1; i < markers.length; i++) {
        const m1 = markers[i - 1]
        const m2 = markers[i]

        if (num <= m1) return i - 1
        if (num <= m2) return i
    }

    return markers.length
}