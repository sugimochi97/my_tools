import pandas as pd
import time
import random

def wget_english_words():
    df_list = []
    for i in range(1,21):
        df = pd.read_html(f"https://l-formula.com/words{i}")[0]
        df_list.append(df)
        time.sleep(1)

    df_all = pd.concat(df_list)
    df_all = df_all.reset_index(drop=True).drop(0, axis=1)
    df_all = df_all.set_axis(df_all.iloc[0, :], axis=1).drop(0)

    df_all.to_csv("./English_words.csv", index=False)
    return df_all

def gacha_english_word(show=True):
    df_all = pd.read_csv("./English_words.csv")
    word = df_all.iloc[random.choice(df_all.index)]

    print("英単語：", word["英単語"])
    print("意味：", word["意味"])

    return word

if __name__ == "__main__":
    # wget_english_words()
    gacha_english_word()