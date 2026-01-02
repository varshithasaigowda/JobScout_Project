/* ------------------------------------ */
/*  RADAR CHART FOR SKILLS               */
/* ------------------------------------ */
// Make sure Chart.js is included in your base.html via CDN:
// <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

const skillDataElem = document.getElementById('skillChart');
if (skillDataElem) {
    const ctx = skillDataElem.getContext('2d');

    // Sample skill values; replace dynamically via Flask/Jinja
    const skills = skillDataElem.dataset.skills ? JSON.parse(skillDataElem.dataset.skills) : {
        "Python": 80,
        "JavaScript": 70,
        "SQL": 60,
        "Machine Learning": 50,
        "Communication": 75,
        "Problem Solving": 65
    };

    const labels = Object.keys(skills);
    const data = Object.values(skills);

    const radarChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Skill Map',
                data: data,
                fill: true,
                backgroundColor: 'rgba(139, 92, 246, 0.2)', // Purple glass effect
                borderColor: 'rgba(139, 92, 246, 1)',
                pointBackgroundColor: 'rgba(139, 92, 246, 1)',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: 'rgba(139, 92, 246, 1)'
            }]
        },
        options: {
            responsive: true,
            scales: {
                r: {
                    angleLines: { color: 'rgba(255,255,255,0.1)' },
                    grid: { color: 'rgba(255,255,255,0.1)' },
                    suggestedMin: 0,
                    suggestedMax: 100,
                    ticks: {
                        color: '#fff',
                        backdropColor: 'transparent'
                    },
                    pointLabels: {
                        color: '#fff',
                        font: { size: 14 }
                    }
                }
            },
            plugins: {
                legend: { labels: { color: '#fff' } }
            }
        }
    });
}

/* ------------------------------------ */
/*  TRUST SCORE ANIMATION                */
/* ------------------------------------ */
const trustScoreElem = document.getElementById('trustScore');
if (trustScoreElem) {
    const score = parseFloat(trustScoreElem.dataset.score) || 0;
    let current = 0;

    const interval = setInterval(() => {
        if (current < score) {
            current += 0.5; // speed of increment
            trustScoreElem.textContent = current.toFixed(1) + '%';
        } else {
            trustScoreElem.textContent = score.toFixed(1) + '%';
            clearInterval(interval);
        }
    }, 20);
}
