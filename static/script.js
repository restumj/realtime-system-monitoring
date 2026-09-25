async function updateStats() {
    const response = await fetch('/api/stats');
    const data = await response.json();

    document.getElementById('cpu').innerText = data.cpu_usage;
    document.getElementById('ram').innerText = data.used_ram;
}

document.addEventListener('DOMContentLoaded', (event) => {
    setInterval(() => {
        updateStats();
    }, 1000);
})