import MeCab

tagger = MeCab.Tagger()
tagger.parse('') #this is the hack to avoif the bug of .parseToNode()

#. parseTONode() catcheds the node object which expresses the first form
node = tagger.parseToNode('すもももももももものうち')

while node:
    #. surface is the string array of the form elements,  .featrue expresses the string array which contains some part of speech
    print(node.surface, node.feature)
    node = node.next # get the next node by .next
