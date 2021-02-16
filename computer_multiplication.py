"""
简单的乘法实现
原理: 10进制数转换为2进制保存在计算机中如 5 = 0101, 7 = 0111
当0101向左移动1位变为 1010其十进制为10 = 5 * 2，即向左移动以为表示该数乘于2，不移动表示该数乘于1
7 * 5 = 7 * (2 + 2 + 1)所以计算7 * 5的步骤为7 = 0111， 0111向左移动一位 + 0111向左移动一位 + 0111不移动
"""


def multiplication(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("类型错误")
    if a == 0 or b == 0:
        return 0
    # 保证b为较小数，减少复杂度
    if a < b:
        a, b = b, a
    # 将被乘数转换为二进制如 -5 : [1, 1, 0, 1], 高位为1代表负数
    b_binary = convert_to_binary(b)
    # 转换为二进制的有效位数，除去符号位
    bit_index = len(b_binary) - 1
    # 记录结果
    ans = 0
    for b in b_binary[1:]:
        bit_index -= 1
        if b:
            ans += a << bit_index
    # 高位为1表示负数，变换符号
    return 0 - ans if b_binary[1] else ans


def convert_to_binary(num):
    if not isinstance(num, int):
        raise
    ans = []
    t = abs(num)
    while t:
        ans.append(t % 2)
        t = t >> 1  # 等价 num // 2
    # 高位为1表示负数， 0表示正数
    if num < 0:
        ans.append(1)
    else:
        ans.append(0)
    return ans[::-1]


if __name__ == '__main__':
    try:
        print(multiplication(25, -4))
        print(multiplication(-25, -4))
    except Exception as exc:
        print(exc)
