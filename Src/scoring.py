import pandas as pd

def score_wallets(df):
    grouped = df.groupby("user")

    scores = []
    for user, group in grouped:
        score = 1000
        deposit_count = (group["type"] == "deposit").sum()
        borrow_count = (group["type"] == "borrow").sum()
        repay_count = (group["type"] == "repay").sum()
        liquidation_count = (group["type"] == "liquidationcall").sum()

        score += deposit_count * 5
        score -= liquidation_count * 100
        score -= max(0, borrow_count - repay_count) * 10

        score = max(min(score, 1000), 0)

        scores.append({"user": user, "score": score})

    return pd.DataFrame(scores)
