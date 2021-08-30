import os
class Nodo:
    def __init__(self,data):
        self.prev = None
        self.next = None
        self.data = data
class Cola:
    def __init__(self):
        self.first = None
        self.last = None
    def Empty(self):
        return self.first == None
    def Inqueue(self,data):
        if self.Empty():
            self.first = self.last = Nodo(data)
            return
        aux=self.first
        while aux:
            if aux.next == None:
                aux.next = self.last = Nodo(data)
                self.last.prev = aux
                return
            aux = aux.next
    def Dequeue(self):
        aux = self.first
        if self.last == aux:
            print("Ultima orden pendiente")
            self.first = self.last = None
            return aux
        else:
            self.first = aux.next
            self.first.prev = None
            return aux
    def travelCola(self):
        listCola = []
        aux = self.first
        while aux:
            listCola.append(aux)
            aux = aux.next
        return listCola
Ordenes = Cola()
def Menu():
    print("Menu Principal")
    print("1. Agregar Orden")
    print("2. Entregar Orden")
    print("3. Mostrar Ordenes")
    print("4. Mostrar datos del estudiatne")
    print("5. Salida")
    option = input()
    if option == "1":
        clearConsole()
        AddOrden()
    elif option == "2":
        clearConsole()
        OutOrden()
    elif option == "3":
        clearConsole()
        ShowOrden()
    elif option == "4":
        clearConsole()
        DataStudent()
        Menu()
    elif option == "5":
        clearConsole()
        exit()
    else:
        clearConsole()
        print("Debe de ingresar alguna opcion valida.")
        input()
        clearConsole()
        Menu()
def AddOrden():
    print("Agregar Orden")
    print("Ingrese el ingrediente")
    Igr = input()
    if Igr == "":
        clearConsole()
        Menu()
    Ordenes.Inqueue(Igr)
    clearConsole()
    print("Para agregar otra orden presione enter")
    print("Culquier tecla para regresar al Menu")
    op = input()
    if op != "":
        clearConsole()
        Menu()
    else:
        clearConsole()
        AddOrden() 
def OutOrden():
    if Ordenes.Empty():
        print("No hay ordenes pendientes")
        input()
        clearConsole()
        Menu()
    Ord = Ordenes.Dequeue()
    print("Pizza de "+str(Ord.data)+" entregada")
    input()
    clearConsole()
    Menu()
def ShowOrden():
    if Ordenes.Empty():
        print("No hay ordenes pendientes")
        input()
        clearConsole()
        Menu()
    ls = Ordenes.travelCola()
    n = 1
    for i in ls:
        print(str(n)+"Orden: Pizza de "+str(i.data))
    input()
    clearConsole()
    Menu()
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
def DataStudent():
    print("Erick Daniel Ajche Hernandez")
    print("201701043")
    print("Introduccion a la Programacion y computacion seccion D")
    print("Ingenieria en Ciencias y Sistemas")
    print("4to Semestre")
    input()
    clearConsole()
    return
Menu()