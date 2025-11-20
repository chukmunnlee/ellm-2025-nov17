import requests
import pandas as pd

# TODO: Import fastmcp
from mcp.server.fastmcp import FastMCP

# Setup 
# Open a terminal and type the following
# source $HOME/.bashrc to set node environment

# TODO: Create MCP server
mcp = FastMCP('Crypto MCP')

@mcp.tool()
def get_crypto_price(crypto = 'bitcoin') -> str:
  """ 
  Get the price of a crypto currency

  Args:
    crypto: crypto currency symbol eg bitcoin, ethereum, etc.
  """
  currency = 'sgd'
  url = "https://api.coingecko.com/api/v3/simple/price"
  params = { "ids": crypto.lower(), "vs_currencies": currency}
  try:
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    price = data.get(crypto.lower(), {}).get(currency)
    if price is not None:
      return f"The price of {crypto} is {currency.upper()} {price}"

    return f"Price for {crypto} is not found"
  except Exception as e:
    return f"Error fetching crypto: {e}"


# TODO: Start the server
if __name__ == "__main__":
  mcp.run()
  #mcp.run(transport="streamable-http")
