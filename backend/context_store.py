class ContextStore:
    def __init__(self):
        self._data = {}

    def _ensure_user(self, user_id):
        if user_id not in self._data:
            self._data[user_id] = {}

    def save(self, user_id, key, value):
        self._ensure_user(user_id)
        self._data[user_id][key] = value
        return True

    def list_for_user(self, user_id):
        user_context = self._data.get(user_id, {})
        return [{"key": k, "value": v} for k, v in user_context.items()]

    def get(self, user_id, key, default=None):
        user_context = self._data.get(user_id, {})
        return user_context.get(key, default)
