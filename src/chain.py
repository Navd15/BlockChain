import hashlib as hasher,datetime as date


class Block:
    def __init__(self,index,timestamp,data,previousHash):
        self.index=index
        self.timestamp=timestamp
        self.data=data
        self.previousHash = previousHash
        self.hash=self.hashBlock()


    def hashBlock(self):
            sha=hasher.sha256()
            sha.update(str(self.index,'utf-8')+
                       str(self.timestamp,'utf-8')+
                       str(self.data, 'utf-8')+
                       str(self.previousHash,'utf-8')
                       )

            return sha.hexdigest()




def createGenisis():
    return Block(0,date.datetime.now(),"First Block","0")



def nextBlock(lastBlock):
        this_index=lastBlock.index+1;
        this_timestamp=date.datetime.now()
        this_data="Block"+ str(this_index)
        this_hash=lastBlock.hash
        return Block(this_index,this_timestamp,this_data,this_hash)






## make blockchains using above methods

blockchain=[createGenisis()]
previousBlock=blockchain[0];

## number of blockchains
noBlock=10;

for i in range(0,noBlock):
    blockAdd=nextBlock(previousBlock)
    blockchain.append(blockAdd)
    previousBlock=blockAdd

    print("Block #"+blockAdd.index+"has been added");
    print("Hash:"+blockAdd.hash);













