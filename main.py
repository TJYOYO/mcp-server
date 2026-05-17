from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def writeEmail(date: str):
    """
    Writes an email to the user.
    """
    print(f"Email: Hi, all, I'll take a leave on {date}, if has any problem, please let me know. Thanks!")

def main():
    print("Hello from mcp-server!")


if __name__ == "__main__":
    mcp.run()
