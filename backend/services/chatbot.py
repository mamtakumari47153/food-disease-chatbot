def generate_response(labels):
    if not labels:
        return "I couldn't detect anything."

    label = labels[0].lower()

    if "fresh" in label:
        return "✅ The food is fresh and safe to eat."

    elif "rotten" in label:
        return "⚠️ The food is rotten and not safe to eat."

    return f"I detected: {label}"