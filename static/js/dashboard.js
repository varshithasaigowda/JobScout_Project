/**
 * JOB SCOUT: Dashboard Visualizations
 * Powers the Radar Skill Map and the Trust Gauge.
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Skill Map (Radar Chart)
    const skillCtx = document.getElementById('skillMap').getContext('2d');
    
    new Chart(skillCtx, {
        type: 'radar',
        data: {
            labels: ['Technical', 'Logic', 'Exp', 'Reliability', 'Stack Depth'],
            datasets: [{
                label: 'Professional DNA',
                data: [85, 92, 78, 95, 88], // These would be dynamic in production
                backgroundColor: 'rgba(209, 131, 169, 0.2)', // Middle Purple
                borderColor: '#D183A9',
                borderWidth: 2,
                pointBackgroundColor: '#F3C8DD', // Queen Pink
                pointHoverRadius: 5
            }]
        },
        options: {
            scales: {
                r: {
                    angleLines: { color: 'rgba(255, 255, 255, 0.1)' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' },
                    pointLabels: { color: '#F3C8DD', font: { size: 12 } },
                    ticks: { display: false, max: 100 }
                }
            },
            plugins: { legend: { display: false } },
            responsive: true,
            maintainAspectRatio: false
        }
    });

    // 2. Trust Gauge (Semi-Circle Doughnut)
    const trustCtx = document.getElementById('trustGauge').getContext('2d');
    const trustScore = parseInt(document.querySelector('.trust-value')?.innerText) || 75;

    new Chart(trustCtx, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [trustScore, 100 - trustScore],
                backgroundColor: [
                    '#BA71A2', // Pearly Purple
                    'rgba(255, 255, 255, 0.05)'
                ],
                borderWidth: 0,
                circumference: 180,
                rotation: 270,
                borderRadius: 10
            }]
        },
        options: {
            cutout: '85%',
            responsive: true,
            maintainAspectRatio: false,
            plugins: { tooltip: { enabled: false } }
        }
    });
});