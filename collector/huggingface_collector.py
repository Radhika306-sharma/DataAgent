from huggingface_hub import list_datasets

SEARCH_TERMS = [
    "fake news",
    "misinformation",
    "fact check",
    "fact checking",
    "claim verification",
    "news verification",
    "rumor detection",
    "rumour detection",
    "fake news detection",
    "hindi fake news",
    "english fake news",
    "hinglish",
    "code mixed",
    "code-mixed",
    "indian fake news",
    "india fake news",
    "AI4Bharat",
    "IFND",
    "news classification"
]


def search_huggingface():
    print("\nSearching Hugging Face...\n")

    seen = set()

    for query in SEARCH_TERMS:

        print(f"\n========== {query.upper()} ==========\n")

        try:
            datasets = list_datasets(search=query)

            for dataset in datasets:
                if dataset.id not in seen:
                    seen.add(dataset.id)
                    yield dataset

        except Exception as e:
            print(f"Error while searching '{query}': {e}")


if __name__ == "__main__":

    count = 0

    for dataset in search_huggingface():
        print(dataset.id)
        count += 1

    print(f"\nTotal unique datasets found: {count}")