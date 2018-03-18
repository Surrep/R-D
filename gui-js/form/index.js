const canvas = document.createElement('canvas');
const context = canvas.getContext('2d');

const image = new Image()
image.src = 'http://localhost:3000/eee.jpg'
document.body.appendChild(image)

image.onload = function () {
    canvas.width = image.width;
    canvas.height = image.height;
    context.drawImage(image, 0, 0);
    const myData = context.getImageData(0, 0, image.width, image.height);
    console.log(myData)
}






// const table = new Table(28, 28, cells).addListener(flood)

