from mcp.server.fastmcp import FastMCP

mcp = FastMCP()


@mcp.tool()
def write_email(date: str) -> str:
    """Generate a leave request email for the given date (YYYY-MM-DD)."""
    return (
        f"Hi, all, I'll take a leave on {date}. "
        "If you have any questions, please let me know. Thanks!"
    )


if __name__ == "__main__":
    mcp.run()
