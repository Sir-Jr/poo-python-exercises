from respExercicio02 import Aluno
from respExercicio01 import Disciplina

class Secretaria:

    @staticmethod
    def inscrever_aluno(aluno, disciplina):
        if disciplina not in aluno.disciplinas_inscritas:
            aluno.disciplinas_inscritas.append(disciplina)

        if aluno not in disciplina.alunos_matriculados:
            disciplina.alunos_matriculados.append(aluno)

class Aluno(Aluno):  
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula, curso)
        self.disciplinas_inscritas = []  

    def listar_disciplinas(self):
        print(f"=== Disciplinas inscritas de {self.nome} ===")
        if not self.disciplinas_inscritas:
            print("Nenhuma disciplina inscrita.")
            return
        for disc in self.disciplinas_inscritas:
            print(f"- {disc.nome} ({disc.codigo})")

class Disciplina(Disciplina):  
    def __init__(self, nome, codigo, carga_horaria):
        super().__init__(nome, codigo, carga_horaria)
        self.alunos_matriculados = []  

    def listar_alunos(self):
        print(f"=== Alunos matriculados em {self.nome} ===")
        if not self.alunos_matriculados:
            print("Nenhum aluno matriculado.")
            return
        for aluno in self.alunos_matriculados:
            print(f"- {aluno.nome} ({aluno.matricula})")
