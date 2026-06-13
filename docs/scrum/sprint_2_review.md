# Sprint 2 — Sprint Review & Retrospective

## Resultados
- `apply_context()` implementado en `cag.py`: modifica la respuesta según contexto del usuario
- `assistant.py` integrado con `ContextStore` y `apply_context()`
- `server.py` conectado pasando `context_store` a `answer_question()`
- **3/3 pruebas de validación CAG pasan** ✅
- **3/3 pruebas base siguen pasando** ✅ (sin regresión)
- **8/8 pruebas unitarias ContextStore pasan** ✅
- PR creado, revisado y fusionado a main
- README.md actualizado con documentación técnica
- PROMPTS.md completo con todas las entradas cronológicas

## Historias completadas
- HU-2: apply_context implementado ✓
- HU-3: Endpoints /api/context funcionales ✓
- HU-4: Pruebas unitarias y de validación completas ✓
- HU-5: RAG + CAG combinados correctamente ✓
- HU-6: Documentación Scrum completa ✓
- HU-7: PR creado, revisado y mergeado ✓
- HU-8: README.md y PROMPTS.md actualizados ✓
- HU-9: Validación final ejecutada ✓

## Retrospectiva

**¿Qué funcionó bien?**
- Integración limpia: solo 3 archivos modificados para la integración CAG.
- TDD real: pruebas escritas primero (ContextStore), código después.
- Commits incrementales con avance visible.

**¿Qué mejorar?**
- Podrían agregarse más tipos de contexto además de "audience".
- El almacenamiento en memoria podría migrarse a persistencia (archivo/BD) en el futuro.

**Lecciones aprendidas**
- La arquitectura del proyecto base facilitó la integración gracias a la separación clara de responsabilidades (context_store, cag, assistant, knowledge).
- Las pruebas de validación funcionaron como contrato de integración, guiando la implementación.
