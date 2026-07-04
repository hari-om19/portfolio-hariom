document.addEventListener('DOMContentLoaded', () => {
    const learnMoreBtn = document.getElementById('learnMoreBtn');
    const learningContent = document.getElementById('learningContent');

    learnMoreBtn.addEventListener('click', () => {
        // Toggle the visibility state class
        learningContent.classList.toggle('show');
        learnMoreBtn.classList.toggle('active');
    });
});