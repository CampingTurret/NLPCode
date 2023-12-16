import typing


def Not_filter(PrevGen: typing.Generator, EndOfLine = "<>", Sarcasm = '</s>'):

    for line in PrevGen:
        line: str = line
        if not (('not' in line) or ( Sarcasm in line)):
            yield line
        else:
            StartPositive = True
            if ( Sarcasm in line):
                 StartPositive = False
            Positive = StartPositive
            LineList = line.split(' ')
            for i, w in LineList.copy():
                if (w == 'not'):
                    Positive = not Positive
                    continue
                if (w == EndOfLine):
                    Positive = StartPositive
                    continue
                if (Positive is False):
                    LineList[i] = 'NOT_' + w
                if ( Sarcasm == w):
                    LineList[i] = ''
               

            NewLine = " ".join(LineList)
            yield NewLine
    
    