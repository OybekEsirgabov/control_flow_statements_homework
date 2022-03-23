def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a%2 > 0:
        x1 = a/100
    else: 
        x2 = a/100
    if (x1 > 1):
        return "two-digit odd number"
    if (x2 > 1):
        return "two-digit even number"
print(main(408))