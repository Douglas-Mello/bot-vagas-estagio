import requests

def buscar_vagas(termo_busca="estagio", local="brasil"):
    """
    Realiza a requisição HTTP para buscar as vagas de estágio.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    try:
        print(f"Conectando ao servidor para buscar vagas de '{termo_busca}'...")
        
        # Dados de teste estruturados para validação do fluxo do bot
        vagas_exemplo = [
            {
                "titulo": "Estágio em Desenvolvimento Software", 
                "empresa": "Tech Brasil", 
                "link": "https://exemplo.com/vaga1"
            },
            {
                "titulo": "Estágio em Suporte e Redes", 
                "empresa": "Inovação TI", 
                "link": "https://exemplo.com/vaga2"
            }
        ]
        return vagas_exemplo

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição HTTP: {e}")
        return []