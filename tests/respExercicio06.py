from respExercicio01 import Disciplina

class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.disciplinas = []  
    def adicionar_disciplina(self, disciplina):
        if isinstance(disciplina, Disciplina):
            self.disciplinas.append(disciplina)
        else:
            print("Erro: objeto deve ser uma instância de Disciplina.")

    def listar_disciplinas(self):
        print(f"=== Disciplinas do Curso: {self.nome} ===")
        for disc in self.disciplinas:
            print(f"- {disc.nome} ({disc.codigo})")

    def carga_horaria_total(self):
        total = 0
        for disc in self.disciplinas:
            total += disc.carga_horaria
        return total
