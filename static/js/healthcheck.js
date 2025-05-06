const checkBtn = document.getElementById('checkBtn');
const loadingDiv = document.getElementById('loading');
const statusDiv = document.getElementById('status');
const statusText = document.getElementById('statusText');
const iconSvg = document.getElementById('icon');
const responseTimeSpan = document.getElementById('responseTime');

const ICONS = {
  success: `
    <path d="M9 16.2l-3.5-3.5 1.41-1.41L9 13.38l7.09-7.09 1.41 1.41z"/>
  `,
  error: `
    <path d="M18.3 5.71l-1.41-1.41L12 9.59 7.11 4.7 5.7 6.11 10.59 11 5.7 15.89l1.41 1.41L12 12.41l4.89 4.89 1.41-1.41L13.41 11z"/>
  `
};

function setStatus(success, time = null, errorMsg = null) {
  if (success) {
    statusDiv.classList.remove('error');
    statusText.textContent = 'Activo';
    iconSvg.innerHTML = ICONS.success;
    responseTimeSpan.textContent = time !== null ? `(${time} ms)` : '';
  } else {
    statusDiv.classList.add('error');
    statusText.textContent = 'Error';
    iconSvg.innerHTML = ICONS.error;
    responseTimeSpan.textContent = errorMsg ? `- ${errorMsg}` : '';
  }
  statusDiv.classList.remove('hidden');
}

async function doHealthcheck() {
  checkBtn.disabled = true;
  checkBtn.setAttribute('aria-busy', 'true');
  statusDiv.classList.add('hidden');
  loadingDiv.classList.remove('hidden');
  responseTimeSpan.textContent = '';

  const start = performance.now();

  try {
    const res = await fetch('/api/piratear-eltoque');

    const end = performance.now();
    const duration = Math.round(end - start);

    if (!res.ok) {
      setStatus(false, null, `HTTP ${res.status}`);
    } else {
      setStatus(true, duration);
    }
  } catch (err) {
    setStatus(false, null, err.message);
  } finally {
    loadingDiv.classList.add('hidden');
    checkBtn.disabled = false;
    checkBtn.setAttribute('aria-busy', 'false');
  }
}

checkBtn.addEventListener('click', doHealthcheck);

window.addEventListener('load', doHealthcheck);
