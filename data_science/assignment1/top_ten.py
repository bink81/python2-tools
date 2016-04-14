import sys
import json
import operator

# Problem 6: Top ten hash tags

# Write a Python script top_ten.py that computes the ten most frequently occurring hashtags from the data you gathered in Problem 1.

# Your script will be run from the command line like this:
# $ python top_ten.py <tweet_file>

def main():
    tweet_file = open(sys.argv[1])
    tag_count = {}
    for line in tweet_file:
        #print line
        tweet  =  json.loads(line)
        if 'entities' in tweet.keys():
            entities = tweet['entities']
            tags = entities['hashtags']
            for tag in tags:
                text = tag['text']
                #print text
                if text in tag_count.keys():
                    tag_count[text] = tag_count[text] + 1
                else:
                    tag_count[text] = 1
    hashtags = sorted(tag_count.items(), key=operator.itemgetter(1), reverse=True)
    #print hashtags 
    for hashtag in hashtags[:10]:
        print hashtag[0].encode('utf-8')  + " " + str(hashtag[1])
                    
if __name__ == '__main__':
    main()
