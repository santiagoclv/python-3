
# Net Score vs Number of Retweets.

# Number of Retweets, 
# Number of Replies, 
# Positive Score, 
# Negative Score, 
# Net Score

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def reduce(function, sequence, initial=None):
    it = iter(sequence)
    value = initial
    for element in it:
        value = function(value, element)
    return value

def strip_punctuation(word = ''):
    return reduce((lambda word_acc, char: word_acc.replace(char, '')), punctuation_chars, word)

def get_pos(sentense):
    positive_counter = 0
    words = strip_punctuation(sentense).split()
    for word in words:
        if word.lower() in positive_words:
            positive_counter += 1
    return positive_counter

def get_neg(sentense):
    negative_counter = 0
    words = strip_punctuation(sentense).split()
    for word in words:
        if word.lower() in negative_words:
            negative_counter += 1
    return negative_counter


with open("resulting_data.csv", "w") as outfile:
    outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
    with open("project_twitter_data.csv") as pos_f:
        lines = pos_f.readlines()
        for lin in lines[1:]:
            row = lin.replace('\n', '').split(',')
            positive = get_pos(row[0])
            negative = get_neg(row[0])
            retweets = row[1]
            replies = row[2]
            net_score = positive - negative
            row_string = '{},{},{},{},{}\n'.format(retweets, replies, positive, negative, net_score)
            outfile.write(row_string)