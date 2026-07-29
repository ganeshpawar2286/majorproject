document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const button = document.querySelector('button[type="submit"]');

    if (form && button) {
        form.addEventListener('submit', () => {
            button.textContent = 'Analyzing...';
            button.disabled = true;
        });
    }
});
