from debug import Debug
d=Debug()

print(d.format(d.Formatter.ERROR, 'hello',  True))
X = 1
d.Formatted().variable('hi', X)
print(d.format(d.Formatter.PROGRAM, 'hello'))
print(d.format(d.Formatter.LOG, 'hi'))
d.function('not_existant',{})