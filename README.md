# 🛡️ Fintech Data Shield: Implementação ElGamal

Este projeto apresenta uma solução de segurança de dados para uma Fintech, focada na proteção de credenciais de usuários em uma base de dados de alto crescimento. A solução utiliza o algoritmo de criptografia assimétrica **ElGamal** para garantir a confidencialidade e integridade das senhas.

## 📝 O Cenário
Um aumento na base de usuários de uma Fintech gerou preocupações de segurança. Como Analista de SI, a missão foi implementar um nível superior de proteção para as senhas sem corromper ou alterar a estrutura da base de dados existente, apenas adicionando uma tabela auxiliar para metadados de criptografia.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Bibliotecas:** `math` (aritmética modular), `random` (geração de chaves efêmeras)
* **Algoritmo:** ElGamal (Criptografia de Chave Pública baseada em Logaritmo Discreto)



## 💡 Por que ElGamal?
Diferente de métodos de hash tradicionais, o ElGamal oferece:
1. **Segurança Probabilística:** A mesma senha gera textos cifrados diferentes a cada execução (devido à chave efêmera $k$), o que impede ataques de análise de frequência e Rainbow Tables.
2. **Resistência Matemática:** A segurança baseia-se na dificuldade computacional de resolver o problema do logaritmo discreto em corpos finitos.
3. **Escalabilidade:** Permite a rotação de chaves e o uso de metadados (SALT, IV e Contador de Iteração) em uma base separada, mantendo o legado funcional.

## 🏗️ Arquitetura da Solução
Para manter a base atual, a proposta define a criação de uma tabela de **Security Metadata**:
* **Chave Pública ($h$):** Compartilhada para cifragem.
* **Valor P ($c_1$):** Vetor de inicialização/componente da cifra gerado por senha.
* **Texto Cifrado ($c_2$):** A representação numérica da senha protegida.



## 💻 Demonstração: Saída do Terminal
Abaixo, apresento o log real da execução do sistema, validando a geração de chaves, a cifragem dos dados e a posterior recuperação para autenticação.

```text
--- CONFIGURAÇÃO DE SEGURANÇA ---
Módulo (q): 565426066828200446564383598878
Gerador (g): 143773699967134059815311833171
Chave Pública (h): 434412517996919106278361554643
----------------------------------------

[CLIENTE] Senha original: Fintech@Safe#2026

[BASE DE DADOS - NOVA TABELA]
Cifrado (c2): [2376424210950278238102467544010, 3564636316425417357153701316015]... (truncado)
Valor P (c1/IV): 373014913690455233801365195305
Status: Protegido com ElGamal

[SISTEMA DE AUTENTICAÇÃO]
Senha recuperada para validação: Fintech@Safe#2026
Sucesso: Senha validada com segurança total!

