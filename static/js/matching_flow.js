/**
 * JOB SCOUT: Matching Flow & Scanning Animations
 * This script handles the visual transition of jobs as they enter the viewport.
 */

document.addEventListener('DOMContentLoaded', () => {
    const jobCards = document.querySelectorAll('.job-card');
    
    // 1. Intersection Observer for "Flowing" effect
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const jobObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Add a staggered delay based on the card index
                setTimeout(() => {
                    entry.target.classList.add('flow-visible');
                    simulateScanning(entry.target);
                }, index * 100); 
                
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    jobCards.forEach(card => jobObserver.observe(card));
});

/**
 * Simulates the "AI Scanning" visual on a job card
 */
function simulateScanning(card) {
    const scanLine = document.createElement('div');
    scanLine.className = 'scan-line';
    card.appendChild(scanLine);

    // Remove the scan line after the animation completes
    setTimeout(() => {
        scanLine.remove();
        const matchBadge = card.querySelector('.match-percentage');
        if (matchBadge) {
            matchBadge.style.opacity = '1';
            matchBadge.classList.add('pulse-glow');
        }
    }, 2000);
}

/**
 * Handles the "Automatic Apply" toggle flow
 */
function toggleAutoApply(jobId) {
    const btn = document.getElementById(`apply-btn-${jobId}`);
    btn.innerHTML = '<span>Scanning DNA...</span>';
    btn.classList.add('scanning-active');

    // Simulate backend processing delay
    setTimeout(() => {
        fetch(`/jobs/apply/${jobId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ is_automated: true })
        })
        .then(res => res.json())
        .then(data => {
            if (data.status === 'success') {
                btn.innerHTML = '✓ Applied Automatically';
                btn.className = 'btn-applied-glow';
            }
        });
    }, 1500);
}