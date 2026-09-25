async function updateStats() {
    const response = await fetch('/api/stats');
    const data = await response.json();

    document.getElementById('cpu_usage').innerText = "Usage: " + data.cpu_usage;
    document.getElementById('ram-total').innerText = "Total: " + data.total_ram;
    document.getElementById('ram-available').innerText = "Available: " + data.available_ram;
    document.getElementById('ram-used').innerText = "Used: " + data.used_ram;
    document.getElementById('ram-usage').innerText = "Usage: " + data.ram_usage;
}

document.addEventListener('DOMContentLoaded', () => {
    updateStats();
    setInterval(() => {
        updateStats();
    }, 1000);
})