def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'rahul'))
print(add_tags('b', 'rana'))
