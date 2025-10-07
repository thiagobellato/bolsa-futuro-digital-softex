class MinhaClasse():
    def __init__(self) -> None:
        self.__idade = None
        self.__nome = None
        
    def setter(self,idade: int,nome: str) -> None:
        self.__idade = idade
        self.__nome = nome
        
    def getter(self) -> int:
        return self.__idade,self.__nome
        
classe1 = MinhaClasse()
classe1.setter(14,"João")
valor = classe1.getter()
print(valor)

classe2 = MinhaClasse()
classe2.setter(7,"Lucas")
valor = classe2.getter()
print(valor)

classe3 = MinhaClasse()
classe3.setter(95,"Marcos")
valor = classe3.getter()
print(valor)
