from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices
from pprint import pprint


if __name__ == "__main__":
   
    # Connect to client
    try:
        cpprint("Connecting to Client")
        client = connect_dydx()
    except Exception as e:
        cpprint("Error connecting to Client: ", e)
        exit(1)

    # Abort all open positions
    if ABORT_ALL_POSITIONS:
        try:
            cpprint("Closing all positions...")
            close_orders = abort_all_positions(client)
        except Exception as e:
            cpprint("Error closing all positions: ", e)
            exit(1)
    
    # Find Cointegrated Pairs
    if FIND_COINTEGRATED:
        
        # Construct Market Prices
        try:
            print("Fetching market prices, please wait...")
            df_market_prices = construct_market_prices(client)
        except Exception as e:
            print("Error contructing market prices: ", e)
            exit(1)
