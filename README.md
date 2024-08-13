# Dev-Web-Mob-2024-1
Dedicado a projeto da disciplina de Desenvolvimento Web Mobile 2024-1

# Gap’s: Sistema de Gerenciamento de Eventos Esportivos

**Universidade Federal do Tocantins**
**Curso:** Ciência da Computação  
**Disciplina:** Desenvolvimento Web Mobile  
**Prof:** Thiago Magalhães  
**Aluno:** Gabryel Soares Marques  
**Data:** 24/04/2024  

---

## Resumo:

O Gap’s é um projeto desenvolvido para gerenciar eventos esportivos em Palmas-TO. Ele oferece uma plataforma onde os usuários podem fazer login, visualizar os eventos ocorridos na cidade e se inscrever neles.

## Requisitos Funcionais (Iterações):

1. **RF01:** Efetuar login
2. **RF02:** Adicionar evento
3. **RF03:** Pesquisar eventos
4. **RF04:** Exibir detalhes do evento
5. **RF05:** Editar evento
6. **RF06:** Realizar inscrição
7. **RF07:** Cancelar inscrição
8. **RF08:** Deletar evento

### Classes:

#### Usuários
- **Atributos:**
  - `id_usuário`: int
  - `nome`: string
  - `email`: string
  - `senha`: string
- **Métodos:**
  - `login()`
  - `pesquisar_evento()`
  - `visualizar_inscrição()`
  - `realizar_inscrição()`
  - `cancelar_inscrição()`

#### Inscrições
- **Atributos:**
  - `id`: int
  - `id_usuário`: int
  - `id_evento`: int

#### Administradores
- **Atributos:**
  - `id_adm`: int
  - `nome`: string
  - `email`: string
  - `senha`: string
- **Métodos:**
  - `login()`
  - `pesquisa_evento()`
  - `visualizar_detalhe_evento()`
  - `adicionar_evento()`
  - `editar_evento()`
  - `deletar_evento()`

#### Eventos
- **Atributos:**
  - `id_evento`: int
  - `título`: string
  - `descrição`: string
  - `data`: date
  - `hora`: time
  - `local`: string

### Caso de Uso:

1. **Fazer Login:**
   - Ator: Usuário/Administrador
   - Descrição: Permite que o usuário ou administrador faça login no sistema.

2. **Pesquisar Evento:**
   - Ator: Usuário/Administrador
   - Descrição: Permite que o usuário ou administrador pesquise eventos disponíveis no sistema.

3. **Visualizar Detalhes do Evento:**
   - Ator: Usuário/Administrador
   - Descrição: Permite que o usuário ou administrador visualize todos os detalhes de um evento específico.

4. **Cancelar Inscrição:**
   - Ator: Usuário
   - Descrição: Permite que o usuário cancele sua inscrição em um evento específico.

5. **Realizar Inscrição:**
   - Ator: Usuário
   - Descrição: Permite que o usuário se inscreva em um evento específico.

6. **Deletar Evento:**
   - Ator: Administrador
   - Descrição: Permite que o administrador delete um evento existente do sistema.

7. **Adicionar Evento:**
   - Ator: Administrador
   - Descrição: Permite que o administrador adicione um novo evento ao sistema.

8. **Editar Evento:**
   - Ator: Administrador
   - Descrição: Permite que o administrador edite as informações de um evento já existente no sistema.
## Repositório:

[Dev-Web-Mob-2024-1](https://github.com/GabryelMarques/Dev-Web-Mob-2024-1)
