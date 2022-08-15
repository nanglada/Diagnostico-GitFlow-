import json
from collections import Counter

def best_users(file):
    users = []
    tweets = [json.loads(line) for line in open(file, 'r')]
    for i in tweets:
        users.append(i["user"]["username"])
    best_users = Counter(users)
    print(f"Los top 10 usuarios son:")
    best = best_users.most_common(10)
    for i in range(0, len(best)):
        print(f"Número {i + 1}: {best[i][0]} con {best[i][1]} tweets")
