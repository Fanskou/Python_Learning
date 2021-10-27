'''
首先需要将文本分块
简单做法： 收集空行前的所有行并将它们返回，然后重复这样的操作
'''

def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

