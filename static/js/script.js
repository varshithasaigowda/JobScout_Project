/* ------------------------------------ */
/*  SMOOTH SCROLLING                     */
/* ------------------------------------ */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

/* ------------------------------------ */
/*  HERO ANIMATION ON SCROLL             */
/* ------------------------------------ */
const hero = document.querySelector('.hero');
if (hero) {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                hero.classList.add('fadeIn');
            }
        });
    }, { threshold: 0.1 });
    observer.observe(hero);
}

/* ------------------------------------ */
/*  CARD HOVER EFFECT (SCALE + SHADOW)  */
/* ------------------------------------ */
const cards = document.querySelectorAll('.card, .job-card, .dashboard-card');
cards.forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.transform = 'translateY(-4px)';
        card.style.boxShadow = '0 12px 40px rgba(0,0,0,0.35)';
    });
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0)';
        card.style.boxShadow = '0 8px 32px rgba(0,0,0,0.25)';
    });
});

/* ------------------------------------ */
/*  BUTTON INTERACTIONS                  */
/* ------------------------------------ */
const buttons = document.querySelectorAll('button');
buttons.forEach(btn => {
    btn.addEventListener('mouseenter', () => {
        btn.style.opacity = '0.85';
        btn.style.transform = 'translateY(-2px)';
    });
    btn.addEventListener('mouseleave', () => {
        btn.style.opacity = '1';
        btn.style.transform = 'translateY(0)';
    });
});

/* ------------------------------------ */
/*  SCROLL TO TOP BUTTON                 */
/* ------------------------------------ */
const scrollBtn = document.createElement('button');
scrollBtn.textContent = '⬆';
scrollBtn.className = 'scroll-top';
scrollBtn.style.position = 'fixed';
scrollBtn.style.bottom = '30px';
scrollBtn.style.right = '30px';
scrollBtn.style.padding = '12px 16px';
scrollBtn.style.borderRadius = '50%';
scrollBtn.style.border = 'none';
scrollBtn.style.background = 'linear-gradient(90deg, #22d3ee, #8b5cf6)';
scrollBtn.style.color = '#000';
scrollBtn.style.cursor = 'pointer';
scrollBtn.style.display = 'none';
scrollBtn.style.zIndex = '1000';
document.body.appendChild(scrollBtn);

scrollBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        scrollBtn.style.display = 'block';
    } else {
        scrollBtn.style.display = 'none';
    }
});

/* ------------------------------------ */
/*  TOOLTIP INTERACTION                  */
/* ------------------------------------ */
const tooltipElems = document.querySelectorAll('[data-tooltip]');
tooltipElems.forEach(elem => {
    elem.addEventListener('mouseenter', () => {
        let tooltip = document.createElement('span');
        tooltip.className = 'tooltip';
        tooltip.textContent = elem.dataset.tooltip;
        tooltip.style.position = 'absolute';
        tooltip.style.background = 'rgba(0,0,0,0.8)';
        tooltip.style.color = '#fff';
        tooltip.style.padding = '6px 10px';
        tooltip.style.borderRadius = '8px';
        tooltip.style.fontSize = '12px';
        tooltip.style.whiteSpace = 'nowrap';
        tooltip.style.pointerEvents = 'none';
        tooltip.style.transition = 'opacity 0.3s';
        tooltip.style.opacity = '0';
        document.body.appendChild(tooltip);

        const rect = elem.getBoundingClientRect();
        tooltip.style.top = `${rect.top - rect.height}px`;
        tooltip.style.left = `${rect.left}px`;

        setTimeout(() => tooltip.style.opacity = '1', 10);

        elem.addEventListener('mouseleave', () => {
            tooltip.style.opacity = '0';
            setTimeout(() => tooltip.remove(), 300);
        }, { once: true });
    });
});
