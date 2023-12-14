import typing


def fix_contractions(gen: typing.Generator) -> typing.Generator:
    import contractions
    for i in gen:
        yield contractions.fix(i)
    raise StopIteration()