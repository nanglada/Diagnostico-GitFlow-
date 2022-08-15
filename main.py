import users
import retweets

def main(file):
    retweets.most_retweets(file)
    users.best_users(file)

main("farmers-protest-tweets-2021-03-5.json")