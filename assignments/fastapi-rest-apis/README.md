# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a construir uma API REST usando o framework FastAPI, criando endpoints para consultar, cadastrar, atualizar e remover tarefas. Pratique também validação de dados com modelos Pydantic e códigos de status HTTP.

## 📝 Tarefas

### 🛠️ Criar Endpoints de Consulta

#### Descrição

Complete a aplicação FastAPI para disponibilizar uma lista de tarefas e permitir a consulta de uma tarefa específica pelo seu identificador.

#### Requisitos

O programa concluído deve:

- Criar uma aplicação FastAPI na variável `app`.
- Implementar `GET /tasks` para retornar todas as tarefas cadastradas.
- Implementar `GET /tasks/{task_id}` para retornar uma tarefa pelo identificador.
- Retornar status `404` quando o identificador não existir.
- Iniciar a aplicação com um servidor ASGI, como o Uvicorn.

### 🛠️ Adicionar Criação e Validação de Tarefas

#### Descrição

Adicione um modelo Pydantic para representar os dados de uma tarefa e implemente um endpoint para cadastrar novas tarefas por meio de uma requisição JSON.

#### Requisitos

O programa concluído deve:

- Definir um modelo `TaskCreate` com os campos `title` e `completed`.
- Validar que `title` seja obrigatório e não esteja vazio.
- Implementar `POST /tasks` para criar uma tarefa e adicioná-la à lista em memória.
- Gerar um identificador único para cada nova tarefa.
- Retornar a tarefa criada com status `201`.

Exemplo de requisição:

```json
{
  "title": "Estudar FastAPI",
  "completed": false
}
```

### 🛠️ Implementar Atualização e Remoção

#### Descrição

Complete a API com operações para atualizar o status de uma tarefa e removê-la pelo identificador.

#### Requisitos

O programa concluído deve:

- Implementar `PATCH /tasks/{task_id}` para atualizar os dados permitidos de uma tarefa.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa existente.
- Retornar status `404` quando a tarefa informada não existir.
- Retornar a tarefa atualizada após uma alteração bem-sucedida.
- Retornar status `204` ao remover uma tarefa com sucesso.
