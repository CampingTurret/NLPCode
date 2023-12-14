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