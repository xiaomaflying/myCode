from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import ClientCreator

class Greeter(Protocol):
    def sendMessage(self, msg):
        self.transport.write('MESSAGE %s\n' % msg)

def gotProtocol(p):
    p.sendMessage('Hello')
    reactor.callLater(1, p.sendMessage, 'This is sent in a second')
    reactor.callLater(2, p.transport.loseConnection)


#point = TCP4ClientEndpoint(reactor, 'localhost', 8888)
#d = connectProtocol(point, Greeter())
#d.addCallback(gotProtocol)
#reactor.run()

#creator = ClientCreator(reactor, Greeter)
#d = creator.connectTCP('127.0.0.1', 8888)
#d.addCallback(gotProtocol)
#reactor.run()
class Echo(Protocol):
    def dataReceived(self, data):
        print data

class EchoClientFactory(ClientFactory):
    protocol = Echo
    def conncetionMade(self):
        print 'connect client'

reactor.connectTCP('localhost', 8888, EchoClientFactory())
reactor.run()
