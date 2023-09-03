import json
from datetime import datetime
from pythorhead import Lemmy

community = "gunners@lemmy.world"


def getTimestamp():
    dt = str(datetime.now().month) + '/' + str(datetime.now().day) + ' '
    hr = str(datetime.now().hour) if len(str(datetime.now().hour)) > 1 else '0' + str(datetime.now().hour)
    minute = str(datetime.now().minute) if len(str(datetime.now().minute)) > 1 else '0' + str(datetime.now().minute)
    t = '[' + hr + ':' + minute + '] '
    return dt + t


def createBody():
    body = "Use this thread for general daily football discussion.\n\n"
    body += "This thread can also be used to discuss Transfer rumours and to post Tier 4 sources.\n\n"
    return body


def createTitle():
    date = datetime.today().strftime('%d %B %Y')
    title = f'Daily Discussion - {date}'
    return title


def login():
    with open("../config.json") as file:
        config = json.load(file)
    file.close()
    lemmy = Lemmy(f'https://{config["instance"]}')
    lemmy.log_in(config["username"], config["password"])
    print(f'{getTimestamp()} Logged in as {config["username"]}')
    return lemmy


def main():
    title = createTitle()
    body = createBody()
    lemmy = login()
    community_id = lemmy.discover_community("eabryt@lemmy.world")
    response = lemmy.post.create(community_id, name=title, body=body)
    print(f"{getTimestamp()} Post at {response['post_view']['post']['id']}")


if __name__ == '__main__':
    main()
