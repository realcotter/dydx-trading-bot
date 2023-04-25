from constants import ABORT_ALL_POSITIONS
from func_private import abort_all_positions
from func_messaging import send_message
from prettyprinter import cpprint
from func_connections import connect_dydx

# Connect to client
try:
    cpprint("Connecting to Client")
    client = connect_dydx()
except Exception as e:
    cpprint("Error connecting to Client: ", e)
    send_message(f"Failed to connect to client {e}")
    exit(1)


# Abort all open positions
if ABORT_ALL_POSITIONS:
    try:
        cpprint("Closing all positions...")
        close_orders = abort_all_positions(client)
    except Exception as e:
        print("Error closing all positions: ", e)
        send_message(f"Error closing positions {e}")
        exit(1)
