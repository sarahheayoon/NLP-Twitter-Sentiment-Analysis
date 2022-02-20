from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRequestError, TwitterConnectionError, TwitterPager
import pandas as pd

""" GETTING TWITTER AUTHENTICATION """

# Oauth keys
consumer_key = '37osUadblZABTOkc2mqlhERZu'
consumer_secret = 'k2HdTUg5GERupy8iUyOdrd8Z2J67S4qUeNaZhbgvCSd0p3JmY6'
access_token = '1453471187653201923-i7wAcAEJSI1youyTHsObUPNuDZENXH'
access_token_secret = 'Da6L4g5a4IlqEQRpMlLla2ZgvgZLDXd19SaCLULWzauCR'


api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret, api_version='2')

""" CREATING THE CODE NEEDED TO GET REPLIES FOR TWEETS """


def add_data(tweets):
    """
    Takes a data frame with tweet_ids and retrieves conversation_id for each tweet

    :param tweets: data frame
    :return: adds conversation_id variable for every observation
    """
    print("Retrieving additional data")
    ids = tweets.tweet_id
    conv_ids = []

    for id in ids:

        TWEET_ID = id
        TWEET_FIELDS = 'conversation_id'

        try:
            r = api.request(f'tweets/:{TWEET_ID}', {'tweet.fields': TWEET_FIELDS})
            for item in r:
                conv_ids.append(item['conversation_id'])

        except TwitterRequestError as e:
            print(e.status_code)
            for msg in iter(e):
                print(msg)

        except TwitterConnectionError as e:
            print(e)

        except Exception as e:
            print(e)

    tweets['conversation_id'] = conv_ids
    return tweets


class TreeNode:
    """ Helps us retrieve replies from a twitter post """

    def __init__(self, data):
        """data is a tweet's json object"""
        self.data = data
        self.children = []

    def id(self):
        """a node is identified by its author"""
        return self.data['author_id']

    def reply_to(self):
        """the reply-to user is the parent of the node"""
        return self.data['in_reply_to_user_id']

    def find_parent_of(self, node):
        """append a node to the children of it's reply-to user"""
        if node.reply_to() == self.id():
            self.children.append(node)
            return True
        for child in self.children:
            if child.find_parent_of(node):
                return True
        return False

    def print_tree(self, level):
        """level 0 is the root node, then incremented for subsequent generations"""
        # print(f'{level*"_"}{level}: {self.id()}')
        level += 1
        for child in self.children:
            child.print_tree(level)

    def list_l1(self):
        conv_id = []
        child_id = []
        text = []
        # print(self.data['id'])
        for child in self.children:
            conv_id.append(self.data['id'])
            child_id.append(child.data['id'])
            text.append(child.data['text'])
        return conv_id, child_id, text


def retrieve_replies(conversation_id):
    """
    Retrieves level 1 replies for a given conversation id
    Returns lists conv_id, child_id, text tuple which shows every reply's tweet_id and text in the last two lists
    """

    try:
        # GET ROOT OF THE CONVERSATION
        r = api.request(f'tweets/:{conversation_id}',
                        {
                            'tweet.fields': 'author_id,conversation_id,created_at,in_reply_to_user_id'
                        })

        for item in r:
            root = TreeNode(item)
            # print(f'ROOT {root.id()}')

        # GET ALL REPLIES IN CONVERSATION

        pager = TwitterPager(api, 'tweets/search/recent',
                             {
                                 'query': f'conversation_id:{conversation_id}',
                                 'tweet.fields': 'author_id,conversation_id,created_at,in_reply_to_user_id'
                             })

        orphans = []

        for item in pager.get_iterator(wait=2):
            node = TreeNode(item)
            # print(f'{node.id()} => {node.reply_to()}')
            # COLLECT ANY ORPHANS THAT ARE NODE'S CHILD
            orphans = [orphan for orphan in orphans if not node.find_parent_of(orphan)]
            # IF NODE CANNOT BE PLACED IN TREE, ORPHAN IT UNTIL ITS PARENT IS FOUND
            if not root.find_parent_of(node):
                orphans.append(node)

        conv_id, child_id, text = root.list_l1()

        assert len(orphans) == 0, f'{len(orphans)} orphaned tweets'

    except TwitterRequestError as e:
        print(e.status_code)
        for msg in iter(e):
            print(msg)

    except TwitterConnectionError as e:
        print(e)

    except Exception as e:
        print(e)

    return conv_id, child_id, text


def reply_thread_maker(conv_ids):
    """
    Retrieves replies for a list of conversation ids [conv_ids]
    Returns a data frame with columns [conv_id, child_id, text] tuple which shows every reply's tweet_id and text
    """
    conv_id = []
    child_id = []
    text = []
    for id in conv_ids:
        conv_id1, child_id1, text1 = retrieve_replies(id)
        conv_id.extend(conv_id1)
        child_id.extend(child_id1)
        text.extend(text1)

    replies_data = {'conversation_id' : conv_id,
               'child_tweet_id': child_id,
               'tweet_text' : text}

    replies = pd.DataFrame(replies_data)
    return replies


def final_function(df1_path, df2):
    """
    Takes in a data frame with tweet ID's and returna a dataframe with replies to all tweets
    :param df1_path: e.g. "/Users/carlosvalerapaulino/Desktop/CompStats/GroupB-TextPower/tim_cook_tweets.csv"
    :param df2: e.g. "./tweets.csv"
    :return: data frame with all replies
    """
    df = pd.read_csv(df1_path)
    tweets = add_data(df)
    tweets.to_csv(df2)
    convo_df = pd.read_csv(df2)
    list_of_convo_ids = convo_df['conversation_id'].to_list()
    replies = reply_thread_maker(list_of_convo_ids)
    replies.to_csv("replies.csv")


""" Getting the replies """

# final_function("/Users/carlosvalerapaulino/Desktop/CompStats/GroupB-TextPower/tim_cook_tweets.csv", "./tweets.csv")


# https://towardsdatascience.com/mining-replies-to-tweets-a-walkthrough-9a936602c4d6 --> source of data

df = pd.read_csv("/Users/carlosvalerapaulino/Desktop/CompStats/GroupB-TextPower/tim_cook_tweets.csv")

tweet1 = ['1465050134274785282']
tweet2 = ['1463909273482641411']
tweet3 = ['1463236596505841665']


t3 = reply_thread_maker(tweet3)

t3.to_csv("t3.csv")
