from collector.huggingface_collector import search_huggingface
#from collector.kaggle_collector import search_kaggle
#from collector.github_collector import search_github
#from collector.ai4bharat_collector import search_ai4bharat
#from collector.paperswithcode_collector import search_paperswithcode
#from collector.zenodo_collector import search_zenodo

from analyzer.metadata_extractor import extract_metadata
from analyzer.dataset_scorer import score_dataset
from analyzer.priority_engine import assign_priority
from processor.deduplicator import remove_duplicates

datasets = []

datasets += search_huggingface()
#datasets += search_kaggle()
#datasets += search_github()
#datasets += search_ai4bharat()
#datasets += search_paperswithcode()
#datasets += search_zenodo()
datasets = remove_duplicates(datasets)

for item in datasets:
    info = extract_metadata(item)
    score = score_dataset(info)
    decision = assign_priority(score)
    #print_report(info, score, decision)