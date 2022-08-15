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
    for i in retweeted:
        print(i[1])
most_retweets("farmers-protest-tweets-2021-03-5.json")