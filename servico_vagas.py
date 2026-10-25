import requests
from bs4 import BeautifulSoup

def buscar_vagas(termo_busca="estagio"):
    """
    Realiza a requisição HTTP GET em um site de vagas e utiliza o BeautifulSoup
    para fazer o parsing (raspagem) do HTML bruto, extraindo títulos, empresas e links.
    """
    # URL de exemplo (substituiremos pelo site alvo em breve)
    url = f"https://example.com/vagas?q={termo_busca}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    try:
        print(f"Conectando à rede para buscar vagas de '{termo_busca}'...")
        
        # 1. Requisição HTTP real via requests
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Garante que se o site der erro (ex: 404), o código falha de forma tratada
        
        # 2. O BeautifulSoup entra em ação: transforma o HTML bruto (texto plano) em uma árvore de objetos
        soup = BeautifulSoup(response.text, 'html.parser')
        
        vagas = []
        
        # 3. Varredura do HTML (Exemplo estrutural de busca por tags e classes CSS)
        # O método find_all procura todos os blocos que correspondem ao critério
        for card in soup.find_all('div', class_='job-card'):
            # Extrai o texto limpo de dentro da tag do título
            titulo = card.find('h2', class_='job-title').get_text(strip=True)
            
            # Extrai o texto da empresa
            empresa = card.find('span', class_='company-name').get_text(strip=True)
            
            # Extrai o link de redirecionamento contido no atributo 'href' da tag <a>
            link = card.find('a', class_='job-link')['href']
            
            vagas.append({
                "titulo": titulo,
                "empresa": empresa,
                "link": link
            })
            
        return vagas

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição HTTP: {e}")
        return []
    except Exception as e:
        print(f"Erro ao processar o HTML com BeautifulSoup: {e}")
        return []