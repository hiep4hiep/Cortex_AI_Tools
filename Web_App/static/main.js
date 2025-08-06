// Map tool to API endpoint (specify port for each container)
const apiMap = {
    dmgen: { url: '/api/query/dmgen/'},
    spl: { url: '/api/query/spl/'},
    ingestion: { url: '/api/query/ingestion/'}
};

document.getElementById('mainForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const textarea = document.querySelector('textarea[name="prompt"]');
    const btn = document.getElementById('submitBtn');
    const tool = document.getElementById('toolSelect').value;
    btn.disabled = true;
    btn.textContent = 'Analyzing, please wait...';
    const responseDiv = document.querySelector('.output');
    if (responseDiv) responseDiv.remove();

    const apiUrl = apiMap[tool].url;

    const res = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: textarea.value })
    });
    let html_response = 'No response received.';
    try {
        const data = await res.json();
        html_response = data.response || html_response;
    } catch (err) {
        html_response = 'Error parsing response.';
    }

    const output = document.createElement('div');
    output.className = 'output';
    output.innerHTML = `<h3>Response:</h3>${html_response}`;
    document.body.appendChild(output);

    btn.disabled = false;
    btn.textContent = 'Send';
});