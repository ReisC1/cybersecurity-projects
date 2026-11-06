import socket

alvo = input("Digite o endereço IP ou hostname do alvo: ")  
contador = 0


def testar_porta(porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    resultado = s.connect_ex((alvo, porta))
    s.close()
    return resultado
      
    

print(f"Escaneando portas em {alvo}")
for porta in range(1,1024): 
    resultado = testar_porta(porta) 
    if resultado == 0:
        print(f"Porta {porta} está aberta")         
        contador += 1


print(f"Scan terminado. {contador} portas encontradas abertas.")
print("Obrigado por usar o scanner de portas!")