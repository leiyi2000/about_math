"""
简单二进制加法实现(不考虑符号问题)
实现原理: 考虑该计算式 1010 + 0111

    1 0 1 0
+   0 1 1 1
--------------
  1 0 0 0 1
在计算过程中需要考虑低位产生的进位信息，初始进位 carry = 0,
当前位加后的结果: carry ^ a(i) ^ b(i)
当前位产生的进位数: a(i) & b(i) | carry & (a(i) | b(i))

问题和说明: 8位的有效范围: -127 - 127, 对于保存-128还没想到好的解决方法
          每次遍历计算都依赖前项产生的进位信息，效率慢，解决办法：超前进位加法器
          无法计算负数相加问题，可以采用补码的方式计算解决问题
"""


def adder(a, b, max_len):
    if not isinstance(a, int) or not isinstance(b, int):
        raise
    # 转换位二进制，由数组保存
    a_binary = convert_to_binary(a, max_len)
    b_binary = convert_to_binary(b, max_len)
    # 记录结果
    ans = [0] * max_len
    # 开始进位为0
    carry = 0
    for i in range(max_len - 1, -1, -1):
        ans[i] = carry ^ a_binary[i] ^ b_binary[i]
        carry = a_binary[i] & b_binary[i] | carry & (a_binary[i] | b_binary[i])
    return ans


def convert_to_binary(num, max_len):
    if not isinstance(num, int): raise
    ans = []
    t = abs(num)
    length = 0
    while length < max_len - 1:
        ans.append(t % 2)
        length += 1
        t = t >> 1  # 等价 num // 2
    # 大数无法保存
    if t != 0:
        raise
    # 添加符号位高位为1表示负数， 0表示正数
    if num < 0:
        ans.append(1)
    else:
        ans.append(0)

    return ans[::-1]


if __name__ == '__main__':
    print(adder(6, 8, 8))
