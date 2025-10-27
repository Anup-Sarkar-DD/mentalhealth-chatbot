from datasets import load_dataset
import pandas as pd
import os

def download_and_save_mentalchat16k():
    dataset = load_dataset("ShenLab/MentalChat16K")

    print("Available splits:", dataset)

    os.makedirs('data', exist_ok=True)

    # Save train split
    train_data = dataset['train']
    df_train = pd.DataFrame(train_data)
    df_train.to_csv('data/mentalchat16k_train.csv', index=False)
    print("Train split saved as data/mentalchat16k_train.csv")

    # Save validation split if exists
    if 'validation' in dataset:
        df_val = pd.DataFrame(dataset['validation'])
        df_val.to_csv('data/mentalchat16k_validation.csv', index=False)
        print("Validation split saved as data/mentalchat16k_validation.csv")

    # Save test split if exists
    if 'test' in dataset:
        df_test = pd.DataFrame(dataset['test'])
        df_test.to_csv('data/mentalchat16k_test.csv', index=False)
        print("Test split saved as data/mentalchat16k_test.csv")

if __name__ == "__main__":
    download_and_save_mentalchat16k()
