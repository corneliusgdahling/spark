from pyspark import SparkContext, SparkConf


def get_tweets(task, sample=True):
    conf = SparkConf().setAppName(task)
    sc = SparkContext(conf=conf)
    tweets = sc.textFile('../data/geotweets.tsv')
    tweets_split = tweets.map(lambda x: x.split('\t'))
    return tweets_split.sample(False, 0.1, 5) if sample else tweets_split


def get_stopwords():
    words = []
    f = open('../data/stopwords.txt', 'r')
    for word in f:
        words.append(word.strip("\n"))
    f.close()
    return words


def result_file(task):
    return '../results/task'+ task + '.tsv'


def write_results(result_file, results):
    for r in results:
        result_file.write(r+"\n")