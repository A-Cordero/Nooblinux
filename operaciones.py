import sys
def my_sub(list_a, list_b, base) :
    print "te mamaste we"
    return [1,1]
#la suma acepta dos listas , la base en que se sumara y un valor por defecto 0 si se suman entero o 1 si la suma viene de decimales
def my_add( list_a, list_b, base,decimal) :
    #listas a usar
    list_a_entero = []
    list_b_entero = []
    list_a_decimal = []
    list_b_decimal = []
    list_z_decimal = []
    list_aux = []
    #por defecto list_z es entera
    list_z = []
    flag_decimal  = 0
    #signo por defecto es positivo(0)
    signo = 0
    #se analizan los signos
    if list_a.count("-") == 1 | list_b.count("-") == 1 :
        if list_a.count("-") == 1 and list_b.count("-") == 1 :
                signo = 1
                list_a.pop(0)
                list_b.pop(0)
        elif (list_a.count("-") == 1 and list_b.count("-") == 0) | (list_a.count("-") == 0 and list_b.count("-") == 1)  :
            return my_sub(list_a, list_b, base)

    #se analiza si tienen parte decimal
    if list_a.count(".") == 1 | list_b.count(".") == 1:
        #se sumaran enteros
        flag_decimal = 1
        if list_a.count(".") == 1 :
            for i in range( 0 , list_a.index(".")) :
                list_a_entero.append(list_a[i])
            for i in range(list_a.index(".")+1, len(list_a)) :
                list_a_decimal.append(list_a[i])
        else :
                list_a_entero = list_a
        if list_b.count(".") == 1 :
            for i in range( 0 , list_b.index(".")) :
                list_b_entero.append(list_b[i])
            for i in range(list_b.index(".")+1, len(list_b)) :
                list_b_decimal.append(list_b[i])
        else :
                list_b_entero = list_b
        if len(list_a_decimal) > len(list_b_decimal) :
            for i in range( len(list_b_decimal) , len(list_a_decimal)) :
                list_b_decimal.append('0')
        else :
            for i in range( len(list_a_decimal) , len(list_b_decimal)) :
                list_a_decimal.append('0')

        list_z_decimal = my_add(list_a_decimal,list_b_decimal,base, 1)
    else :
        list_a_entero = list_a
        list_b_entero = list_b

    carry = 0
    i = 0
    j = 0

    #nos aseguramos que  a  es mayor siempre
    if len(list_a_entero) < len( list_b_entero) :
        list_temp = list_a_entero
        list_a_entero = list_b_entero
        list_b_entero = list_temp
    #La lista  donde quedara el resultado debe ser de tamano 1 mas que la lista a
    for k in range( (len(list_a_entero) + 1)) :
        list_z.append(0)
    #se recorre desde la ultima posicion de b hasta el final de b
    for i in range( len(list_b_entero) -1, -1, -1) :
        carry += (int(list_a_entero[i+ ( len(list_a_entero) - len( list_b_entero))]) + int(list_b_entero[i]))
        #suma en una base dada
        if carry >= base :
            aux = carry%base
            list_z[ (i -1) + ( len(list_a_entero) + 1 - len( list_b_entero))] += carry/base
            carry = aux
        list_z[i+ ( len(list_a_entero) + 1 - len( list_b_entero))] += carry
        carry *= 0
    carry *=0
    #se comienza donde quedo i hasta el final de la lista a
    if i  <= 0 :
        for j in range(i+ ( len(list_a_entero) - len( list_b_entero) -1), -1, -1) :
            carry += int(list_a_entero[j])
            list_z[j+1] += carry
            if list_z[j+1] >= base :
                list_z[j] += list_z[j+1]/base
                list_z[j+1] = list_z[j+1]%base
            carry *= 0
    #se eliminan los 0 a la izquierda
    k = 0
    while list_z[k] == 0 and len(list_z) != 1 and decimal != 1:
        list_z.pop(k)
    #eliminamos posibles numeros mayores a la base
    for i in range( len(list_z)-1, -1, -1) :
        if list_z[i] >= base :
            if i == 0 :
                list_z.insert(0, list_z[0]/base)
                list_z[1] = list_z[1]%base
            else :
                list_z[i-1] += list_z[i]/base
                list_z[i] = list_z[i]%base
    #se une la parte entera con la decimal
    if flag_decimal != 0 :
        if len(list_z_decimal) != len(list_a_decimal) :
            list_aux.append(list_z_decimal[0])
            list_z_decimal.pop(0)
            list_z = my_add(list_z, list_aux, base, 0)
        list_z.append(".")
        list_z.extend(list_z_decimal)
    if signo == 1 :
        list_z.insert(0,"-")
    return list_z
