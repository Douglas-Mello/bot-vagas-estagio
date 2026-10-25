import csv
from servico_vagas import buscar_vagas

def formatar_e_exibir_vagas(vagas):
    """
    Recebe a lista de vagas e exibe os dados formatados no console.
    """
    if not vagas:
        print("Nenhuma vaga encontrada.")
        return
    
    print("\n" + "="*50)
    print(" 🚀 VAGAS DE ESTÁGIO ENCONTRADAS ")
    print("="*50)
    
    for i, vaga in enumerate(vagas, 1):
        print(f"{i}. Cargo:   {vaga['titulo']}")
        print(f"   Empresa: {vaga['empresa']}")
        print(f"   Link:    {vaga['link']}")
        print("-" * 50)

def salvar_em_csv(vagas):
    """
    Salva a lista de dicionários de vagas em um arquivo estruturado .csv
    utilizando a biblioteca nativa csv do Python.
    """
    nome_arquivo = "vagas_encontradas.csv"
    
    try:
        # Abre o arquivo com codificação utf-8-sig para compatibilidade perfeita com o Excel
        with open(nome_arquivo, mode="w", newline="", encoding="utf-8-sig") as arquivo_csv:
            # Definimos os nomes das colunas (cabeçalho do CSV)
            colunas = ["titulo", "empresa", "link"]
            
            # Criamos o escritor CSV vinculado ao arquivo aberto
            escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
            
            # Escreve o cabeçalho na primeira linha
            escritor.writeheader()
            
            # Escreve cada dicionário de vaga como uma linha no arquivo
            for vaga in vagas:
                escritor.writerow(vaga)
                
        print(f"Sucesso! Dados exportados para o arquivo estruturado '{nome_arquivo}'.")
        
    except Exception as e:
        print(f"Erro ao salvar o arquivo CSV: {e}")

if __name__ == "__main__":
    termo_pesquisa = "estagio software"
    
    print(f"Iniciando busca de vagas para: {termo_pesquisa}")
    
    # Chama o módulo de serviço para buscar os dados
    lista_vagas = buscar_vagas(termo_busca=termo_pesquisa)
    
    # Exibe no console
    formatar_e_exibir_vagas(lista_vagas)
    
    # Salva no novo formato estruturado CSV (se houver vagas)
    if lista_vagas:
        salvar_em_csv(lista_vagas)