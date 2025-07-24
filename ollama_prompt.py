import ollama


def create_noisy_essay(essay: str, deviation: str, competency: str, model: str) -> str:
    """
    Adiciona um desvio específico a uma redação dissertativa-argumentativa.
    
    Args:
        essay (str): A redação original.
        deviation (str): O desvio a ser adicionado.
        competency (str): A competência a ser atacada.
        model (str): O modelo de IA a ser usado ('Deepseek', 'Qwen', 'Llama', 'Gemini').
        
    Returns:
        str: A redação com o desvio adicionado.
    """
    task = "Sua tarefa é adicionar desvios em redações dissertativas-argumentativas do ENEM."
    message = f"Em ataque à competência {competency} do ENEM, reescreva a redação a seguir com desvio: {deviation}.\n{essay}"

    prompt = f"{task}\n {message}\n"
    if model == 'Deepseek':
        model = 'deepseek-r1:8b'
    elif model == 'Qwen':
        model = 'qwen3:latest'
    elif model == 'Llama':
        model = 'llama3:8b'
    else:
        raise ValueError("Modelo desconhecido. Use 'Deepseek', 'Qwen' ou 'Llama'.")

    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": "Atue como um revisor especializado em redações dissertativas-argumentativas para o ENEM."},
            {"role": "user", "content": prompt},
        ]
    )
    # Resposta da API
    res = response['message']['content']

    return res.strip()


