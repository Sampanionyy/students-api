let selectedStudent = null;
let selectedCategory = null;

// Student selection
document.getElementById('studentSelect').addEventListener('change', function(e) {
    selectedStudent = e.target.value;
    updateStartButton();
});

// Category selection
document.querySelectorAll('.category-card').forEach(card => {
    card.addEventListener('click', function() {
        document.querySelectorAll('.category-card').forEach(c => c.classList.remove('selected'));
        this.classList.add('selected');
        selectedCategory = this.dataset.category;
        updateStartButton();
    });
});

// Update start button state
function updateStartButton() {
    const startButton = document.getElementById('startButton');
    if (selectedStudent && selectedCategory) {
        startButton.disabled = false;
    } else {
        startButton.disabled = true;
    }
}

// Start quiz
document.getElementById('startButton').addEventListener('click', function() {
    if (selectedStudent && selectedCategory) {
        window.location.href = `/quiz/play/${selectedCategory}?student_id=${selectedStudent}`;
    }
});