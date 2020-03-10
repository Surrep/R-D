function randint(low, high) {
    return Math.floor((high - low) * Math.random() + low)
}

async function audioread(path) {
    const response = await fetch(path)
    const arrayBuffer = await response.arrayBuffer()
    const audioBuffer = await new AudioContext().decodeAudioData(arrayBuffer)

    return audioBuffer.getChannelData(0)
}

function sample(k, n) {
    return [
        Math.cos(2 * Math.PI * k * n / 20000),
        -Math.sin(2 * Math.PI * k * n / 20000)
    ]
}

export default async function () {
    const canvas = document.getElementById('main')
    canvas.width = this.innerWidth
    canvas.height = this.innerHeight

    this.board = new RenderBoard(canvas, {
        x: this.innerWidth / 2,
        y: this.innerHeight / 2
    })


    this.data = await audioread('act.wav')
    this.data = this.data.slice(600)

    let n = 0
    const points = [
        [
            this.board.origin.x,
            this.board.origin.y,
        ]
    ]

    const sum = [0, 0]

    this.board.context.beginPath()
    this.board.context.moveTo(this.board.origin.x, this.board.origin.y)

    this.board.animate(function (tick) {
        const coords = sample(100, n)


        points[n] = [
            coords[0] * 1000 * data[n] + this.board.origin.x,
            coords[1] * 1000 * data[n] + this.board.origin.y,
        ]

        this.board.context.lineTo(points[n][0], points[n][1])
        this.board.context.moveTo(points[n][0], points[n][1])
        this.board.context.stroke()

        sum[0] += coords[0]
        sum[1] += coords[1]

        if (!(n % 100))
            console.log(n, sum)

        n++

    }.bind(this))
}

class Animator {
    animate(callback) {
        requestAnimationFrame(function animator(time) {
            callback(time)

            requestAnimationFrame(animator)
        })
    }
}

class SketchBoard extends Animator {
    constructor(canvas, origin) {
        super()

        this.cursor = {}
        this.canvas = canvas
        this.origin = origin
        this.context = this.canvas.getContext('2d')
    }

    pointermove(event) {
        this.cursor.x = event.x - this.origin.x
        this.cursor.y = this.origin.y - event.y
    }
}

class RenderBoard extends Animator {
    constructor(canvas, origin) {
        super()

        this.canvas = canvas
        this.origin = origin
        this.context = this.canvas.getContext('2d')
    }
}
