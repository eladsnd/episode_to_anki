import pandas as pd
import os


def save_to_csv(data, output_csv, columns):
    """Saves sentence data to a CSV file formatted for Anki."""
    df = pd.DataFrame(data, columns=columns)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    df.to_csv(output_csv, index=False, encoding="utf-8-sig")
    print(f"✅ Anki CSV saved as: {output_csv}")
