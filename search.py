import os
import time
import shutil
from colorama import init, Fore, Style

# Inicializa o colorama para Windows
init()

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def barra_de_progresso(atual, total, tamanho=30):
    progresso = int((atual / total) * tamanho)
    barra = "█" * progresso + "-" * (tamanho - progresso)
    porcentagem = (atual / total) * 100
    print(f"\r{Fore.CYAN}[{barra}] {porcentagem:.2f}% concluído{Style.RESET_ALL}", end='', flush=True)

def buscar_texto_em_arquivos(pasta, texto_procurado):
    arquivos_encontrados = 0
    arquivos_totais = sum(len(files) for _, _, files in os.walk(pasta))
    arquivos_processados = 0
    
    if arquivos_totais == 0:
        print(f"{Fore.RED}Nenhum arquivo encontrado na pasta!{Style.RESET_ALL}")
        return
    
    print(f"{Fore.YELLOW}Buscando '{texto_procurado}' nos arquivos...{Style.RESET_ALL}")
    time.sleep(1)
    
    for raiz, _, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            arquivos_processados += 1
            barra_de_progresso(arquivos_processados, arquivos_totais)
            
            try:
                with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as f:
                    for numero_linha, linha in enumerate(f, 1):
                        if texto_procurado in linha:
                            arquivos_encontrados += 1
                            print(f"\n{Fore.GREEN}Encontrado em: {caminho_completo} (Linha {numero_linha}){Style.RESET_ALL}")
            except Exception as e:
                print(f"\n{Fore.RED}Erro ao ler {caminho_completo}: {e}{Style.RESET_ALL}")
    
    print(f"\n{Fore.BLUE}Busca concluída. {arquivos_encontrados} ocorrências encontradas.{Style.RESET_ALL}")

def main():
    pasta_do_projeto = os.getcwd()  # Define a pasta atual como diretório de busca
    
    while True:
        termo_pesquisado = input(f"{Fore.MAGENTA}Digite a palavra para pesquisar: {Style.RESET_ALL}")
        buscar_texto_em_arquivos(pasta_do_projeto, termo_pesquisado)
        
        while True:
            continuar = input(f"{Fore.CYAN}Deseja limpar o terminal? (s/n): {Style.RESET_ALL}").strip().lower()
            if continuar == 's':
                limpar_terminal()
                break
            elif continuar == 'n':
                break
            else:
                print(f"{Fore.RED}Opção inválida! Digite 's' ou 'n'.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
