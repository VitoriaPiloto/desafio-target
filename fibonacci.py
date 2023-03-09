def fibonacci(n):
    if (n < 3):
        return (1)
    else :
        return fibonacci(n - 1) + fibonacci(n - 2);
  
numero=input("Insira o numero que deseja descobrir se faz parte da sequencia de fibonacci: ")
numero = int(numero)
i=0
while (i<=numero):
    result=fibonacci(i)
    if(result==numero):
        print("O numero faz parte da sequência!!")
        break
    else:
        if(result>numero):
            break
    i=i+1
print("Número não faz parte da sequência!!")


