

class VietToken:
  def __init__(self, text, pos, index):
    self.text = text
    self.pos = pos
    self.index = index

class VietNLP:
    def __init__(self, text):
        self.tokens = self.handle(text)
        
    def handle(self, text):
        from pyvi import ViPosTagger, ViTokenizer
        doc = ViPosTagger.postagging(ViTokenizer.tokenize(text))

        tokens = []
        for text, pos, i in zip(doc[0], doc[1], range(0, len(doc[0]))):
            token = VietToken(text, pos, i)
            tokens.append(token)
        #self.tokens = tokens
        return tokens
 
#...........................

text1 = u"Tổ hợp xét tuyển của ngành Sư phạm Toán học là gì?."
text2 = u"Tổ hợp xét tuyển của ngành Toán học là gì?."

doc1 = VietNLP(text1).tokens
for token in doc1:
    print(token.text, token.pos, token.index)

doc2 = VietNLP(text2).tokens
for token in doc2:
    print(token.text, token.pos, token.index)


