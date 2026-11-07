import os
import subprocess

resultado = subprocess.run("ps aux --sort=-%cpu | head" , capture_output=True,
                           text= True, shell=True)

linhas = resultado.stdout.split("\n")

try: 
    limite_CPU = float(input("Digite o limite da CPU: "))

except ValueError:
    print("Apenas Números! ")
    exit()

if limite_CPU < 0 :
    print("X" *35)
    print("    LIMITE NÃO DISPONÍVEl    ")
    print("X" *35)
    exit()


print("=" * 42)
print("        --MONITOR DE PROCESSOS--   ")
print(f"          CPU acima de {limite_CPU}% ")
print("="* 42)


for linha in linhas:
    partes = linha.split()
    if len (partes) >= 3:
        if partes[0] == "USER":
            continue
        cpu = float(partes[2])
        if cpu > limite_CPU:
            print(f"Usuário :  {partes[0]}")
            print(f"Processo :  {partes[1]}")
            print(f"Programa :  {partes[10]}")
            print(f"Cpu :  {partes[2]}")
            print("-" * 42) 


investigar = input("Deseja investigar algum PID? (responda com sim/nao): ")

if investigar == "sim":
    resposta = int(input("Digite o PID: "))
    resposta2 = subprocess.run(["ps" , "-p", str(resposta), "-o",
    "user,pid,comm,%cpu"], 
    capture_output=True,text=True)
    print(resposta2.stdout)
    
else:
    print("Obrigado pela sua resposta! ")