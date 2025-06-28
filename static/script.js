const selectCompetencia = document.getElementById('selectCompetencia');
const desviosContainer = document.getElementById('desviosContainer');
const desvioList = document.getElementById('desvioList');
let selectedDesvio = null;

const desviosPorCompetencia = {
    "1": [
        "Desvio 1.1",
        "Desvio 1.2",
        "Desvio 1.3",
        "Desvio 1.4",
        "Desvio 1.5"
    ],
    "2": [
        "Desvio 2.1",
        "Desvio 2.2",
        "Desvio 2.3",
        "Desvio 2.4",
        "Desvio 2.5"
    ],
    "3": [
        "Desvio 3.1",
        "Desvio 3.2",
        "Desvio 3.3",
        "Desvio 3.4",
    ],
    "4": [
        "Desvio 4.1",
        "Desvio 4.2",
        "Desvio 4.3",
        "Desvio 4.4"
    ],
    "5": [
        "Desvio 5.1",
        "Desvio 5.2",
        "Desvio 5.3",
        "Desvio 5.4"
    ]
};

selectCompetencia.addEventListener('change', () => {
    const selected = selectCompetencia.value;

    // Se o usuário selecionar "Nenhuma"
    if (selected === "0") {
        desviosContainer.classList.add('hidden');
        desvioList.innerHTML = '';
        selectedDesvio = null;
        return;
    }

    const desvios = desviosPorCompetencia[selected];
    if (!desvios) return;

    desvioList.innerHTML = '';
    selectedDesvio = null;

    desvios.forEach(d => {
        const div = document.createElement('div');
        div.classList.add('desvio-choice');
        div.textContent = d;
        div.dataset.desvio = d;
        div.addEventListener('click', () => {
            document.querySelectorAll('.desvio-choice').forEach(c => c.classList.remove('selected'));
            div.classList.add('selected');
            selectedDesvio = d;
        });
        desvioList.appendChild(div);
    });

    desviosContainer.classList.remove('hidden');
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

// Modal
const modal = document.getElementById('responseModal');
const modalClose = document.getElementById('modalClose');
const modalText = document.getElementById('modalText');
modalClose.onclick = () => modal.style.display = 'none';
window.onclick = event => { if (event.target == modal) modal.style.display = 'none'; };

// Botão gerar
document.getElementById('generateBtn').addEventListener('click', async () => {
    const text = document.getElementById('inputText').value.trim();
    if (!text) {
        showAlert('O campo de texto está vazio.');
        return;
    }

    const selectedCompetencia = selectCompetencia.value;
    if (!selectedCompetencia) {
        showAlert('Selecione uma competência.');
        return;
    }

    if (!selectedDesvio) {
        showAlert('Selecione um desvio.');
        return;
    }

    const params = {
        competencia: selectedCompetencia,
        desvio: selectedDesvio
    };

    const options = [];
    [1, 2, 3, 4, 5].forEach(i => {
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
