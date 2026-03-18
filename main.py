import random
import math

def gcd(a, b):
    """Calcula o Máximo Divisor Comum (MDC)."""
    while b != 0:
        a, b = b, a % b
    return a

def power(a, b, m):
    """Potenciação modular eficiente: (a^b) % m."""
    res = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res

def generate_keys():
    """Gera o par de chaves e parâmetros do sistema."""
    # q: Um número primo grande (módulo)
    q = random.randint(pow(10, 20), pow(10, 30))
    # g: Raiz primitiva (gerador)
    g = random.randint(2, q - 1)
    # key: Chave privada (segredo do analista/sistema)
    key = random.randint(2, q - 2)
    # h: Parte da chave pública calculada como g^key % q
    h = power(g, key, q)
    
    return q, g, h, key

def encrypt(msg, q, h, g):
    """
    Cifra a senha.
    Retorna a lista de caracteres cifrados e o valor 'p' (c1).
    """
    en_msg = []
    k = random.randint(2, q - 2) # Chave efêmera (aleatoriedade por cifra)
    p = power(g, k, q)           # Este é o 'c1' da fórmula ElGamal
    s = power(h, k, q)           # Segredo compartilhado (h^k % q)
    
    for char in msg:
        # Cada caractere é multiplicado pelo segredo s
        en_msg.append(s * ord(char))
        
    return en_msg, p

def decrypt(en_msg, p, key, q):
    """
    Decifra a senha usando a chave privada.
    """
    dr_msg = []
    # Reconstrói o segredo compartilhado: s = p^key % q
    h = power(p, key, q)
    
    for char_code in en_msg:
        # Divide o código pelo segredo para voltar ao ASCII original
        dr_msg.append(chr(int(char_code / h)))
        
    return "".join(dr_msg)

# --- SIMULAÇÃO DO AMBIENTE DA FINTECH ---

# 1. O Analista de SI gera os parâmetros uma única vez
q, g, h, private_key = generate_keys()

print("--- CONFIGURAÇÃO DE SEGURANÇA ---")
print(f"Módulo (q): {q}")
print(f"Gerador (g): {g}")
print(f"Chave Pública (h): {h}")
print("-" * 40)

# 2. Usuário da Fintech tenta cadastrar uma senha
senha_original = "Fintech@Safe#2026"
print(f"\n[CLIENTE] Senha original: {senha_original}")

# 3. O sistema cifra a senha antes de salvar na base nova
dados_cifrados, valor_p = encrypt(senha_original, q, h, g)

print("\n[BASE DE DADOS - NOVA TABELA]")
print(f"Cifrado (c2): {dados_cifrados[:2]}... (truncado)")
print(f"Valor P (c1/IV): {valor_p}")
print("Status: Protegido com ElGamal")

# 4. Quando o usuário faz login, o sistema decifra para validar
senha_recuperada = decrypt(dados_cifrados, valor_p, private_key, q)

print(f"\n[SISTEMA DE AUTENTICAÇÃO]")
print(f"Senha recuperada para validação: {senha_recuperada}")

if senha_original == senha_recuperada:
    print("Sucesso: Senha validada com segurança total!")