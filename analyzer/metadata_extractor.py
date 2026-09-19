def extract_metadata(dataset, source):
    card = dataset.cardData or {}
    return {
        "name": dataset.id,
        "source": source,
        "description": card.get("description", ""),
        "downloads": getattr(dataset, "downloads", 0),
        "likes": getattr(dataset, "likes", 0),
        "tags": getattr(dataset, "tags", []),
        "languages": card.get("language", []),
        "license": card.get("license", ""),
        "task": card.get("task_categories", [])
    }