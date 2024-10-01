function validateInput(inputId, maxValue) {
    const input = document.getElementById(inputId);
    input.addEventListener('input', function(event) {
        const inputValue = parseFloat(event.target.value);
        if (inputValue > maxValue) {
            alert(`输入值不能超过 ${maxValue}`);
            event.target.value = maxValue; // 将值重置为最大值
        }
    });
}

window.onload = function() {
    validateInput('playermax', 64);
    validateInput('thralls', 64);
    validateInput('dayminutes', 3);
    validateInput('daysbeforeblizzard', 3);
    validateInput('predatordamage', 3);
    validateInput('coalburnrate', 3);
    validateInput('hungerrate', 3);
    validateInput('coldintensity', 3);
};