def apply_context(user_id, question, base_answer, context_items):
    if not context_items:
        return base_answer, []

    context_used = []
    extra_parts = []

    for item in context_items:
        key = item["key"]
        value = item["value"]
        context_used.append(key)

        if key == "audience":
            extra_parts.append(f"Explicado pensando en: {value}")
        elif key == "preferred_style":
            extra_parts.append(f"Estilo: {value}")
        else:
            extra_parts.append(f"Contexto ({key}): {value}")

    if extra_parts:
        base_answer = base_answer.rstrip(".") + ". (" + "; ".join(extra_parts) + ")."

    return base_answer, context_used
