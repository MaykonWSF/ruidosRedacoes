// Atualiza o valor exibido ao lado do slider
const sliders = [1, 2, 3, 4, 5];
const checkboxes = [1, 2, 3, 4, 5];
sliders.forEach(i => {
    const slider = document.getElementById(`slider${i}`);
    const output = document.getElementById(`value${i}`);
    const chk = document.getElementById(`chk${i}`);
    // Atualiza valor em %
    slider.addEventListener('input', () => output.textContent = slider.value + '%');
    // Ativa/desativa slider com checkbox
    chk.addEventListener('change', () => slider.disabled = !chk.checked);
    // Estado inicial
    slider.disabled = !chk.checked;
});

// Alerta
const alertBox = document.getElementById('alertBox');
const alertMsg = document.getElementById('alertMessage');
document.getElementById('closeAlert').addEventListener('click', () => alertBox.classList.remove('show'));
function showAlert(msg) {
    alertMsg.textContent = msg;
    alertBox.classList.add('show');
    setTimeout(() => alertBox.classList.remove('show'), 3000);
}

// Modal handlers
const modal = document.getElementById('responseModal');
const modalClose = document.getElementById('modalClose');
const modalText = document.getElementById('modalText');
modalClose.onclick = () => modal.style.display = 'none';
window.onclick = event => { if (event.target == modal) modal.style.display = 'none'; };

// Envia dados para o servidor Flask
document.getElementById('generateBtn').addEventListener('click', async () => {
    const text = document.getElementById('inputText').value.trim();
    if (!text) { showAlert('O campo de texto está vazio.'); return; }
    const params = {};
    sliders.forEach(i => { if (document.getElementById(`chk${i}`).checked) params[`param${i}`] = document.getElementById(`slider${i}`).value; });
    if (Object.keys(params).length === 0) { showAlert('Nenhuma competência selecionada.'); return; }
    const options = [];
    checkboxes.forEach(i => {
        if (document.getElementById(`opt${i}`).checked) {
            options.push(`opt${i}`);
        }
    });

    const overlay = document.getElementById('loadingOverlay');
    overlay.classList.add('show');

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, params, options })
        });
        if (!response.ok) throw new Error('Erro na requisição');
        
        const result = await response.json();
        console.log('Resposta do servidor:', result);
        modalText.textContent = JSON.stringify(result, null, 2);
        modal.style.display = 'block';
            
    } catch (err) {
        console.error(err);
        alert('Falha ao enviar dados ao servidor.');
    } finally {
        overlay.classList.remove('show');
    }    
});