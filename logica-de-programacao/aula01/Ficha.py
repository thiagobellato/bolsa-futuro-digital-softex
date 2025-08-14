from datetime import date

data = date.today()
nome = "Thiago"
sobrenome = "Bellato"
curso = "BFD Back-End (Python)"

print(
    f"Hello World, my name is {nome} {sobrenome}. Today is {data:%d/%m/%Y}, the first day of class in the {curso} course!!"
)
