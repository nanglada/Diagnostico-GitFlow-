import json

def most_retweets(file):
    retweeted = [[0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], 
                [0, ""], [0, ""], [0, ""], [0, ""]]
    tweets = [json.loads(line) for line in open(file, 'r')]
    for i in tweets:
        for j in range(0, len(retweeted)):
            if i["retweetCount"] > retweeted[j][0]:
                retweeted[j][0] = i["retweetCount"]
                retweeted[j][1] = i["content"]
                break
    print(f"Los 10 tweets más retweeteados son:")
    for i in range(0, len(retweeted)):
        print(f"Número {i}: {retweeted[i][1]}\n")

