let counterValue = document.getElementById("counter-number");

function clickAdd(parameters) {
    let previousValue = counterValue.textContent;
    let updatedValue = parseInt(previousValue) + 1;
    document.getElementById("counter-number").textContent = (updatedValue);
}

function clickReset(parameters) {
    document.getElementById("counter-number").textContent = 0;
}

function clickLess(parameters) {
    let previousValue = counterValue.textContent;
    let updatedValue = parseInt(previousValue) - 1;
    document.getElementById("counter-number").textContent = (updatedValue);
}

