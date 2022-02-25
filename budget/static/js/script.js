let amounts = document.getElementsByClassName("col-amount");
let types = document.getElementsByClassName("col-type");
let balance = document.getElementById("balance");

// Change operations amounts Colors
for (let i = 0; i < amounts.length; i++) {
    console.log(amounts[i].textContent);
    console.log(types[i].textContent);
    let cellAmount = amounts[i];
    let cellType = types[i];
    if (cellType.textContent === "Débit") {
        cellAmount.style.color = "red"
    } else {
        cellAmount.style.color = "green"
    }
}

// Change Balance Color

balanceFloat = parseFloat(balance.textContent);
console.log(balanceFloat);
if (balanceFloat < 0) {
    balance.style.color = "red";
} else {
    balance.style.color = "green";
}