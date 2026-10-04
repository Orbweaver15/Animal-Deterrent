const keys = {w: false, a: false, s: false, d: false};

function handleKey(key, isPressed) {
    const element = document.getElementById(key);
    element.classList.toggle('active', isPressed);
    fetch(`/${key}/${isPressed ? 'press' : 'release'}`)
        .catch(err => console.log('Command failed:', err));
}

// Mouse events
document.querySelectorAll('.key').forEach(btn => {
    btn.addEventListener('mousedown', () => handleKey(btn.id, true));
    btn.addEventListener('mouseup', () => handleKey(btn.id, false));
    btn.addEventListener('mouseleave', () => {
        if (keys[btn.id]) handleKey(btn.id, false);
    });
});

// Keyboard events
document.addEventListener('keydown', (e) => {
    const key = e.key.toLowerCase();
    if (['w','a','s','d'].includes(key) && !keys[key]) {
        keys[key] = true;
        handleKey(key, true);
    }
});

document.addEventListener('keyup', (e) => {
    const key = e.key.toLowerCase();
    if (['w','a','s','d'].includes(key)) {
        keys[key] = false;
        handleKey(key, false);
    }
});

// Prevent context menu on long press
document.addEventListener('contextmenu', (e) => e.preventDefault());
