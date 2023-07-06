salario = 2000

def salario_bonus(bonus, lista):        
    global salario

    #quando usar um objeto mutavel copiar a lista para nao gerar erro
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)
#salario_bonus(500)  # 2500
