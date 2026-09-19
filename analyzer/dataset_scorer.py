def score_dataset(info):
    score = 0

    # Safe extraction (avoids NoneType errors)
    name = (info.get("name") or "").lower()
    description = (info.get("description") or "").lower()

    text = name + " " + description

    # -------------------------
    # Indian relevance
    # -------------------------
    INDIAN_KEYWORDS = [
        "india",
        "indian",
        "bharat",
        "ai4bharat",
        "ifnd"
    ]

    # -------------------------
    # Languages
    # -------------------------
    LANGUAGE_KEYWORDS = [
        "hindi",
        "english",
        "hinglish",
        "code mixed",
        "code-mixed",
        "tamil"
    ]

    # -------------------------
    # Fake news related
    # -------------------------
    FAKE_NEWS_KEYWORDS = [
        "fake",
        "real",
        "misinformation",
        "disinformation",
        "fact",
        "fact check",
        "fact checking",
        "claim",
        "verification",
        "rumor",
        "rumour",
        "news"
    ]

    # -------------------------
    # Scoring
    # -------------------------

    # Indian datasets are the highest priority
    for word in INDIAN_KEYWORDS:
        if word in text:
            score += 20

    # Language relevance
    for word in LANGUAGE_KEYWORDS:
        if word in text:
            score += 15

    # Fake news / fact checking relevance
    for word in FAKE_NEWS_KEYWORDS:
        if word in text:
            score += 10

    # Bonus if dataset has a description
    if description:
        score += 5

    return score