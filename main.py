from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load

def run_pipeline():
    extract()
    transform()
    load()

if __name__ == "__main__":
    run_pipeline()
