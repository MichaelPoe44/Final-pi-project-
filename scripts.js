let enteredPasscode = '';

function enterDigit(digit) {
    enteredPasscode += digit;
    document.getElementById('password').value = enteredPasscode;
}

function clearPasscode() {
    enteredPasscode = '';
    document.getElementById('password').value = '';
}

const correctPassword = '1234';  // In real applications, handle this securely on the server side

function checkPassword() {
    if (enteredPasscode === correctPassword) {
        alert('Phone unlocked!');
        enteredPasscode = '';
        document.getElementById('password').value = '';
    } else {
        alert('Incorrect password!');
        enteredPasscode = '';
        document.getElementById('password').value = '';
    }
}

function updateTime() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const timeStr = hours + ':' + minutes;
    const dateStr = now.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' });

    document.getElementById('time').textContent = timeStr;
    document.getElementById('date').textContent = dateStr;
}

setInterval(updateTime, 1000);
updateTime();
