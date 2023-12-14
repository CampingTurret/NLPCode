import typing

def safe_filtered_corpus(gen: typing.Generator) -> None:
    f = open('SaveFilteredCorpus.txt', 'w')
    for s in gen:
        f.write(s + '\n')
    f.close()

def load_filtered_corpus() -> typing.Generator:
    f = open('SaveFilteredCorpus.txt', 'r')
    for l in f:
        yield l.strip()
    f.close()
    raise StopIteration()

def load_data() -> typing.Generator:
    import json
    f = open('cars_comments.ndjson', 'rb')
    for l in f:
        line = json.loads(l)
        yield line
    f = open('cars_submissions.ndjson', 'rb')
    for l in f:
        line = json.loads(l)
        yield line

for i, l in enumerate(load_data()):
    if i == 800000:
        print(l)
    