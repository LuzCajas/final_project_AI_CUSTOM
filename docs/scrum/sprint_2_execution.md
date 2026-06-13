# Sprint 2 — Ejecución

## Daily Standup 1
**Fecha:** 2026-06-12

**¿Qué hice ayer?**
- Sprint 1 completado: ContextStore implementado y pruebas unitarias pasando
- Scrum docs del Sprint 1 creados

**¿Qué haré hoy?**
- Implementar `apply_context()` en `cag.py`
- Integrar en `assistant.py` y `server.py`
- Hacer pasar pruebas de validación
- Crear PR y fusionar a main
- Actualizar README.md y PROMPTS.md
- Preparar evidencias

**¿Hay impedimentos?**
- Ninguno.

## Commits realizados
- `feat: implement apply_context in cag.py and integrate with assistant`
- `docs: add sprint 2 planning, execution, and review docs`
- `docs: update README.md, PROMPTS.md and final documentation`

## Sprint 2 - Resultados de pruebas

### Pruebas base (sin regresión)
```
test_ask_answers_from_knowledge_base ... ok
test_ask_requires_user_and_question ... ok
test_health_returns_ok ... ok
```

### Pruebas de validación CAG
```
test_saves_context_for_user ... ok
test_retrieves_context_for_user ... ok
test_ask_uses_context_to_influence_later_response ... ok
```

### Pruebas unitarias ContextStore
```
test_get_returns_default_when_missing ... ok
test_get_returns_value ... ok
test_list_for_user_returns_all_items ... ok
test_list_for_user_returns_empty_list_when_no_context ... ok
test_overwrite_existing_key ... ok
test_save_and_list_for_user ... ok
test_save_returns_true ... ok
test_users_are_isolated ... ok
```
