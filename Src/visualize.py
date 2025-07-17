import matplotlib.pyplot as plt
import os

def plot_score_distribution(df):
    plt.figure(figsize=(10,6))
    plt.hist(df['score'], bins=10, range=(0, 1000), edgecolor='black')
    plt.title("Wallet Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Number of Wallets")
    os.makedirs("output", exist_ok=True)
    plt.savefig("output/score_distribution.png")
