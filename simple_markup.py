import sys,re
from util import *

'''
Target) 打印一些起始标记
2）对于每个文本块，在段落标签内打印它
3）打印一些结束标记
'''

print('<html><head><title>...</title><body>')

title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)  # 正则表达式加上 ？ 后为非贪婪模式
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')

print('</body></html>')
