import json
menor=99999999
maior=0
soma=0
campos = ['dia','valor']
with open('dados.json') as f:
    entrada = json.load(f)

for elemento in entrada:
    for campo in campos:
        soma=soma+elemento['valor']
        if (elemento['valor']!=0):
            menor=elemento[campo]
        if (elemento['valor']>maior):
            maior=elemento[campo]
quant=0       
media = soma/30 
for elemento in entrada:
    for campo in campos:
        if(elemento['valor']>media):
            quant=quant+1
print("Maior valor arrecadado: ",maior)
print("Menor valor arrecadado: ", menor)
print("Quantidade de dias que o valor foi maior que a média mensal: ",quant)            
