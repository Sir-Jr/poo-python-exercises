class Departamento:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.professores = []  
        
    @classmethod
    def criar_departamento_exatas(cls, nome):
        return cls(nome, "EXA")

    @classmethod
    def criar_departamento_humanas(cls, nome):
        return cls(nome, "HUM")

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def listar_professores(self):
        print(f"=== Professores do Departamento {self.nome} ({self.sigla}) ===")
        if not self.professores:
            print("Nenhum professor cadastrado.")
            return
        
        for prof in self.professores:
            print(f"- {prof.nome}")
