# Código para desligar ou reiniciar o sistema operecional

import os

# solicitar a ação desejada
# inclui o ".strip()" e o ".lower()" para evitar digitação por engano de espaços ou maiúsculas
option = input("Deseja desligar ou reiniciar o computador? (digite 'desligar' ou 'reiniciar'): ").strip().lower()

if option == "desligar":
    os.system("shutdown /s /f /t 0")  # Desligar o computador imediatamente
elif option == "reiniciar":
    os.system("shutdown /r /f /t 0")  # Reiniciar o computador imediatamente
else:
    print("Opção inválida. Use 'desligar' ou 'reiniciar'.")

""" O parâmetro /s é usado para desligar e /r para reiniciar, ambos com um atraso de 0 segundos (/t 0), o que significa
que a ação ocorrerá imediatamente. O parâmetro /f é usado para forçar o fechamento de aplicativos em execução. """
