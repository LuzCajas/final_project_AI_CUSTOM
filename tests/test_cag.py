import unittest

from backend.cag import apply_context


class TestCagApplyContext(unittest.TestCase):

    def test_sin_contexto_devuelve_misma_respuesta(self):
        respuesta, usado = apply_context("user1", "hola", "respuesta base", [])
        self.assertEqual(respuesta, "respuesta base")
        self.assertEqual(usado, [])

    def test_contexto_audience_modifica_respuesta(self):
        ctx = [{"key": "audience", "value": "explicar como principiante"}]
        respuesta, usado = apply_context("user1", "que es x?", "Respuesta.", ctx)
        self.assertIn("principiante", respuesta.lower())
        self.assertIn("audience", usado)

    def test_contexto_preferred_style_se_aplica(self):
        ctx = [{"key": "preferred_style", "value": "con analogias"}]
        respuesta, usado = apply_context("user1", "que es x?", "Respuesta.", ctx)
        self.assertIn("analogias", respuesta.lower())
        self.assertIn("preferred_style", usado)

    def test_multiples_contextos_se_combinan(self):
        ctx = [
            {"key": "audience", "value": "experto"},
            {"key": "language", "value": "en"},
        ]
        respuesta, usado = apply_context("u1", "que es x?", "Respuesta.", ctx)
        self.assertEqual(len(usado), 2)
        self.assertIn("audience", usado)
        self.assertIn("language", usado)

    def test_contexto_generico_fallback(self):
        ctx = [{"key": "custom_key", "value": "custom_value"}]
        respuesta, usado = apply_context("u1", "que es x?", "Respuesta.", ctx)
        self.assertIn("custom_key", usado)
        self.assertIn("custom_value", respuesta)


if __name__ == "__main__":
    unittest.main()
