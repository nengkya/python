from time  import ctime

class MetaC(type):
   def __init__(cls, name, bases, attrd):
       super(MetaC, cls).__init__(name, bases, attrd)
       print 'Created class %r at: %s' % (name, ctime())

class Foo(object):
   __metaclass__ = MetaC
   def __init__(self):
       print 'Instantiated class %r at: %s' % (self.__class__.__name__, ctime())

f = Foo()
