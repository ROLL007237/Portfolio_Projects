import pickle
import time as t
f = open('data.pickle', 'rb')
data = pickle.load(f)

class Message:
    def __init__(self,time,author,text,score,subreddit,archived):
        self.time = time
        self.author = author
        self.text = text
        self.score = score
        self.subreddit = subreddit
        self.archived = archived

    def __repr__(self):
        return f"Subreddit: \"{self.subreddit}\"\n{t.ctime(int(self.time))}\nMessage from '{self.author}' [{self.score}]:\n\"{self.text}\""

def  data2obj(data):
    messages = []
    subreddits = []
    for msg in data:
        author = msg['author']
        text = msg['body']
        score = msg['score']
        subreddit = msg['subreddit']
        archived = msg['archived']
        time = (msg['created_utc'])
        mem = Message(time,author,text,score,subreddit,archived)
        if (text and author) != '[deleted]':
            messages.append(mem)
            subreddits.append(mem.subreddit)

    return messages,list(set(subreddits))

messages = data2obj(data)[0]
subreddits = data2obj(data)[1]


def at_least_one_digit(msg):
    k=0
    texts = [i.text for i in msg]
    for i in texts:
        for j in i:
            if j.isdecimal():
                k+=1
                break
    return k

def top_lowest_score(messages, top_size=15):
    scores = [i.score for i in messages]
    scored_messages = dict()
    for i in range (len(scores)):
        scored_messages[messages[i].text] = scores[i]
    scored_messages = sorted(scored_messages.items(), key=lambda item: item[1])[:top_size]
    return scored_messages


def sub_category(messages):
    objects_of_subreddit = dict()
    for i in subreddits:
        k=0
        for j in messages:
            if j.subreddit == i:
                k+=1
        objects_of_subreddit[i] = k
    return sorted(objects_of_subreddit.items(), key=lambda item: item[1],reverse=True)

def mean_msg_size(messages):
    length = []
    for i in messages:
        length.append(len(i.text.replace('\n','')))
    return length
