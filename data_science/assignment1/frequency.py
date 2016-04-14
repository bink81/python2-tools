import sys
import json

# Problem 4: Compute Term Frequency

# Write a Python script frequency.py to compute the term frequency histogram of the livestream data you harvested from Problem 1.
# The frequency of a term can be calculated as [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]
# Your script will be run from the command line like this:

# $ python frequency.py <tweet_file>
def main():
    tweet_file = open(sys.argv[1])
    #lines(tweet_file)
    terms = {}
    count = 0
    for line in tweet_file:
        tweet = {}
        tweet  =  json.loads(line)
        if 'text' in tweet.keys():
            text = tweet['text'].encode('utf-8')
            #print 'text: ', text
            words = text.split()
            #print 'words: ', len(words)
            # now we know tweet's score!
            for word in words:
                if word in terms.keys():
                    terms[word] = terms[word] + 1
                else:
                    terms[word] = 0
                    count =count + 1
                    
    for term in terms.keys():                
        print term, (terms[term] * 1.0) / (count * 1.0)

if __name__ == '__main__':
    main()
    #print '---------------------------------------------------------------'
