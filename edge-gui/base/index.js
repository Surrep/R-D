const rawFile = new XMLHttpRequest();
rawFile.open("GET", "a.txt", false);

rawFile.onreadystatechange = function () {
    const cells = rawFile.responseText.split('\n')
    const [height, width, channels] = cells.slice(-2)[0].split(' ')
    const table = new Table(height, width, cells).addListener(flood)
}

rawFile.send(null);
