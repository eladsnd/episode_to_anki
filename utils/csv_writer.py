import pandas as pd
import config

def save_to_csv(data, columns):
    """Saves sentence data to a CSV file formatted for Anki."""
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(config.OUTPUT_CSV, index=False, encoding="utf-8-sig")
    print(f"✅ Anki CSV saved as: {config.OUTPUT_CSV}")
