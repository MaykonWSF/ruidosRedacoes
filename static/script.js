const selectCompetencia = document.getElementById('selectCompetencia');
const desviosContainer = document.getElementById('desviosContainer');
const desvioList = document.getElementById('desvioList');
let selectedDesvio = null;

const desviosPorCompetencia = {
    "1": ["Desvios de convenções da escrita", "Desvios gramaticais", "Desvios de escolha de registro", "Desvios de escolha vocabular"],
    "2": ["Tangenciamento do tema", "Fuga total do tema", "Repertório mal utilizado", "Tipo textual diferente do dissertativo-argumentativo"],
    "3": ["Falta de coerência", "Sem ponto de vista claro"],
    "4": ["Falta de coesão", "Uso inadequado de conectores"],
    "5": ["Falta de proposta de intervenção", "Desrespeito aos direitos humanos", "Incitação à violência"]
};

// Atualiza lista de desvios conforme competência
selectCompetencia.addEventListener('change', () => {
    const selected = selectCompetencia.value;

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

// Modais
const modal = document.getElementById('responseModal');
const modalClose = document.getElementById('modalClose');
const modalText = document.getElementById('modalText');
const modelModal = document.getElementById('modelSelectionModal');
const modelModalClose = document.getElementById('modelModalClose');
const modelButtons = document.querySelectorAll('.model-btn');

modalClose.onclick = () => modal.style.display = 'none';
modelModalClose.onclick = () => modelModal.style.display = 'none';

window.onclick = event => {
    if (event.target === modal) modal.style.display = 'none';
    if (event.target === modelModal) modelModal.style.display = 'none';
};

modelButtons.forEach(button => {
    button.addEventListener('click', () => {
        const selectedModel = button.getAttribute('data-model');
        modelModal.style.display = 'none';
        gerarRedacaoComModelo(selectedModel);
    });
});

// Botão principal: validações e abertura de modal de modelos
document.getElementById('generateBtn').addEventListener('click', () => {
    const text = document.getElementById('inputText').value.trim();
    if (!text) {
        showAlert('O campo de texto está vazio.');
        return;
    }

    const checkboxes = document.querySelectorAll('.checkbox-list input[type="checkbox"]');
    const options = [];

    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            const labelText = checkbox.parentElement.textContent.trim();
            options.push(labelText);
        }
    });

    if (!selectedDesvio && options.length === 0) {
        showAlert('Selecione pelo menos um ruído: um desvio de competência ou uma opção geral.');
        return;
    }

    openModelSelectionModal();
});

function openModelSelectionModal() {
    modelModal.style.display = 'block';
}

// Envia dados com modelo escolhido
async function gerarRedacaoComModelo(modelo) {
    const text = document.getElementById('inputText').value.trim();
    const selectedCompetencia = selectCompetencia.value;

    const checkboxes = document.querySelectorAll('.checkbox-list input[type="checkbox"]');
    const selectedOptions = [];
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            const labelText = checkbox.parentElement.textContent.trim();
            selectedOptions.push(labelText);
        }
    });

    const params = {
        competencia: selectedCompetencia,
        desvio: selectedDesvio,
        modelo: modelo,
        desviosGerais: selectedOptions
    };

    const overlay = document.getElementById('loadingOverlay');
    overlay.classList.add('show');

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, params })
        });

        if (!response.ok) throw new Error('Erro na requisição');
        const result = await response.json();

        modalText.textContent = JSON.stringify(result, null, 2);
        modal.style.display = 'block';
    } catch (err) {
        console.error(err);
        alert('Falha ao enviar dados ao servidor.');
    } finally {
        overlay.classList.remove('show');
    }
}
