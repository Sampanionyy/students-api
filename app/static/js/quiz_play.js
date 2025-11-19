// Timer configuration (2 minutes = 120 seconds)
let timeLeft = 120;
let timerInterval;
const totalQuestions = parseInt("{{ total_questions }}");

// Format time display
function formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}

// Update timer display
function updateTimer() {
    const timerElement = document.getElementById('timer');
    timerElement.textContent = formatTime(timeLeft);

    // Warning state when less than 30 seconds
    if (timeLeft <= 30) {
        timerElement.classList.add('warning');
    }

    // Time's up
    if (timeLeft <= 0) {
        clearInterval(timerInterval);
        showTimeUpModal();
        setTimeout(() => {
            document.getElementById('quizForm').submit();
        }, 2000);
    }

    timeLeft--;
}

// Show time's up modal
function showTimeUpModal() {
    document.getElementById('timeUpModal').classList.add('show');
}

// Update progress
function updateProgress() {
    const form = document.getElementById('quizForm');
    const answeredQuestions = new Set();
    
    // Count unique answered questions
    const inputs = form.querySelectorAll('input[type="radio"]:checked');
    inputs.forEach(input => {
        answeredQuestions.add(input.name);
    });

    const count = answeredQuestions.size;
    const percentage = (count / totalQuestions) * 100;

    document.getElementById('answeredCount').textContent = count;
    document.getElementById('currentQuestion').textContent = count;
    document.getElementById('progressFill').style.width = percentage + '%';
}

// Start timer when page loads
window.addEventListener('load', () => {
    updateTimer(); // Initial display
    timerInterval = setInterval(updateTimer, 1000);
    updateProgress(); // Initial progress
});

// Prevent form submission without confirmation
document.getElementById('quizForm').addEventListener('submit', (e) => {
    const form = e.target;
    const answeredQuestions = new Set();
    
    const inputs = form.querySelectorAll('input[type="radio"]:checked');
    inputs.forEach(input => {
        answeredQuestions.add(input.name);
    });

    if (answeredQuestions.size < totalQuestions) {
        if (!confirm(`Vous n'avez répondu qu'à ${answeredQuestions.size} questions sur ${totalQuestions}. Voulez-vous vraiment soumettre ?`)) {
            e.preventDefault();
        }
    }
});

// Warn before leaving page
window.addEventListener('beforeunload', (e) => {
    e.preventDefault();
    e.returnValue = '';
});