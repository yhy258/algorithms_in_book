"""
    두 리스트의 크기가 다른 경우 zero padding으로 매꿔주면 된다.
    하지만 이 코드에서는 길이가 같다는 가정을 기저에 깔고 간다.
"""



def binary_safe_padding(x,y):
    """
    :param x: input list x
    :param y: input list y
    :return: safe padding results padded_x, padded_y
    """
    # Casting
    if not isinstance(x, str):
        x = str(x)
    if not isinstance(y, str):
        y = str(y)
    if len(x) == len(y):
        return x, y
    max_len = max(len(x), len(y))
    if len(x) > len(y):
        y= "0" * (len(x) - len(y)) + y
    else :
        x = "0" * (len(y) - len(x)) + x
    return x, y

def binary_add(x, y):
    x,y = binary_safe_padding(x,y)
    assert len(x) == len(y), "Same Length Lists"

    """
        두 factor의 boolean or binary 값이 달라야 True가 되는 XOR operation이 굉장히 유용하게 사용될 수 있다.
        이진수의 덧셈을 직접 해보면 감이 올것이다.
    """
    prev_factor = 0
    result = ""
    for i in range(len(x)- 1, -1, -1):
        a, b = int(x[i]), int(y[i]) # 논리 연산자들을 사용해주기 위해서 int형으로 바꿔줍시다.
        now = (a ^ b) ^ prev_factor
        result = str(now) + result
        prev_factor = (a and b) or (b and prev_factor) or (prev_factor and a) # 2개 이상의 factor가 1이라면 그 다음에 1을 더해줘야한다.
    if prev_factor: # final iteration이 끝나고 나서 이전 팩터의 영향이 남아있다면 1을 더해준다.
        result = "1" + result
    return result


def binary_multiplication(x, y):
    x, y = binary_safe_padding(x, y)
    assert len(x) == len(y), "Same Length Lists"
    n = len(x)
    """
        카라추바 알고리즘에 의거하여 T(n) = 4T(n/2) + O(n) -> 3T(n/2) + O(n)으로 바꿔볼 수 있다.
    """

    if n == 0:
        return 0
    elif n == 1:
        return int(x) * int(y)
    xl, xr = x[:n//2] ,x[n//2:]
    yl, yr = y[:n//2], y[n//2:]
    P1 = binary_multiplication(xl,yl)
    P2 = binary_multiplication(xr, yr)
    P3 = binary_multiplication(binary_add(xl, xr), binary_add(yl, yr))
    return P1 * 2** (2 *(n - n //2)) + (P3 - P2 - P1) * 2 ** (n - n//2) + P2 # 시프트 연산으로 power of 2를 적용해주자.


if __name__ == "__main__":
    print("Padding 확인, Input : 100, 1 , Result : {}".format(binary_safe_padding("100", "1")))
    print("Binary form의 Add. Input : 101, 111, Result : {}".format(binary_add("101", "111")))
    print("Binary Multiplication. Input : 111, 10, Result : {}".format(binary_multiplication(111, 10)))