import json
from collections import Counter

def most_hashtags(file):
    hashtags = []
    tweets = [json.loads(line) for line in open(file, 'r')]
    for i in tweets:
        if "#" in i["content"]:
            hashtags.append(i["content"])
    best_hashtags = Counter(hashtags)
    print(f"Los top 10 usuarios son:")
    best = best_hashtags.most_common(10)
    for i in range(0, len(best)):
        print(f"Número {i + 1}: {best[i][0]} con {best[i][1]} tweets")

most_hashtags("farmers-protest-tweets-2021-03-5.json")