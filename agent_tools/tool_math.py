import os
import math
import json

from dotenv import load_dotenv
from fastmcp import FastMCP

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.general_tools import get_config_value
load_dotenv()

mcp = FastMCP("Math")


@mcp.tool()
def financial_calculator(expression: str) -> str:
    """
    A high-precision financial calculator for evaluating mathematical expressions.
    Use this to calculate intraday volatility, price changes, and risk ratios.
    Example expression: "(high - low) / open" or "(current - entry) / entry"
    """
    # log_file = get_config_value("LOG_FILE")
    # signature = get_config_value("SIGNATURE")
    
    try:
        allowed_names = {
            "abs": abs, "round": round, "min": min, "max": max,
            "sqrt": math.sqrt, "pow": pow, "__builtins__": None
        }

        result = eval(expression, {"__builtins__": None}, allowed_names)
        formatted_result = f"{float(result):.6f}"

        # log_entry = {
        #     "signature": signature,
        #     "new_messages": [
        #         {
        #             "role": "tool:financial_calculator", 
        #             "content": f"Calc: {expression} => {formatted_result}"
        #         }
        #     ]
        # }
        # with open(log_file, "a", encoding="utf-8") as f:
        #     f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

        return formatted_result

    except Exception as e:
        error_msg = f"Calculation Error: {str(e)}"
        return error_msg

# function add and multiply is the original tool
'''
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers (supports int and float)"""
    # log_file = get_config_value("LOG_FILE")
    # signature = get_config_value("SIGNATURE")
    # log_entry = {
    #     "signature": signature,
    #     "new_messages": [{"role": "tool:add", "content": f"{a} + {b} = {float(a) + float(b)}"}]
    # }
    # with open(log_file, "a", encoding="utf-8") as f:
    #     f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
    return float(a) + float(b)


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers (supports int and float)"""
    # log_file = get_config_value("LOG_FILE")
    # signature = get_config_value("SIGNATURE")
    # log_entry = {
    #     "signature": signature,
    #     "new_messages": [{"role": "tool:multiply", "content": f"{a} * {b} = {float(a) * float(b)}"}]
    # }
    # with open(log_file, "a", encoding="utf-8") as f:
    #     f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
    return float(a) * float(b)
'''

if __name__ == "__main__":
    port = int(os.getenv("MATH_HTTP_PORT", "8000"))
    mcp.run(transport="streamable-http", port=port)
