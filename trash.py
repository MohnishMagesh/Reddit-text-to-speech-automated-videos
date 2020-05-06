import re

lister = []

comment = "this is a really long paragraph, so direction is still recommended. We shall see?"
punctuation_reg = re.compile('(?<=[.!,?:;-]) +')
split_parts = punctuation_reg.split(comment)
parts = list(filter(None, split_parts))
lister = parts
print(lister)
