# Relatório Técnico – Correções dos 7 Erros Identificados

## Erro 1 – Nome da classe fora da convenção
**Problema:** A classe estava nomeada como `pessoa`, violando a convenção PascalCase usada para classes.  
**Correção:** Renomeada para `Pessoa`.  
**Princípio de POO:** Boas práticas de modelagem e nomenclatura.

---

## Erro 2 – Atributo `nome` não atribuído ao objeto
**Problema:** No construtor havia a linha `nome = nome`, que não atribui valor ao objeto.  
**Correção:** Substituído por `self.nome = nome`.  
**Princípio de POO:** Encapsulamento e inicialização correta.

---

## Erro 3 – Atributo privado `__cpf` declarado incorretamente
**Problema:** O uso de `__cpf` ativa name mangling sem necessidade, dificultando o acesso ao atributo.  
**Correção:** Alterado para `_cpf`, mantendo proteção sem complicar o código.  
**Princípio de POO:** Encapsulamento aplicado corretamente.

---

## Erro 4 – Método `apresentar()` sem parâmetro `self`
**Problema:** Declarado como `def apresentar():`, o método não conseguia acessar os atributos da instância.  
**Correção:** Alterado para `def apresentar(self):`.  
**Princípio de POO:** Estrutura correta de métodos de instância.

---

## Erro 5 – Construtor da classe Estudante ignorando a herança
**Problema:** O construtor atribuía nome e idade manualmente, sem usar `super()`, quebrando o fluxo correto da herança.  
**Correção:** Alterado para `super().__init__(nome, idade)`.  
**Princípio de POO:** Herança e reutilização de código.

---

## Erro 6 – Possível divisão por zero em `calcular_media()`
**Problema:** Caso a lista de notas estivesse vazia, `sum(self.notas) / len(self.notas)` geraria erro.  
**Correção:** Adicionada validação:
```python
if len(self.notas) == 0:
    return 0
```
**Princípio de POO:** Robustez e segurança lógica.

---

## Erro 7 – Chamada de `calcular_media()` sem garantir que existem notas
**Problema:** No teste final, `calcular_media()` era chamado mesmo sem notas adicionadas, o que antes causava erro por divisão por zero.  
**Correção:** Com a correção do Erro 6, o método agora retorna 0 quando não há notas, evitando falhas na execução.  
**Princípio de POO:** Robustez, lógica de negócio consistente e prevenção de estados inválidos.

---

# Conclusão
As correções alinham o código com princípios fundamentais da Programação Orientada a Objetos, garantindo funcionamento estável, seguro e bem estruturado.
