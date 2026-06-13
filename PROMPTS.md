# PROMPTS.md — Registro de uso de IA

> Cada entrada documenta el uso relevante de IA en orden cronológico.
> Formato: objetivo del prompt, prompt usado, resumen de la respuesta recibida,
> decisión humana tomada, cambios realizados en el proyecto y verificación aplicada.

---

## Entrada 1 — 2026-06-12

### Objetivo del prompt
Entender cómo ejecutar las pruebas base del proyecto y confirmar que pasan antes de iniciar la implementación (Paso 3 de las instrucciones).

### Prompt usado
"Primero, explicame como hacer esta parte 3. Ejecute las pruebas base y confirme que pasan antes de implementar."

### Resumen de la respuesta recibida
El asistente explicó que el proyecto tiene dos suites de pruebas:
- `tests/base/test_base_api.py` (pruebas base que deben pasar)
- `tests/validation/test_cag_contract.py` (pruebas de validación CAG que deben fallar porque el módulo CAG es placeholder)

También proporcionó los comandos exactos para ejecutar cada suite en PowerShell:
```powershell
$env:PYTHONPATH="."; python -m unittest discover -s tests/base -p "test_*.py" -v
$env:PYTHONPATH="."; python -m unittest discover -s tests/validation -p "test_*.py" -v
```

Adicionalmente, detalló la estructura del proyecto: backend con servidor HTTP, knowledge.py para RAG básico, context_store.py y cag.py como placeholders, y frontend estático.

### Decisión humana tomada
Se decidió ejecutar las pruebas base manualmente para verificar que el proyecto base funciona correctamente antes de cualquier modificación, siguiendo el principio de TDD de confirmar que las pruebas existentes pasan.

### Cambios realizados en el proyecto
Ninguno. Solo exploración y lectura del código fuente para entender la arquitectura existente.

### Verificación aplicada
El usuario confirmó: "genial, ya lo realice yo, gracias por la explicacion", indicando que las pruebas base se ejecutaron exitosamente de forma manual.

---

## Entrada 2 — 2026-06-12

### Objetivo del prompt
Organizar el trabajo con metodología Scrum usando al menos 2 sprints (Paso 4 de las instrucciones).

### Prompt usado
"Te propongo el siguiente plan para organizar el trabajo con Scrum: [lista de backlog con 9 historias de usuario distribuidas en 2 sprints]"

### Resumen de la respuesta recibida
El asistente propuso un plan completo con:
- 9 historias de usuario en el product backlog
- Sprint 1: ContextStore en memoria y pruebas unitarias
- Sprint 2: Integración CAG completa (apply_context, assistant, validación, PR, documentación)
- Cada sprint con criterios de aceptación claros

### Decisión humana tomada
Se aceptó la planificación propuesta y se procedió a crear los artefactos Scrum: product backlog, sprint planning, execution docs y sprint review.

### Cambios realizados en el proyecto
- Creación de `docs/scrum/product_backlog.md` con 9 historias de usuario priorizadas
- Creación de `docs/scrum/sprint_1_planning.md` con sprint backlog del Sprint 1
- Creación de `docs/scrum/sprint_1_execution.md` con daily standup
- Creación de `docs/scrum/sprint_1_review.md` con resultados y retrospectiva

### Verificación aplicada
Los archivos se crearon y se confirmó visualmente su contenido. Se referencian desde el README.

---

## Entrada 3 — 2026-06-12

### Objetivo del prompt
Implementar el módulo ContextStore en memoria con pruebas unitarias (Sprint 1).

### Prompt usado
El usuario aceptó la planificación y se procedió a la implementación del Sprint 1. El asistente propuso implementar:
- `ContextStore.save()` y `ContextStore.list_for_user()` en `backend/context_store.py`
- Pruebas unitarias en `tests/test_context_store.py`
- Además se agregó `ContextStore.get()` para acceso directo

### Resumen de la respuesta recibida
El asistente implementó:
- `context_store.py` con diccionario anidado `{user_id: {key: value}}`
- 8 pruebas unitarias cubriendo: save, list, usuario vacío, múltiples items, aislamiento entre usuarios, overwrite, get con y sin default
- Todas las pruebas pasaron (8/8)
- Pruebas base sin regresión (3/3)

### Decisión humana tomada
Se aceptó la implementación completa. Se decidió agregar el método `get()` como utilidad adicional para acceso directo a contexto.

### Cambios realizados en el proyecto
- Modificado: `backend/context_store.py` (implementación completa)
- Creado: `tests/test_context_store.py` (8 pruebas unitarias)
- Commit: `Sprint 1: implement ContextStore and add unit tests`

### Verificación aplicada
```powershell
$env:PYTHONPATH="."; python -m unittest tests.test_context_store -v
# Resultado: 8 tests OK

$env:PYTHONPATH="."; python -m unittest discover -s tests/base -p "test_*.py" -v
# Resultado: 3 tests OK (sin regresión)
```

---

## Entrada 4 — 2026-06-12

### Objetivo del prompt
Integrar el módulo CAG completo: implementar `apply_context`, conectar con `assistant.py`, y hacer pasar las pruebas de validación (Sprint 2).

### Prompt usado
Se describió el plan del Sprint 2:
1. Implementar `apply_context()` en `cag.py`
2. Modificar `assistant.answer_question()` para recibir y aplicar contexto
3. Conectar `server.py` pasando `context_store`
4. Verificar pruebas de validación CAG

