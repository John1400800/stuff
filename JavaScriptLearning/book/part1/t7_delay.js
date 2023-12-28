/*
function showAlert() {
  alert("moo");
}

let timeoutID = setTimeout(showAlert, 5000);
clearTimeout(timeoutID);
*/
/*
Если вы вообще не планируете отменять установленный таймер,
можете использовать setTimeout напрямую, не прибегая к инициализации
переменной.
*/

// также есть функци setInterval

let thingToPrint = '';

function drowText() {
    thingToPrint += '#';
    document.writeln(thingToPrint);
}

let intervalID = setInterval(drowText, 2000);
clearInterval(intervalID);
