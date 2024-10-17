from web3 import Web3
from colorama import Fore, Style

# List of Ethereum RPC server addresses with aliases
ethereum_rpc_info = {
    "https://mainnet.infura.io/v3/[your ID]": "ETHEREUM",
    "https://linea-mainnet.infura.io/v3/[your ID]": "LINEA",
    "https://polygon-mainnet.infura.io/v3/[your ID]": "POLYGON",
    "https://arbitrum-mainnet.infura.io/v3/[your ID]": "ARBITRUM",
    "https://optimism-mainnet.infura.io/v3/[your ID]": "OPTIMISM"
}
def get_gas_price(web3):
    try:
        # Get the current gas price
        gas_price = web3.eth.gas_price
        # Convert from Wei to Gwei
        gas_price_in_gwei = web3.from_wei(gas_price, 'gwei')
        return gas_price_in_gwei
    except Exception as e:
        print("An error occurred:", e)
        return None

# Iterate through the list of Ethereum RPC server addresses
for rpc_url, rpc_alias in ethereum_rpc_info.items():
    # Initialize the Web3 object for the selected RPC address
    web3 = Web3(Web3.HTTPProvider(rpc_url))

    # Call the function to fetch the gas price
    gas_price = get_gas_price(web3)
    if gas_price is not None:
        print(Fore.CYAN + f"Gas price in the {rpc_alias} network: {gas_price} Gwei")
    else:
        print(Fore.RED + f"Failed to retrieve gas price for the {rpc_alias} network")

    print(Fore.YELLOW + "---------------------------------------------" + Style.RESET_ALL)
