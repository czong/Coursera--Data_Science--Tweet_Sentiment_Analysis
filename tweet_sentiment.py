import sys
import pdb
import json

def lines(fp):
    print str(len(fp.readlines()))

def get_score(tweet_text,score_map):
    score = 0
    for key in score_map.keys():
	#pdb.set_trace()
	if key in tweet_text:
	    score+=score_map[key]
    
    return score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)
    scores_map = {}
    scores_tweet = []
    ### extract the score of each word from sentiment file
    for line in sent_file:
	term,score = line.split('\t')
	scores_map[term]=int(score)
    
    for line in tweet_file:
	#pdb.set_trace()
	temp = json.loads(line)
	if 'text' in temp:
    	    text = temp['text']
	    #pdb.set_trace()
	    text_sep = text.split(' ')
	    score_temp  = get_score(text_sep,scores_map)
	    scores_tweet.append(str(score_temp))
	else:
	    scores_tweet.append(str(0))
    pdb.set_trace() 
    file_write = open('tweet_scores.txt','w')
    file_write.write('\n'.join(str(item) for item in scores_tweet))
    file_write.close()


	
if __name__ == '__main__':
    main()
