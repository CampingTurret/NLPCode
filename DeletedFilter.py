import typing

def filter_data(PrevGen: typing.Generator) -> typing.Generator:
    for line in PrevGen:
        if line['selftext'].lower() not in {'[removed]', '[deleted]', ''}:
            yield line
    