### Resumen de la respuesta recibida
El asistente implementó:
- `cag.py`: función `apply_context()` que recibe context_items, modifica la respuesta añadiendo contexto según key (audience, preferred_style, u otros), y devuelve la respuesta modificada + lista de keys usadas
- `assistant.py`: modificado para aceptar `context_store` opcional, obtener contexto del usuario, y pasarlo a `apply_context()`
- `server.py`: modificado para pasar `context_store` a `answer_question()`

### Decisión humana tomada
Se aceptó la implementación completa. Se decidió que el formato de respuesta modificada fuera: añadir "(Explicado pensando en: {value})" al final de la respuesta base.

### Cambios realizados en el proyecto
- Modificado: `backend/cag.py` (implementación de apply_context)
- Modificado: `backend/assistant.py` (integración con context_store y cag)
- Modificado: `backend/server.py` (pasar context_store a answer_question)
- Creados: `docs/scrum/sprint_2_planning.md`, `sprint_2_execution.md`, `sprint_2_review.md`
- Commit: `Sprint 2: implement CAG integration and pass validation tests`

### Verificación aplicada
```powershell
$env:PYTHONPATH="."; python -m unittest discover -s tests/validation -p "test_*.py" -v
# Resultado: 3 tests OK

$env:PYTHONPATH="."; python -m unittest discover -s tests/base -p "test_*.py" -v
# Resultado: 3 tests OK (sin regresión)

$env:PYTHONPATH="."; python -m unittest tests.test_context_store -v
# Resultado: 8 tests OK
```

---

## Entrada 5 — 2026-06-12

### Objetivo del prompt
Crear PR, actualizar README.md, ejecutar validación final y preparar evidencias.

### Prompt usado
Se solicitó al asistente completar las tareas finales del proyecto: PR, merge, documentación, validación final.

### Resumen de la respuesta recibida
El asistente propuso:
- Crear un Pull Request dentro del fork, revisarlo y fusionarlo a main
- Actualizar README.md con documentación técnica del módulo CAG
- Ejecutar `test.sh` (validación final)
- Tomar capturas de evidencias
- Actualizar PROMPTS.md con esta entrada

### Decisión humana tomada
Se ejecutaron todas las tareas finales según lo planificado.

### Cambios realizados en el proyecto
- Actualizado: `README.md` con documentación técnica, instrucciones y Scrum docs
- Creado: PR, revisado y fusionado a main
- Ejecutada validación final con éxito
- Creadas: capturas de evidencias en `docs/evidencias/`

### Verificación aplicada
```powershell
$env:PYTHONPATH="."; python -m unittest discover -s tests/base -p "test_*.py" -v
# 3 tests OK

$env:PYTHONPATH="."; python -m unittest discover -s tests/validation -p "test_*.py" -v
# 3 tests OK

$env:PYTHONPATH="."; python -m unittest tests.test_context_store -v
# 8 tests OK
```

---

## Entrada 6 — 2026-06-12

### Objetivo del prompt
Agregar pruebas unitarias para la función `apply_context` del módulo CAG (paso 8 de las instrucciones).

### Prompt usado
"dime como hacer las pruebas propias para este inciso" (refiriéndose al paso 8 de implementar integración CAG, agregar pruebas propias y actualizar documentación).

### Resumen de la respuesta recibida
El asistente propuso 5 pruebas unitarias para `tests/test_cag.py`:
- `test_sin_contexto_devuelve_misma_respuesta`: sin contexto, respuesta no cambia
- `test_contexto_audience_modifica_respuesta`: contexto de audiencia se refleja en respuesta
- `test_contexto_preferred_style_se_aplica`: estilo preferido se aplica
- `test_multiples_contextos_se_combinan`: múltiples claves de contexto funcionan juntas
- `test_contexto_generico_fallback`: claves no conocidas usan formato genérico

### Decisión humana tomada
Se aceptó la propuesta completa y se creó el archivo con las 5 pruebas.

### Cambios realizados en el proyecto
- Creado: `tests/test_cag.py` con 5 pruebas unitarias para `apply_context()`
- Commit: `test: agregar pruebas unitarias para apply_context en cag.py`

### Verificación aplicada
```powershell
$env:PYTHONPATH="."; python -m unittest tests.test_cag -v
# Resultado: 5 tests OK
```

---

## Entrada 7 — 2026-06-12

### Objetivo del prompt
Ejecutar validación final y preparar explicación técnica breve de la solución (paso 9 de las instrucciones).

### Prompt usado
"bien, ahora necesito esta parte 9. Ejecute la validación final y prepare una explicación técnica breve de la solución."

### Resumen de la respuesta recibida
El asistente ejecutó la validación completa: 19 pruebas en 4 suites (base, validación CAG, ContextStore, CAG) — todas pasaron. Luego preparó la explicación técnica de la solución.

### Decisión humana tomada
Se ejecutó la validación final y se documentó la explicación técnica en el README.md.

### Cambios realizados en el proyecto
- Actualizado: `PROMPTS.md` con entrada 7
- Actualizado: `README.md` con sección de explicación técnica

### Verificación aplicada
```powershell
$env:PYTHONPATH="."; python -m unittest discover -s tests/base -p "test_*.py" -v
# 3 tests OK

$env:PYTHONPATH="."; python -m unittest discover -s tests/validation -p "test_*.py" -v
# 3 tests OK

$env:PYTHONPATH="."; python -m unittest tests.test_context_store -v
# 8 tests OK

$env:PYTHONPATH="."; python -m unittest tests.test_cag -v
# 5 tests OK
```

---

