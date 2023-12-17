import typing
import time

def safe_filtered_corpus(gen: typing.Generator) -> None:
    f = open('SaveFilteredCorpus.txt', 'w', encoding='utf-8')
    for s in gen:
        f.write(s + '\n')
    f.close()

def load_filtered_corpus() -> typing.Generator:
    f = open('SaveFilteredCorpus.txt', 'r')
    for l in f:
        yield l.strip()
    f.close()
    

def load_data() -> typing.Generator:
    import json
    f = open('cars_comments.ndjson', 'rb')
    for l in f:
        line = json.loads(l)
        yield line['body']
    f = open('cars_submissions.ndjson', 'rb')
    for l in f:
        line = json.loads(l)
        yield line['selftext']
    

def lower(gen: typing.Generator) -> typing.Generator:
    for i in gen:
        yield i.lower()
    
