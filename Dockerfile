FROM python:3.7-alpine

COPY bot_tweets/config.py /bot_tweet/
COPY bot_tweets/favretweet.py /bot_tweet/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot_tweet
CMD ["python3", "favretweet.py"]
