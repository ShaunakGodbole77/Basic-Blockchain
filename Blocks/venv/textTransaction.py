#SIP#
import hashlib
import socket
import threading
#from BlockChainClass import BlockChain

def sendTransaction(value,reciever,crecievervalue,sender,csenderValue):
    personalledger = open("Myledger.txt","r")
    balancesheet = open("Mybalance.txt","r")
    contents = personalledger.readlines()
    balance = balancesheet.readlines()
    for n in balance:
        param = n.split()
        if param[0] == sender and param[1] == csenderValue and int(value) < int(csenderValue):
            for i in contents:
                j =i.split()
                if j[0] == reciever and j[1] == crecievervalue:
                    msgtosnd = f"$ {value} {reciever} {crecievervalue} {sender} {csenderValue}"
                    personalledger.close()
                    balancesheet.close()
                    return msgtosnd
                else: continue
            else: continue
        else: continue
    personalledger.close()
    balancesheet.close()
    return "false"

def sendTransactionhash(value,reciever,crecievervalue,sender,csenderValue):
    personalledger = open("Myledger.txt", "r")
    balancesheet = open("Mybalance.txt", "r")
    contents = personalledger.readlines()
    balance = balancesheet.readlines()
    for n in balance:
        param = n.split()
        if param[0] == sender and param[1] == csenderValue and value < csenderValue:
            for i in contents:
                j = i.split()
                if j[0] == reciever and j[1] == crecievervalue:
                    msgtosnd = f"$ {value} {reciever} {crecievervalue} {sender} {csenderValue}"
                    personalledger.close()
                    balancesheet.close()
                    TransactionHash = hashlib.sha256(msgtosnd)
                    return TransactionHash
                else:
                    continue
            else:
                continue
        else:
            continue
    personalledger.close()
    balancesheet.close()


def recieveTransaction(recieved):
    count = 0
    checkhash = hashlib.sha256(recieved)
    if checkhash != recievedhash:
        return "fail"
    else:
        messagecomponents = recieved.split()
        thisledger = open("ThisLedger.txt","r")
        ledgercheck = thisledger.readlines()
        balancesheet = open("Mybalance1.txt", "r")
        balance = balancesheet.readlines()
        if int(messagecomponents[1]) < int(messagecomponents[5]):
            for i in ledgercheck:
                count += 1
                if i.startswith(messagecomponents[4]):
                    j=i.split()
                    if j[1] == messagecomponents[5]:
                        for m in balance:
                            n = m.split()
                            if n[0] == messagecomponents[2]:
                                if n[1] == messagecomponents[3]:
                                    ledgercheck[count] = f"{messagecomponents[4]} {int(messagecomponents[5]) - int(messagecomponents[1])}"
                                    balance[0] = f"{messagecomponents[2]} {int(messagecomponents[3]) + int(messagecomponents[1])}"
                                    thisledger.close()
                                    balancesheet.close()
                                    for line in ledgercheck:
                                        thisledger = open("ThisLedger.txt", "w")
                                        thisledger.write(line)
                                        thisledger.close()
                                    for new in balance:
                                        balancesheet = open("Mybalance1.txt", "w")
                                        balancesheet.write(new)
                                        balancesheet.close()
                                    return "success"
                                else: continue
                            else: continue
                    else: continue
                else: continue
        else: return "fail"

def recieveTransactionhash(hash1):
    global recievedhash
    recievedhash = hash1