let sum = 0
const dx = 0.000001
const f = x => 2 * x
for (let i = 0; i <= 5.5; i += dx) {
    sum += dx * f(i)
}

console.log(sum)
