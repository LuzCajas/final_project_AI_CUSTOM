# Sprint 1 — Planificación

## Datos del Sprint
- **Duración:** 1 día
- **Objetivo:** Implementar `ContextStore` en memoria con su API completa y pruebas unitarias, sentando la base para la integración CAG.

## Sprint Backlog

| ID | Tarea | Responsable | Estado |
|---|---|---|---|
| HU-1.1 | Implementar `ContextStore.save(user_id, key, value)` en `backend/context_store.py` | Estudiante | Pendiente |
| HU-1.2 | Implementar `ContextStore.list_for_user(user_id)` en `backend/context_store.py` | Estudiante | Pendiente |
| HU-4.1 | Escribir pruebas unitarias para `ContextStore` en `tests/test_context_store.py` | Estudiante | Pendiente |
| HU-6.1 | Crear backlog y planificación Sprint 1 | Estudiante | Pendiente |

## Criterios de aceptación del Sprint
1. `ContextStore.save()` almacena pares clave-valor por usuario sin errores.
2. `ContextStore.list_for_user()` devuelve la lista de contexto de un usuario.
3. Las pruebas unitarias del ContextStore pasan.
4. Las pruebas base del proyecto (`test_base_api.py`) siguen pasando (no hay regresión).

## Daily Standup
- Se documentará en el archivo `sprint_1_execution.md`.
