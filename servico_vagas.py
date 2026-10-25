from bs4 import BeautifulSoup

def buscar_vagas(termo_busca="estagio"):
    """
    Lê um arquivo HTML local e usa o BeautifulSoup para extrair as vagas,
    validando nossa lógica de parsing sem depender de rede externa.
    """
    try:
        print("Lendo página HTML local para teste de parsing...")
        
        # Abre o arquivo HTML local em vez de fazer requisição HTTP
        with open("pagina_teste.html", "r", encoding="utf-8") as arquivo:
            html_conteudo = arquivo.read()
            
        # O BeautifulSoup converte o texto HTML em uma árvore navegável
        soup = BeautifulSoup(html_conteudo, 'html.parser')
        
        vagas = []
        
        # Varredura do HTML buscando as tags e classes específicas
        for card in soup.find_all('div', class_='job-card'):
            titulo = card.find('h2', class_='job-title').get_text(strip=True)
            empresa = card.find('span', class_='company-name').get_text(strip=True)
            link = card.find('a', class_='job-link')['href']
            
            vagas.append({
                "titulo": titulo,
                "empresa": empresa,
                "link": link
            })
            
        return vagas

    except Exception as e:
        print(f"Erro ao processar o HTML: {e}")
        return []