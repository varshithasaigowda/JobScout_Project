/**
 * JOB SCOUT: Application Flow Logic
 * Handles button states and real-time application feedback.
 */

async function toggleAutoApply(jobId) {
    const btn = document.getElementById(`apply-btn-${jobId}`);
    const isAutomated = document.querySelector(`#auto-check-${jobId}`)?.checked || false;

    // 1. Loading State (Visual DNA Handshake)
    btn.disabled = true;
    btn.style.cursor = 'wait';
    const originalText = btn.innerHTML;
    btn.innerHTML = '<span class="loading-spinner"></span> Delivering DNA...';

    try {
        const response = await fetch(`/jobs/apply/${jobId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ is_automated: isAutomated })
        });

        const data = await response.json();

        if (data.status === 'success') {
            // 2. Success State: Transform button to "Delivered"
            btn.innerHTML = '✓ Application Delivered';
            btn.style.background = 'linear-gradient(45deg, #50C878, #2E8B57)'; // Emerald Green
            btn.style.boxShadow = '0 0 20px rgba(80, 200, 120, 0.4)';
            
            showToast("Success", "Your Professional DNA has been successfully scanned and delivered.", "success");
        } else if (data.status === 'already_applied') {
            btn.innerHTML = 'Already Applied';
            showToast("Note", "You have already applied for this role.", "info");
        }
    } catch (error) {
        btn.innerHTML = 'Error';
        btn.disabled = false;
        showToast("Error", "Connection failed. Please try again.", "error");
    }
}

/**
 * Creates a floating Glassmorphic Toast notification
 */
function showToast(title, message, type) {
    const toast = document.createElement('div');
    toast.className = 'glass-card toast-notification';
    toast.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        padding: 20px;
        z-index: 9999;
        border-left: 5px solid ${type === 'success' ? '#50C878' : '#D183A9'};
        animation: slideInLeft 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    `;
    
    toast.innerHTML = `
        <strong style="color: var(--queen-pink); display: block;">${title}</strong>
        <span style="font-size: 0.9rem; color: white;">${message}</span>
    `;

    document.body.appendChild(toast);

    setTimeout(() => {
        toast.style.animation = 'slideOutRight 0.5s forwards';
        setTimeout(() => toast.remove(), 500);
    }, 4000);
}