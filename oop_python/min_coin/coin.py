'''
Given a variety of coin types defining a currency system, 
find the minimum number of coins required to express a given amount of money. 
Assume infinite supply of coins of every type.

{
"coins": [1, 3, 5],
"value": 9
}
Output = 3
'''


def helper(coins,value,result):
    if result.get(value,0):
        return result[value]
    if value == 0:
        return 1
    elif value < 0:
        return 0
    else:
        minimum = []
        for coin in coins:
            minimum.append(helper(coins,value-coin,result))
        result[value] = min(minimum)+1
        return result[value]

def minimum_coins(coins, value):
    """
    Args:
     coins(list_int32)
     value(int32)
    Returns:
     int32
    """
    # Write your code here.
    result = {}
    helper(coins,value,result)
    return result[value]


if __name__ == '__main__':
    input = {
        "coins": [2],
        "value": 9
    }

    result = minimum_coins(input["coins"], input["value"])
    assert  result == 9, f"Incorrect result {result}"

    input["coins"] = [1]
    input["value"] = 1