function colorMe() {
    var colorchoose = randomIntFromInterval(1, 3);
    switch (colorchoose) {
        case 1:
            document.body.style.backgroundColor = "#0099ff";
            break;

        case 2:
            document.body.style.backgroundColor = "#ff6600";
            break;
            //case 3:
            //document.body.style.backgroundColor = "#ff00ff"; 
        case 3:
            document.body.style.backgroundColor = "#666699";
            break;
    }
}


function randomIntFromInterval(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

colorMe();