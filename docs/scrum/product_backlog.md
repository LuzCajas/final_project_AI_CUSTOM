# Product Backlog — Módulo CAG (Context-Augmented Generation)

## Épica
Integrar un módulo CAG que guarde, recupere y utilice contexto persistente de usuario para mejorar las respuestas del asistente.

## Historias de Usuario

| ID | Historia | Prioridad | Estimación | Dependencias | Sprint |
|---|---|---|---|---|---|
| HU-1 | Como usuario, quiero que el sistema guarde contexto sobre mí (clave-valor) para que recuerde preferencias entre sesiones | Alta | 2 | — | Sprint 1 |
| HU-2 | Como usuario, quiero que el sistema use mi contexto guardado para personalizar las respuestas que recibo | Alta | 3 | HU-1 | Sprint 2 |
| HU-3 | Como desarrollador, quiero que el endpoint `/api/context` funcione correctamente (GET y POST) para integrar el frontend | Alta | 1 | HU-1 | Sprint 2 |
| HU-4 | Como desarrollador, quiero pruebas unitarias y de contrato que validen el módulo CAG para garantizar calidad | Alta | 2 | HU-1, HU-2 | Sprint 1 y 2 |
| HU-5 | Como usuario, quiero que el sistema combine conocimiento RAG con contexto CAG para respuestas más ricas | Media | 2 | HU-2 | Sprint 2 |
| HU-6 | Como desarrollador, quiero documentación Scrum completa del proceso para auditoría académica | Media | 1 | — | Sprint 1 y 2 |
| HU-7 | Como desarrollador, quiero un PR revisado y fusionado para mantener la integridad del repositorio | Media | 1 | HU-1, HU-2 | Sprint 2 |
| HU-8 | Como evaluador, quiero un README actualizado y PROMPTS.md cronológico para entender el trabajo | Media | 1 | HU-6 | Sprint 2 |
| HU-9 | Como evaluador, quiero que la validación final pase para certificar la entrega | Alta | 1 | HU-2, HU-3, HU-4 | Sprint 2 |

## Criterios de aceptación generales
- Todo el código debe mantener el estilo existente del proyecto (Python sin tipado forzado, http.server).
- Las pruebas base deben seguir pasando después de la integración.
- Las pruebas de validación (`tests/validation/test_cag_contract.py`) deben pasar completamente.
- El contexto debe persistir en memoria durante la vida del servidor.
