from bitcoinlib.wallets import Wallet
from algosdk import account, encoding

######
# generate an account
private_key, address = account.generate_account() #Generates private key and address for sending ethers
print("Private key:", private_key)
print("Address:", address)

# Check if the address is valid (If the address of sender exists or not for safety)
if encoding.is_valid_address(address):
    print("The address is valid!")
else:
    print("The address is invalid.")

######

w = Wallet.create('Wallet1')
key1 = w.get_key() #Generating new address to receive ethers
x=key1.address

print("Private key:", key1)
print("Address:", x)

# Check if the address is valid (If the address of receiver exists or not for safety)
if encoding.is_valid_address(x):
    print("The address is valid!")
else:
    print("The address is invalid.")


w.scan()
w.info()  #Info() Shows wallet information, keys, transactions

#def update(transactions in) -> show the updated transactions

#Sending transactions and updating the wallet
t = w.send_to('XYZ', '1 ether')
t.info()  # Shows transaction information and send results