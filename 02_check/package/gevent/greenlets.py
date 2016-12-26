import gevent

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('swich to foo again')

def bar():
    print('Running in bar')
    gevent.sleep(0)
    print('swich to bar again')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar)])
