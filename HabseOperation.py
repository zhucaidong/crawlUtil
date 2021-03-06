from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import *

class HabseHelp():
    def __init__(self):
        self.transport = TSocket.TSocket('192.168.0.242', 9090);
        transport = TTransport.TBufferedTransport(self.transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport);
        self.client = Hbase.Client(protocol)
        transport.open()
    def createTable(self):
        contents = ColumnDescriptor(name='cf:', maxVersions=1)
        self.client.createTable('test_b', [contents])
        print self.client.getTableNames()
    def insert(self,dic_list,row):
        mutations=[]
        for i in range(len(dic_list)):
            for (k,v) in dic_list[i].items():
                print k+':'+v
                mu=Mutation(column='cf:'+k,value=v)
                mutations.append(mu)
        #print mutations
        #mutations = [Mutation(column='cf:c', value='value')]
        self.client.mutateRow('test_b', row, mutations)
    def update(self):
        pass
    def query_one(self):
        tableName = 'test'
        rowKey = 'row-key1'
        result = self.client.getRow(tableName, rowKey, None)
        print result
        for r in result:
            print 'the row is ', r.row
            print 'the values is ', r.columns.get('cf:a').value
    def query_many(self):
        scan = TScan()
        tableName = 'test_b'
        id = self.client.scannerOpenWithScan(tableName, scan, None)
        result2 = self.client.scannerGetList(id, 10)

        print result2
if __name__ == '__main__':
    hb=HabseHelp()
    hb.__init__()
    #hb.createTable()
    hb.insert([{'asdw':'sdw2'},{'dsad':'www'},{'555':'666'}],'thasdsa')
    #hb.query_many()
    pass