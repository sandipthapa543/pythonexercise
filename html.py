def html_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)


print(html_tags('i', 'Python'))
print(html_tags('b', 'Python Tutorial'))