import requests
from bs4 import BeautifulSoup

def buscar_vagas(termo_busca="estagio"):
    """
    Realiza uma requisição HTTP GET real para um site alvo,
    utilizando headers de navegador e tratamento avançado de erros de rede.
    """
    # Substitua esta URL pelo site real de vagas que deseja raspar
    url = f"https://example.com/jobs?q={termo_busca}"
    
    # Headers completos para simular um navegador real e evitar bloqueios anti-bot básicos
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    
    try:
        print(f"Conectando à internet para buscar vagas de '{termo_busca}'...")
        
        # O parâmetro timeout=10 evita que o script trave indefinidamente se o servidor demorar a responder
        response = requests.get(url, headers=headers, timeout=10)
        
        # Dispara exceção automática para códigos de erro HTTP (ex: 403 Proibido, 404 Não Encontrado, 500 Erro de Servidor)
        response.raise_for_status()
        
        # O BeautifulSoup recebe o HTML bruto baixado da web
        soup = BeautifulSoup(response.text, 'html.parser')
        
        vagas = []
        
        # Varredura do HTML real buscando os elementos da página
        for card in soup.find_all('div', class_='job-card'):
            titulo_el = card.find('h2', class_='job-title')
            empresa_el = card.find('span', class_='company-name')
            link_el = card.find('a', class_='job-link')
            
            # Programação defensiva: só adiciona se encontrar todas as informações necessárias
            if titulo_el and empresa_el and link_el:
                vagas.append({
                    "titulo": titulo_el.get_text(strip=True),
                    "empresa": empresa_el.get_text(strip=True),
                    "link": link_el['href']
                })
            
        return vagas

    except requests.exceptions.Timeout:
        print("Erro: O servidor demorou muito para responder (Timeout excedido).")
        return []
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP retornado pelo servidor: {e}")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão na rede: {e}")
        return []
    except Exception as e:
        print(f"Erro inesperado no processamento do HTML: {e}")
        return []
    