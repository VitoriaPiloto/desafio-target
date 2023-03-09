import json
campos = ['estado','valor']
with open('dadosEstados.json') as f:
    entrada = json.load(f)

soma=0
for elemento in entrada:
    for campo in campos:
        
        if(elemento['estado'] == 'RJ'):
            valorRJ = elemento['valor']
        
        if(elemento['estado']=='SP'):
            valorSP = elemento['valor']
        
        if(elemento['estado']=='MG'):
            valorMG = elemento['valor']
        
        if(elemento['estado']=='ES'):
            valorES = elemento['valor']
        
        if(elemento['estado']=='Outros'):
            valorOutros = elemento['valor']
        
        soma=soma+elemento['valor']
        

porcentagemRJ= (100*valorRJ)/soma
porcentagemSP= (100*valorSP)/soma
porcentagemMG= (100*valorMG)/soma
porcentagemES= (100*valorES)/soma
porcentagemOutros= (100*valorOutros)/soma

print("Porcentagem RJ: ",porcentagemRJ)
print("Porcentagem SP: " ,porcentagemSP)
print("Porcentagem MG: ",porcentagemMG)
print("Porcentagem ES: ",porcentagemES)
print("Porcentagem Outros: ",porcentagemOutros)
          