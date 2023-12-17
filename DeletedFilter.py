import typing

def filter_data(PrevGen: typing.Generator) -> typing.Generator:
    for line in PrevGen:
        if line.lower() not in {'[removed]', '[deleted]', ''}:
            yield line
    

