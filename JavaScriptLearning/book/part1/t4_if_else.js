// инсчтрукция if else
// if (something_is_true) {
//     do_something;
// } else {
//     do_something_different;
// }
let speedLimit = 55
// разбираюсь в функциях и условных операторах
function trafficLight(color) {
    let res;
    if (color == 'green') {
        res = 'go';
    } else if (color == 'yellow') {
        res = 'get ready';
    } else if (color == 'red') {
        res = 'stop';
    } else {
        res = 'up wipe your eyes';
    }
    return res;
}

function amISpeeding(speed) {
    if (speed >= speedLimit) {
        return 'Yes, you are speeding';
    } else {
        return 'No, You are not speeding. Whats wrong with you';
    }
}

// чуть более сложный пример if...else и условных операторов
function sendWarning(x, y) {
    let xPos = 300, yPos = 250;
    if ((x < xPos) && (y < yPos)) {
        return 'Adjust the position';
    } else {
        return 'Thing are fine!';
    }
}

// alert(sendWarning(500, 160));
// alert(sendWarning(100, 100));
// alert(sendWarning(201, 149));

// почти разобрались с if осталось
// лишь разобраться с её родствениками

// одиночная конструкция if:
if (weight > 5000) {
    alert('No free shipping for you!');
}

// вместо elif в python тут else if
if (position < 100) {
    alert('Do something!')
} else if ((position >= 200) && (position < 300)) {
    alert('Do thomething else!')
} else {
    alert('Do thomething even more different!')
}

// switch - что же это ? (тоже самое что и else if!)

let color = 'green';

switch (color) {
    case 'yellow':
        alert('yellow color');
        break;
    case 'red':
        alert('red color');
        break;
    case 'blue':
        alert('blue color');
        break;
    case 'green':
        alert('green color');
        break;
    case 'black':
        alert('black color');
        break;
    default:
        alert('no known color specified')
        break;
}

// допустим есть такая кл=онструкция if:
let num = 20;

if (num > 10) {
    alert('yes');
} else {
    alert('nope');
}
// преобразуем в switch

switch (num > 10) {
    case true:
        alert('yes');
        break;
    case false:
        alert('nope');
        break;
}
// если условия сложные то используем if else
// switch лучше когда вычисляете выражение и сопоставляете условия

// хоть сколько понятный пример if
let loginStatus = false;

if (name = 'Admin') {
    loginStatus = true;
}

// выборы основываются на условиях которые должны быть вычеслены как true или false

