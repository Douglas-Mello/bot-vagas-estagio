from servico_vagas import buscar_vagas

def formatar_e_exibir_vagas(vagas):
    """
    Recebe a lista de vagas e exibe os dados de forma formatada e limpa no console.
    """
    if not vagas:
        print("Nenhuma vaga encontrada.")
        return
    
    print("\n" + "="*50)
    print(" 🚀 VAGAS DE ESTÁGIO ENCONTRADAS ")
    print("="*50)
    
    # A função enumerate percorre a lista numerando os itens a partir de 1
    for i, vaga in enumerate(vagas, 1):
        print(f"{i}. Cargo:   {vaga['titulo']}")
        print(f"   Empresa: {vaga['empresa']}")
        print(f"   Link:    {vaga['link']}")
        print("-" * 50)

def salvar_em_arquivo(vagas):
    """
    Salva as vagas encontradas em um arquivo de texto local para persistência.
    """
    nome_arquivo = "vagas_encontradas.txt"
    
    # O gerenciador de contexto 'with' garante que o arquivo será fechado corretamente após a escrita
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for vaga in vagas:
            linha = f"Cargo: {vaga['titulo']} | Empresa: {vaga['empresa']} | Link: {vaga['link']}\n"
            arquivo.write(linha)
            
    print(f"Resultados salvos com sucesso no arquivo '{nome_arquivo}'.")

if __name__ == "__main__":
    # Ponto de entrada principal do programa
    termo_pesquisa = "estagio software"
    
    print(f"Iniciando busca de vagas para: {termo_pesquisa}")
    
    # Chama a função importada do nosso módulo de serviço
    lista_vagas = buscar_vagas(termo_busca=termo_pesquisa)
    
    # Processa e exibe os resultados
    formatar_e_exibir_vagas(lista_vagas)
    
    # Salva os dados em disco
    salvar_em_arquivo(lista_vagas)