# Para definir o modo de energia, é necesário ter os GUIDs (identificadores globais exclusivos) do seu sistema
# Geralmente os GUIDs do modo equilibrado e de alto desempenho, correspondem ao seguinte código:
# GUID do Esquema de Energia: 381b4222-f694-41f0-9685-ff5bb260df2e  (Equilibrado)
# GUID do Esquema de Energia: 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c  (Alto desempenho)

# Para saber os códigos no seu sistema, digite "powercfg /l" no prompt de comando

# Para alterar o modo de energia é utilizado o subprocess para realizar esse procedimento
# O código a seguir exemplifica como é realizado este processo

# importar a biblioteca
import subprocess

# solicitar o modo de energia desejado
# inclui o ".strip()" e o ".lower()" para evitar digitação por engano de espaços ou maiúsculas
user_mode = str(input("Power Mode: ")).strip().lower()

# condição para definir o modo de energia conforme a solicitação do user
if user_mode == "equilibrado":
    subprocess.run(["powercfg", "/s", "381b4222-f694-41f0-9685-ff5bb260df2e"])  # define o modo equilibrado
    print("Modo de Energia Equilibrado definido com sucesso!")  # notifica o user de que a alteração para o modo equilibrado foi realizada

elif user_mode == "alto-desempenho":
    subprocess.run(["powercfg", "/s", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"])  # define o modo alto desempenho
    print("Modo de Energia Alto Desempenho definido com sucesso!")  # notifica o user de que a alteração para o modo alto desempenho foi realizada

else:
    print("Modo não suportado ou inexistente. Use 'equilibrado' ou 'alto-desempenho'.")  # notifica o user de que o modo digitado está incorreto ou não existe
