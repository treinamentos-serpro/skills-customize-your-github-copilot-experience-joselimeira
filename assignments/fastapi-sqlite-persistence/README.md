# 📘 Atividade: Persistência de Dados com FastAPI e SQLite

## 🎯 Objetivo

Aprenda a substituir dados armazenados apenas em memória por uma camada de persistência usando SQLite, SQLAlchemy e FastAPI. Ao final, a API de tarefas continuará funcionando depois de ser reiniciada.

## 📝 Tarefas

### 🛠️ Configurar o Banco de Dados

#### Descrição

Configure o SQLite e o SQLAlchemy para que a aplicação tenha uma tabela capaz de armazenar as tarefas da API.

#### Requisitos

O programa concluído deve:

- Criar um engine SQLAlchemy apontando para um arquivo SQLite local.
- Definir uma classe de modelo `Task` com os campos `id`, `title` e `completed`.
- Criar a tabela automaticamente quando a aplicação iniciar.
- Configurar uma sessão de banco para ser usada pelos endpoints.

Para instalar as dependências, use:

```bash
pip install fastapi uvicorn sqlalchemy
```

### 🛠️ Persistir Consultas e Novas Tarefas

#### Descrição

Atualize os endpoints de consulta e criação para ler e gravar dados no SQLite em vez de usar diretamente uma lista em memória.

#### Requisitos

O programa concluído deve:

- Implementar `GET /tasks` consultando as tarefas no banco de dados.
- Implementar `GET /tasks/{task_id}` usando o identificador da tarefa.
- Implementar `POST /tasks` salvando uma nova tarefa no banco.
- Confirmar as alterações com `commit()` e recarregar o objeto salvo.
- Retornar status `404` quando uma tarefa não existir.

### 🛠️ Atualizar e Remover Dados Persistidos

#### Descrição

Complete a API implementando as operações de atualização e remoção diretamente na tabela SQLite.

#### Requisitos

O programa concluído deve:

- Implementar `PATCH /tasks/{task_id}` e persistir as alterações da tarefa.
- Implementar `DELETE /tasks/{task_id}` e remover a tarefa do banco.
- Confirmar as operações de atualização e remoção com `commit()`.
- Fechar ou liberar a sessão do banco ao final de cada requisição.
- Manter os códigos de status `404`, `204` e `201` definidos pela API.
