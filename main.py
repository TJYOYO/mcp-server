from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.
    Args:
        a: The first number.
        b: The second number.
    Returns:
        The sum of a and b.
    """
    return a + b


# @mcp.tool()
# def take_leave_email(date: str) -> str:
#     """
#     take a leave request email for the given date (YYYY-MM-DD).
#     Args:
#         date: Leave date in YYYY-MM-DD format.
#     """
#     return (
#         f"Hi, all, \n\nI'll take a leave on {date}. "
#         "If you have any questions, please let me know. Thanks! \n\nBest regards, \n\nJack"
#     )

if __name__ == "__main__":
    mcp.run()
