from servico_vagas import buscar_vagas

def formatar_e_exibir_vagas(vagas):
    if not vagas:
        print("Nenhuma vaga encontrada.")
        return
    
    print("\n" + "="*40)
    print(" VAGAS DE ESTÁGIO ENCONTRADAS ")
    print("="*40)
    
    for i, vaga in enumerate(vagas, 1):
        print(f"{i}. Cargo: {vaga['titulo']}")
        print(f"   Empresa: {vaga['empresa']}")
        print(f"   Link: {vaga['link']}")
        print("-" * 40)

def salvar_em_arquivo(vagas):
    with open("vagas_encontradas.txt", "w", encoding="utf-8") as arquivo:
        for vaga in vagas:
            arquivo.write(f"Cargo: {vaga['titulo']} | Empresa: {vaga['empresa']} | Link: {vaga['link']}\n")
    print("\nResultados salvos com sucesso no arquivo 'vagas_encontradas.txt'.")

if __name__ == "__main__":
    termo = "estagio software"
    lista_vagas = buscar_vagas(termo_busca=termo)
    
    formatar_e_exibir_vagas(lista_vagas)
    salvar_em_arquivo(lista_vagas)