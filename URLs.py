#! python3
# extracting URLs (http/https) from clipboard
import re
import pyperclip as pc

RE = re.compile(r'(https?:\/\/(www\.)?[-a-zA-Z0-9%._@:\+=#~]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*))')

matches = []
text = pc.paste()
text = '''fhdskfhdsdk http://www.reddit/ ghr3eitgh3im gre438th https://ihateregex.io/expr/url/ rjelgjel https://wiki.python.org/moin/BitwiseOperators 
            sdsdshttps://www.youtube.com/watch?v=cRzQuPvLjdU
            https://adventofcode.com/2015/day/3'''
for groups in RE.findall(text):
    matches.append(groups[0])

print('Found:')
print('\n'.join(matches))
text = '\n'.join(matches)
pc.copy(text)

