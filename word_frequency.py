import sys
import logging
from collections import Counter
from pathlib import Path
from  typing import List, Iterator, TextIO # TextIO is the from that expresses a file object which can get str

import MeCab

tagger = MeCab.Tagger('')
tagger.parse('') # to avoif the bug

def main():
    """
        show the frequent words by reading the file in the directry specified by the command line valuable
    """
    #specify the directry WikiExtractor outputs with the first commnadline valuable
    #Path object is the pbject that makes it abstract to control a file or path to the directry

    input_dir = Path(sys.argv[1])

    #create tje counter object which sotres how many times the word appears
    #Counter class has dict passed down and the number of appearance as the valu
    frequency = Counter()

    #by .glob(), get the list of the file which matcches the wild cards and process all the matched files
    for path in sorted(input_dir.glob('*/wiki_*')):
        logging.info(f'Processing {path}...')

        with open(path) as file: #opem the file
        #count how many times the word appears in the file, and marge the number of appearance
            frequency += count_words(file)


    #if the process was was done, it shows tje 30th toppest nouns and how muc they appeared
    for word, count in frequency.most_common(30):
        print(word, count)


def count_words(file: TextIO) -> Counter:
    """
    The function whcih counts how many the word appeared in all the matched file that the wikiExtracor outputted
    """

    frequency = Counter() #The object that counts the number of the appearance in the file

    num_docs = 0 # this is the valuable to count the number of processed articles im order to outputs

    for content in iter_doc_contents(file): # iterate the process fpr all the article in the files
        words = get_words(content) #get the list of nouns contained in the article
        #If tje iteratable object is specified in the update() method of the counter
        #it can increae the value of the number of appearance in th List
        frequency.update(words)
        num_docs += 1

    logging.info(f'Found {len(frequency)}) words from {num_docs} documents.')
    return frequency

def iter_doc_contents(file: TextIO) ->Iterator[str]:
    """
    The generatring function which reads the file object and returns the contents of the article ( from <doc> to </doc>) in order
    """

    for line in file: # iterate processing about the rows contained in the file
        if line.startswith('<doc '):
            buffer = [] #initialize tje buffer once the start tag is detected
        elif line.startswith('</doc>'):
            #If the end tag was detected, it unifies tje content of the buffer and yields it
            content = ''.join(buffer)
            yield content
        else:
             buffer.append(line) # Except the start tag and the end tag, all the contents are included

def get_words(content: str) -> List[str]:
    """
    the function that get the list of nouns appeared in the string array
    """

    words = [] #the list which stores nouns appeared

    node = tagger.parseToNode(content)
    while node:
        # since the node.feature is spliited by commma, the divide into two by split()
        #and plug the second one in to pos and pos_sub1. pos  stands for Part of speech
        pos, pos_sub1 = node.feature.split(',')[:2]
        #add to words if and only if a proper noun or general nouns
        if pos == '名詞' and pos_sub1 in ('固有名詞', '一般'):
            words.append(node.surface)

        node = node.next

    return words

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO) #Output the log more than the INFO level
    main()
