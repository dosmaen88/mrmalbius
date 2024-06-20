import json
from json import JSONEncoder
class Quotes:
    def __init__(self, author: str, quote: str):
        self.author = author
        self.quote = quote
class QuotesEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
def initializeJSON():
    quotedata = [Quotes("test", "test"), Quotes("test2", "test2")]
    with open('data.json', 'w', encoding='utf-8') as x:
        json.dump(quotedata, x, ensure_ascii=False, indent =4, cls=QuotesEncoder)