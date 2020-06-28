def poors(notting):
    if notting.find('not') and notting.find('poor'):
        return notting.replace('not that poor', 'good')
    else:
        return notting.replace('good', ' poor')


print(poors('The lyrics is not that poor!'))
print(poors ('The lyrics is poor!'))