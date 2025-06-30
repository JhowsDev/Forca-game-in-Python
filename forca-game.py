import random
import os
import unicodedata 

def normalizar_string(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')

def exibir_forca(erros):
    estagios = [
        r"""
        -----
        |   |
        |
        |
        |
        |
        ----------
        """,
        r"""
        -----
        |   |
        |   O 
        |
        |
        |
        ----------
        """,
        r"""
        -----
        |   |
        |   O
        |   |
        |
        |
        ----------
        """,
       r"""
        -----
        |   |
        |   O
        |  /|   
        |
        |
        ----------
        """,
        r"""
        -----
        |   |
        |   O   
        |  /|\  
        |     
        |
        """,
        r"""
        -----
        |   |
        |   O   
        |  /|\  
        |  /  
        |
        ----------
        """,
        r"""
        -----
        |   |
        |   O   
        |  /|\  
        |  / \   
        |
        ----------
        """
    ]

    if 0 <= erros < len(estagios):
        print(estagios[erros])
    elif erros >= len(estagios):
        print(estagios[-1])
    else:
        print("Número de erros inválido!")

def escolher_palavra_aleatoria(caminho_do_arquivo):
    try:
        with open(caminho_do_arquivo, 'r', encoding='utf-8') as f:
            palavras = [linha.strip() for linha in f]

        if palavras:
            palavra_escolhida = random.choice(palavras)
            return palavra_escolhida
        else:
            print("Aviso: O arquivo está vazio.")
            return None

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_do_arquivo}' não foi encontrado.")
        return None

def jogar():
    """Função principal que executa o jogo da forca."""
    
    categorias = {
        "1": {"nome": "Geral", "arquivo": "_all_words.txt"},
        "2": {"nome": "Frutas", "arquivo": "_fruit_words.txt"},
        "3": {"nome": "Profissões", "arquivo": "_professions_words.txt"},
        "4": {"nome": "Países", "arquivo": "_countries_words.txt"}
    }
    
    arquivo_escolhido = None
    nome_da_categoria = None

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("====================================")
        print("=== JOGO DA FORCA DO JHOWSDEV ===") 
        print("====================================\n")
        print("Escolha uma categoria para jogar:")
        for chave, valor in categorias.items():
            print(f"{chave}: {valor['nome']}")
        
        escolha = input("\nDigite o número da sua escolha: ")

        if escolha in categorias:
            arquivo_escolhido = categorias[escolha]['arquivo']
            nome_da_categoria = categorias[escolha]['nome']
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

    palavra_secreta = escolher_palavra_aleatoria(arquivo_escolhido)
    
    if not palavra_secreta:
        print(f"Erro: Não foi possível carregar palavras do arquivo '{arquivo_escolhido}'.")
        return

    palavra_secreta = palavra_secreta.lower()

    palavra_secreta_normalizada = normalizar_string(palavra_secreta)
    letras_acertadas = []
    letras_erradas = []
    erros = 0
    max_erros = 6

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("====================================")
        print("=== JOGO DA FORCA DO JHOWSDEV ===")
        print("====================================\n")
        print(f"Categoria: {nome_da_categoria}\n")

        exibir_forca(erros)

        palavra_para_mostrar = ""
        for letra_original in palavra_secreta:
            if letra_original == ' ':
                palavra_para_mostrar += "  "
                continue

            letra_normalizada = normalizar_string(letra_original)
            if letra_normalizada in letras_acertadas:
                palavra_para_mostrar += letra_original.upper() + " "
            else:
                palavra_para_mostrar += "_ "
        print(f"Palavra: {palavra_para_mostrar}\n")

        print(f"Letras erradas: {' '.join(sorted(letras_erradas))}")
        print(f"Você tem {max_erros - erros} tentativas restantes.")

        acertos_necessarios = set(c for c in palavra_secreta_normalizada if c.strip())
        if set(letras_acertadas) == acertos_necessarios:
            print("\nParabéns! Você acertou a palavra!")
            print(f"A palavra era: {palavra_secreta.upper()}")
            break

        if erros >= max_erros:
            print("\nVocê foi enforcado!")
            print(f"A palavra secreta era: {palavra_secreta.upper()}")
            break

        palpite = input("\nDigite uma letra: ").lower()

        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite apenas uma letra.")
            input("Pressione Enter para continuar...")
            continue
        
        palpite_normalizado = normalizar_string(palpite)

        if palpite_normalizado in letras_acertadas or palpite in letras_erradas:
            print(f"Você já tentou a letra '{palpite}'. Tente outra.")
            input("Pressione Enter para continuar...")
            continue

        if palpite_normalizado in palavra_secreta_normalizada:
            print(f"\nBoa! A letra '{palpite}' está na palavra.")
            letras_acertadas.append(palpite_normalizado)
        else:
            print(f"\nQue pena! A letra '{palpite}' não está na palavra.")
            letras_erradas.append(palpite)
            erros += 1

    print("\n--- Fim de Jogo ---")

if __name__ == "__main__":
    jogar()