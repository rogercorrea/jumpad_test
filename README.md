# Task Jumped.ai - Sanic + React

Aplicação simples de lista de tarefas (To-Do List) com backend em Sanic (Python) e PostgreSQL, e frontend em React com Vite.

---

## Tecnologias

- **Backend:** Python 3.11, Sanic, SQLAlchemy (async), asyncpg, sanic-cors  
- **Frontend:** React 18, TypeScript, Vite, Axios  
- **Banco de Dados:** PostgreSQL (docker)

---

## Estrutura do Projeto

```project/
├── backend/
│ ├── app/
│ │ ├── controllers/
│ │ │ └── task_controller.py
│ │ ├── services/
│ │ │ └── task_service.py
│ │ ├── repositories/
│ │ │ └── task_repository.py
│ │ ├── models/
│ │ │ └── task_model.py
│ │ ├── db.py
│ │ ├── config.py
│ │ └── main.py
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/
│ ├── apps/
│ │ ├── tasks/
│ │ │ ├── components/
│ │ │ ├── pages/
│ │ │ │ └── TaskList.tsx
│ │ │ ├── services/
│ │ │ │ └── api.ts
│ │ │ └── main.tsx
│ ├── shell/
│ │ └── index.html
│ ├── Dockerfile
│ └── package.json
├── docker-compose.yml
└── README.md
```

### Requisitos

- Docker e Docker Compose instalados
- Node.js e npm (para rodar frontend localmente, opcional se usar Docker)
