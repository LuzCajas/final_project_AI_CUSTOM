import unittest

from backend.context_store import ContextStore


class TestContextStore(unittest.TestCase):
    def setUp(self):
        self.store = ContextStore()

    def test_save_returns_true(self):
        result = self.store.save("user1", "key1", "value1")
        self.assertTrue(result)

    def test_save_and_list_for_user(self):
        self.store.save("ana", "preferred_style", "explicaciones con analogias")
        items = self.store.list_for_user("ana")
        self.assertIn({"key": "preferred_style", "value": "explicaciones con analogias"}, items)

    def test_list_for_user_returns_empty_list_when_no_context(self):
        items = self.store.list_for_user("unknown")
        self.assertEqual(items, [])

    def test_list_for_user_returns_all_items(self):
        self.store.save("luis", "audience", "principiante")
        self.store.save("luis", "language", "es")
        items = self.store.list_for_user("luis")
        self.assertEqual(len(items), 2)
        self.assertIn({"key": "audience", "value": "principiante"}, items)
        self.assertIn({"key": "language", "value": "es"}, items)

    def test_users_are_isolated(self):
        self.store.save("ana", "style", "analogias")
        self.store.save("luis", "style", "directo")
        ana_items = self.store.list_for_user("ana")
        luis_items = self.store.list_for_user("luis")
        self.assertEqual(len(ana_items), 1)
        self.assertEqual(ana_items[0]["value"], "analogias")
        self.assertEqual(luis_items[0]["value"], "directo")

    def test_overwrite_existing_key(self):
        self.store.save("user1", "key1", "value1")
        self.store.save("user1", "key1", "value2")
        items = self.store.list_for_user("user1")
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["value"], "value2")

    def test_get_returns_value(self):
        self.store.save("user1", "key1", "value1")
        self.assertEqual(self.store.get("user1", "key1"), "value1")

    def test_get_returns_default_when_missing(self):
        self.assertEqual(self.store.get("user1", "missing"), None)
        self.assertEqual(self.store.get("user1", "missing", "fallback"), "fallback")


if __name__ == "__main__":
    unittest.main()
