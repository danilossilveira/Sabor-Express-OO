# POO - Sabor Express 🍽️

Este repositório contém implementações simples de classes para gerenciar restaurantes em Python, além de uma lista de desafios para você praticar Programação Orientada a Objetos (POO).

## Estrutura do projeto

- `app.py` — contém a classe `Restaurante` e algumas instâncias de exemplo.
- `Exercicios1/Restaurantes.py` — versão simples da classe `Restaurantes` usada para exercícios iniciais.

---

## ✅ Como usar

1. Abra o projeto no seu editor de preferência (VS Code).
2. Execute `app.py` para ver a saída atual:

```bash
python app.py
```

3. Escolha um desafio da lista abaixo e me diga qual quer que eu implemente, ou tente resolver sozinho(a) e peça dicas quando precisar.

---

## 🎯 Desafios (do fácil ao avançado)

### 🔰 Nível Fácil
1. **Método `ativar()` e `desativar()`**
   - Implemente métodos de instância que mudem `self.ativo` para `True` e `False`.
   - Teste criando um restaurante, chamando `ativar()` e verificando `restaurante.ativo`.

2. **Representação curta (`__repr__`)**
   - Implemente `__repr__` para mostrar `Restaurante(nome, categoria)` de forma legível.
   - Teste imprimindo uma lista de objetos.

3. **Função `listar_restaurantes()` aprimorada**
   - Altere a função para aceitar um parâmetro opcional `ativos_only=False`. Se `True`, lista apenas restaurantes ativos.
   - Teste com restaurantes ativos e inativos.

---

### 🛠️ Nível Intermediário
4. **Busca por nome e categoria**
   - Adicione métodos de classe: `buscar_por_nome(nome)` e `buscar_por_categoria(categoria)` que retornem listas correspondentes (case-insensitive).

5. **Remover restaurante**
   - Implemente método de instância `remover()` que o elimine de `Restaurante.restaurantes`.

6. **Atualizar atributos**
   - Adicione método `atualizar(nome=None, categoria=None)` para alterar atributos somente se parâmetros forem dados.

---

### 🚀 Nível Avançado
7. **Persistência simples (JSON)**
   - Adicione métodos `salvar_em_arquivo(path)` (classe) e `carregar_de_arquivo(path)` que serializem/deserializem a lista de restaurantes para JSON.

8. **Unicidade de nome**
   - Evite criar dois restaurantes com o mesmo `nome` (levante uma exceção customizada se necessário).

9. **Menu (composição)**
   - Crie uma classe `Prato(nome, preco)` e adicione à `Restaurante` uma lista de pratos com métodos `adicionar_prato`, `remover_prato`, `listar_cardapio` e `buscar_prato_por_nome`.

10. **Ordenação e filtros**
    - Métodos de classe para ordenar restaurantes por nome ou categoria e para filtrar por categoria.

11. **Cobertura com testes unitários**
    - Crie testes com `unittest` ou `pytest` para cobrir criação, ativação, buscas, persistência e manipulação de cardápio.

12. **API simples (opcional)**
    - Exponha endpoints com Flask ou FastAPI para listar, criar, atualizar e remover restaurantes.

---

## 💡 Dicas

- Use `@property` para expor `ativo` com validação.
- Considere `dataclasses` para `Prato`.
- Para persistência mais robusta, use SQLite (`sqlite3`).

---

## Próximos passos

- Escolha um desafio que você quer que eu implemente e eu faço a alteração aqui no repositório (posso também adicionar testes). 🔧

---

Quer que eu implemente algum desses desafios agora? 😊
