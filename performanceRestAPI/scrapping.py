import tweepy
from dotenv import load_dotenv
import os

load_dotenv()
print("Bearer_Token")
def getDatas(musician):
    bearer_token = os.environ.get("Bearer_Token")

    client = tweepy.Client(bearer_token=bearer_token)
    user = client.get_user(username='YES24TicketOpen')

    paginator = tweepy.Paginator(client.get_users_tweets, id=user.data.id, max_results=100, start_time='2023-01-01T17:00:00Z')

    datas = []
    test = []
    num = 0
    for tweet in paginator.flatten(limit=3200):
        test.append(tweet)
        arr = tweet.data['text'].split('\n')
        print(tweet)
        print(num)
        num = num + 1

        if ('RT @' not in tweet.text):
            arr = list(filter(None, arr))

            title = arr[2].strip()

            if musician in title.casefold():
                date_full = arr[2].strip()[-19:].replace('-', '.')
                date = date_full[0:10]
                link = arr[3].replace('▶️', '').strip()

                obj = {'artist': musician, 'title': title, 'date_full': date_full, 'date':date, 'link': link, 'performance_info':f"{title}-{date_full}"}
                datas.append(obj)

    print('끝')
    print(len(test))
    print(len(datas))
    for data in datas:
        print(data)
        print('================================================')

    return datas

# musician = '코난 그레이'
# getDatas(musician)