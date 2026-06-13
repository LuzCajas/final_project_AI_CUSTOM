# Proyecto Examen Final - Módulo 3 — Integración CAG

## Descripción

Sistema monolítico con frontend web, backend HTTP y recuperación de conocimiento tipo RAG. Se implementó un módulo **CAG (Context-Augmented Generation)** que guarda, recupera y utiliza contexto persistente de usuario para mejorar las respuestas del asistente.

## Estructura del proyecto

| Ruta | Contenido |
|---|---|
| `backend/` | Código del servidor y lógica del asistente |
| `backend/server.py` | Servidor HTTP con endpoints REST |
| `backend/assistant.py` | Lógica de respuesta que integra RAG + CAG |
| `backend/context_store.py` | Almacenamiento de contexto en memoria por usuario |
| `backend/cag.py` | Módulo CAG: aplica contexto a respuestas |
| `backend/knowledge.py` | Recuperación RAG desde base de conocimiento |
| `frontend/` | Interfaz web estática |
| `data/` | Base de conocimiento inicial |
| `tests/base/` | Pruebas base del proyecto |
| `tests/validation/` | Pruebas de validación del contrato CAG |
| `tests/test_context_store.py` | Pruebas unitarias del ContextStore |
| `docs/scrum/` | Artefactos Scrum (backlog, sprints, retrospectivas) |
| `docs/evidencias/` | Capturas del proceso y verificación |
| `PROMPTS.md` | Registro cronológico de uso de IA |

## Inicio rápido

### Prerrequisitos
- Python 3.8+
- Windows (PowerShell) o Linux/Mac

### 1. Ejecutar pruebas base
```powershell
$env:PYTHONPATH="."; python -m unittest discover -s tests/base -p "test_*.py" -v
```

### 2. Ejecutar pruebas de validación CAG
```powershell
$env:PYTHONPATH="."; python -m unittest discover -s tests/validation -p "test_*.py" -v
```

### 3. Ejecutar pruebas unitarias del ContextStore
```powershell
$env:PYTHONPATH="."; python -m unittest tests.test_context_store -v
```

### 4. Levantar backend
```powershell
$env:PYTHONPATH="."; python -m backend.server
```
Backend disponible en `http://127.0.0.1:8000`.

### 5. Abrir frontend
Abra `frontend/index.html` en un navegador.

### 6. Validación final
```powershell
.\test.sh
```
o directamente:
```powershell
$env:PYTHONPATH="."; python -m unittest discover -s tests/validation -p "test_*.py" -v
$env:PYTHONPATH="."; python -m unittest discover -s tests/base -p "test_*.py" -v
$env:PYTHONPATH="."; python -m unittest tests.test_context_store -v
```

## Módulo CAG — Arquitectura

### Flujo de una pregunta con CAG

```
Usuario -> POST /api/ask {user_id, question}
  |
  v
assistant.answer_question(user_id, question, context_store)
  |
  +---> knowledge.retrieve_snippets(question)  [RAG]
  |       Busca términos en la base de conocimiento
  |       Retorna fragmentos relevantes
  |
  +---> context_store.list_for_user(user_id)   [CAG]
  |       Recupera contexto guardado del usuario
  |       Retorna lista de {key, value}
  |
  +---> cag.apply_context(user_id, question, base_answer, context_items)
  |       Modifica la respuesta según el contexto
  |       Retorna (answer_modificada, context_used[])
  |
  v
Response: {answer, sources, context_used}
```

### Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/health` | Estado del servidor |
| POST | `/api/ask` | Hacer pregunta (con contexto CAG) |
| GET | `/api/context?user_id=X` | Recuperar contexto del usuario |
| POST | `/api/context` | Guardar contexto del usuario |

### Ejemplos de uso

**Guardar contexto:**
```powershell
curl -X POST http://127.0.0.1:8000/api/context `
  -H "Content-Type: application/json" `
  -d '{"user_id": "ana", "key": "audience", "value": "explicar como principiante"}'
```

**Preguntar con contexto:**
```powershell
curl -X POST http://127.0.0.1:8000/api/ask `
  -H "Content-Type: application/json" `
  -d '{"user_id": "ana", "question": "Que es CAG?"}'
```

### Decisiones técnicas

- **ContextStore**: almacenamiento en memoria con diccionario `{user_id: {key: value}}`. Aislado por usuario.
- **apply_context**: función pura que recibe contexto y modifica la respuesta. Soporta claves como `audience` y `preferred_style`, con fallback genérico para cualquier otra clave.
- **Separación de responsabilidades**: `context_store` maneja persistencia, `cag` maneja lógica de modificación de respuesta, `assistant` orquesta ambos.
- **Sin dependencias externas**: todo usa la biblioteca estándar de Python (`http.server`, `json`, `unittest`).

## Metodología Scrum

El proyecto se organizó en 2 sprints:

| Sprint | Objetivo | Historias | Estado |
|---|---|---|---|
| Sprint 1 | Implementar ContextStore + pruebas unitarias | HU-1, HU-4, HU-6 | Completado |
| Sprint 2 | Integración CAG completa + validación + entrega | HU-2, HU-3, HU-5, HU-7, HU-8, HU-9 | Completado |

Artefactos Scrum en `docs/scrum/`:
- `product_backlog.md` — Backlog completo con 9 historias
- `sprint_1_planning.md`, `sprint_1_execution.md`, `sprint_1_review.md`
- `sprint_2_planning.md`, `sprint_2_execution.md`, `sprint_2_review.md`

## Evidencias

Capturas del proceso en `docs/evidencias/`.

## PROMPTS.md

Registro cronológico de uso de IA disponible en `PROMPTS.md`.
