import hashlib
import random
import BlocksDatabase
import datetime


def miner(transactions):
    # print(transactions)
    name = "user"
    blocklimit = 2
    tohash = ""
    for i in transactions:
        transact = list(i)
        for j in transact:
            tohash = tohash + str(j)
    #name = tohash.split()
    #print(name[0])
    while True:
        newtohash = tohash.encode("UTF-8")
        # print("newtohash: ",newtohash)
        blocktransactions = hashlib.sha256(newtohash)
        previoushash = BlocksDatabase.GetHash()
        #previoushash = "NA"
        previousblockhash = previoushash
        time = datetime.datetime.now()
        nonce = random.randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999)
        curtohash = str(blocktransactions)+str(previousblockhash)+str(time)+str(nonce)+str(name)+str(blocklimit)
        topasshash = curtohash.encode("UTF-8")
        current_hash = hashlib.sha256(topasshash)
        # print(current_hash)
        #if current_hash.startswith("0"):
        msg = str(name)+"_"+str(current_hash)+"_"+previousblockhash+"_"+tohash+"_"+str(time)+"_"+str(nonce)+"_"+str(blocklimit)
        # print(msg)
        BlocksDatabase.AddBlock(msg)
        break
        #else: continue

#miner("SYSTEM SYSTEM 0.0 0")