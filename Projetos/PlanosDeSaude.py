# Atividade: Cálculo do valor de Planos de Sáude
# Autor: Daniel Macedo Silva

print("Bem-vindo ao simulador de Plano de Saúde!")

# Entrada de dados
idade = int(input("Informe a idade do paciente: "))
sexo = input("Informe o sexo do paciente (M/F): ")
coparticipacao_input = input("Deseja plano com co-participação? (S/N): ")
coparticipacao = coparticipacao_input.upper() == 'S'
quarto = input("Tipo de quarto desejado em internação (apartamento/enfermaria): ")

print("\nTipos de plano disponíveis:")
print("I - Rede básica de laboratórios, clínicas e hospitais credenciados")
print("II - Rede ampliada com hospitais e clínicas renomadas em capitais e interior")
print("III - Rede premium com hospitais top de SP (Sírio Libanês, Albert Einstein) e cobertura no exterior")

nivel_input = input("Escolha o tipo de plano (I/II/III): ").upper()

if nivel_input == '1':
    nivel = 'I'
elif nivel_input == '2':
    nivel = 'II'
elif nivel_input == '3':
    nivel = 'III'
else:
    nivel = nivel_input  # Assume que digitou I, II ou III corretamente

# Valores base
valores_masculino = [350, 600, 1200]  
valores_feminino = [320, 580, 1150]
# Índices: 0 -> I, 1 -> II, 2 -> III

# Valor de acordo com o sexo
if sexo.upper() == 'M':
    valores = valores_masculino
else:
    valores = valores_feminino

# Mapeamento de nível
niveis = {'I': 0, 'II': 1, 'III': 2}
indice = niveis[nivel.upper()]

# Resgata valor base
valor_base = valores[indice]

# Ajuste por idade
if idade < 18:
    valor_base *= 0.6
elif idade > 59:
    valor_base *= 1.3

# Ajuste por co-participação (desconto de 25% na mensalidade)
if coparticipacao:
    valor_base *= 0.75

# Ajuste por tipo de quarto
if quarto.lower() == 'apartamento':
    valor_base *= 1.15  # 15% de aumento no valor

# Saída de dados
print("\n--- Resultado da Simulação ---")
print(f"Idade: {idade} anos")
print(f"Sexo: {'Masculino' if sexo.upper() == 'M' else 'Feminino'}")
print(f"Co-participação: {'Sim (25%)' if coparticipacao else 'Não'}")
print(f"Tipo de Quarto: {quarto.capitalize()}")
print(f"Tipo de Plano: Nível {nivel.upper()}")
print(f"Valor da mensalidade: R$ {round(valor_base, 2):.2f}")