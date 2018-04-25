import lib_nooblinux
import operaciones
import sys
def main():

    list_1 = lib_nooblinux.leer_milista()
    list_2 = lib_nooblinux.leer_milista()
    lib_nooblinux.print_milista(list_1)
    print list_1
    print list_2
    list_add = operaciones.my_add(list_1, list_2, 10, 0)
    lib_nooblinux.print_milista(list_add)
    print list_add
    #binario = lib_nooblinux.convert_binario(list_1)
    #lib_nooblinux.print_milista(binario)
main()
