from twisted.internet.protocol import Protocol, Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class Echo(Protocol):

    def dataReceived(self, data):
        self.transport.write(data)
        self.transport.write(self.factory.msg)


class MyFactory(Factory):
    protocol = Echo

    def __init__(self):
        self.msg = 'hello twisted'


class LineEcho(LineReceiver):

    def lineReceived(self, line):
        self.sendLine('Line: %s' % line)

    def connectionMade(self):
        self.sendLine('Welcome here!')

    def connectionLost(self, reason):
        print 'connection Lost'
        print reason
        self.sendLine('connection LOST')

class AnotherFactory(Factory):
    protocol = LineEcho

    def __init__(self):
        pass

    def startFactory(self):
        print 'start AnotherFactory'

    def stopFactory(self):
        print 'stop AnotherFactory'

reactor.listenTCP(8888, MyFactory())
reactor.listenTCP(9999, AnotherFactory())
reactor.run()
