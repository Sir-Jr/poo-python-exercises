class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def status(self):
        media = self.calcular_media()
        return "Aprovado" if media >= 7.0 else "Reprovado"


class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria


if __name__ == "__main__":
    pass
