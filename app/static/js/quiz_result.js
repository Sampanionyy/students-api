let showingAll = false;

function toggleReview() {
    const content = document.getElementById('reviewContent');
    const toggleText = document.getElementById('toggleText');
    const items = content.querySelectorAll('.answer-item');

    showingAll = !showingAll;

    if (showingAll) {
        items.forEach(item => item.style.display = 'block');
        toggleText.textContent = 'Masquer les correctes';
    } else {
        items.forEach(item => {
            if (item.classList.contains('correct')) {
                item.style.display = 'none';
            }
        });
        toggleText.textContent = 'Afficher tout';
    }
}

// Initially hide correct answers
window.addEventListener('load', () => {
    const items = document.querySelectorAll('.answer-item.correct');
    items.forEach(item => item.style.display = 'none');
});