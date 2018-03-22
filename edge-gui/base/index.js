let table, cells, rawFile

rawFile = new XMLHttpRequest();
rawFile.open("GET", "out99.txt", false);

rawFile.onreadystatechange = function () {
    cells = rawFile.responseText.split('\n')
    const [height, width, channels] = cells.slice(-2)[0].split(' ')
    table = new Table(height, width, cells).addListener(flood)
}

rawFile.send(null);
