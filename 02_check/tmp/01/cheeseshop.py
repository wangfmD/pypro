# codeing:utf-8


def cheeseshop(kind, *arguments, **keywords):
    print "--Do you have any ,", kind, "?"
    print "-- I am sorroy we are out of ", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = keywords.keys()
    keys.sort()
    print keys
    for kl in keys:
        print kl, ":", keywords[kl]

cheeseshop("wfm", "11111111",
           "222222222",
           "222222222",
           "222222222",
           a='1',
           f='2',
           c='3',
           b='2',
           e='3')
