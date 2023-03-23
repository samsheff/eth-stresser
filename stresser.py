from web3 import Web3

# Connect to Ethereum network
w3 = Web3(Web3.HTTPProvider(''))

# Set sender address and private key
sender_address = ""
sender_private_key = ""

# Set recipient address
recipient_address = ""

# Set Number of Transactions to send
number_of_transactions = 100

# Set transaction parameters
value = 100000000000000 # 0.0001 ETH
gas = 200000
gas_price = 5000000000 # 5 Gwei

# Create and sign transactions
signed_txs = []
nonce = w3.eth.get_transaction_count(sender_address)
for i in range(number_of_transactions):
    tx = {
        'nonce': nonce + i,
        'to': recipient_address,
        'value': value,
        'gas': gas,
        'gasPrice': gas_price,
    }
    signed_tx = w3.eth.account.sign_transaction(tx, sender_private_key)
    signed_txs.append(signed_tx)

# Broadcast transactions to Ethereum network
for signed_tx in signed_txs:
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Transaction submitted with hash:", tx_hash.hex())
