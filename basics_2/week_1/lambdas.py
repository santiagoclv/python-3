wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]

# pasa los verbos a pasado

pastensear = lambda w : w + "ed"
past_wrds = []
for word in wrds:
  past_wrds.append(pastensear(word))


inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]


parse_item = lambda item : item.split(", ")
get_item = lambda items, idx : items[idx]

for item in inventory:
    print('The store has {} {}, each for {} USD.'.format(get_item(parse_item(item), 1), get_item(parse_item(item), 0), get_item(parse_item(item), 2)))


scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

parse_array_scores = lambda scores : scores.split(" ")
parse_int_array = lambda scores : map(int, scores)
a_scores = 0
for score in parse_int_array(parse_array_scores(scores)):
    if(score >= 90):
        a_scores += 1




stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

org_lower = org.lower()

org_words = org_lower.split()
acro = ""
for stop_word in stopwords:
    for stop_word_time in range(org_lower.count(stop_word)):
        try:
            org_words.remove(stop_word)
        except:
            pass

for word in org_words:
    word = word.upper()
    acro += word[0]