
Natural = list # 自然数型(型別名)

zero: Natural = []
one: Natural = [zero]
two: Natural = [zero, one]
three: Natural = [zero, one, two]
four: Natural = three + [three]
five: Natural = four + [four]
six: Natural = five + [five]

# 1を足す関数 後者関数 successor function
def suc(x: Natural) -> Natural:
    """ x + 1 を計算する"""
    return x + [x]

# 1を引く関数 前者関数 predecessor function
def pre(x: Natural) -> Natural:  
    """ x - 1 を計算する x=0ならエラー"""
    if x == zero:
        assert False
    return x[:-1]

def is_bigger(x: Natural, y: Natural) -> bool:
    """ x < y かを判定する"""
    return x in y

def plus(x: Natural, y: Natural) -> Natural:
    """x+yを計算する"""
    if y == zero:
        return x  # x + 0 = x
    else:
        return plus(suc(x), pre(y))  # x+y = (x+1)+(y-1)

def mul(x: Natural, y: Natural) -> Natural:
    """x * y を計算する"""
    if y == zero:
        return zero  # x * 0 = 0
    else:
        # x * y = x * (y-1) + x
        return plus(mul(x, pre(y)), x)  
    
def N2int(x: Natural) -> int:
    """Natural型をint型に変換するデバッグ用関数"""
    return len(x)

# x - y = z
# x     = z + y

# a - b = c - d
# a + d = c + b

Integer = tuple[Natural, Natural]

zero_i   : Integer = (zero , zero)  # 整数型 0
one_i    : Integer = (one  , zero)  # 整数型 1
two_i    : Integer = (two  , zero)  # 整数型 2
three_i  : Integer = (three, zero)  # 整数型 3
four_i   : Integer = (four , zero)  # 整数型 4
m_one_i  : Integer = (zero , one )  # 整数型 -1
m_two_i  : Integer = (zero , two )  # 整数型 -2

def N2I(x: Natural) -> Integer:
    return (x, zero)

def eq_i(x: Integer, y: Integer) -> bool:
    """x[0] - x[1] == y[0] - y[1] かを判定する"""
    return plus(x[0], y[1]) == plus(y[0], x[1])  

def plus_i(x: Integer, y: Integer) -> Integer:
    """ x+y を計算する"""
    # a-b + c-d = (a+c) - (b+d)
    return (plus(x[0], y[0]), plus(x[1], y[1]))

def neg_i(x: Integer) -> Integer:
    """ -x を計算する"""
    return (x[1], x[0])

def minus_i(x: Integer, y: Integer) -> Integer:
    """ x-y を計算する"""
    return plus_i(x, neg_i(y)) # x-y = x + (-y)

def mul_i(x: Integer, y: Integer) -> Integer:
    """ x*y を計算する """
    # x * y = x * (y[0] - y[1]) = x * y[0] - x * y[1]
    x_mul_y0: Integer = (mul(x[0],y[0]), mul(x[1],y[0]))  # x * y[0]
    x_mul_y1: Integer = (mul(x[0],y[1]), mul(x[1],y[1]))  # x * y[1]
    return minus_i(x_mul_y0, x_mul_y1)

def I2int(x: Integer) -> int:
    """Integer型をint型に変換するデバッグ用関数"""
    return N2int(x[0])-N2int(x[1])

Rational = tuple[Integer, Integer]

# a / b = c / d
# a * d = c * b 

half: Rational = (one_i, two_i) # 分数型 1/2
quarter: Rational = (one_i, four_i) # 分数型 1/4
two_r : Rational = (two_i, one_i) # 分数型 2
three_quarter: Rational = (three_i, four_i) # 分数型 3/4

def eq_r(x: Rational, y: Rational) -> bool:
    """ x==y かを判定する"""
    return eq_i(
        mul_i(x[0], y[1]),
        mul_i(x[1], y[0])
    )

def mul_r(x: Rational, y: Rational) -> Rational:
    """ x*y を計算する"""
    return (mul_i(x[0], y[0]), mul_i(x[1], y[1]))

def div_r(x: Rational, y: Rational) -> Rational:
    """ x/y を計算する"""
    return (mul_i(x[0], y[1]), mul_i(x[1], y[0]))

def neg_r(x: Rational) -> Rational:
    """ -x を計算する"""
    return (neg_i(x[0]), x[1])

def plus_r(x: Rational, y: Rational) -> Rational:
    """ x+y を計算する"""
    #    x[0]/x[1] + y[0]/y[1] 
    # = (x[0]y[1]+x[1]y[0]) / x[1]y[1]
    numerator = plus_i(mul_i(x[0], y[1]), mul_i(x[1], y[0]))
    denominator = mul_i(x[1], y[1])
    return (numerator, denominator)

def minus_r(x: Rational, y: Rational) -> Rational:
    """ x-y を計算する"""
    return plus_r(x, neg_r(y))

def print_r(x: Rational) -> Rational:
    """Rational型をprintするデバッグ用関数"""
    print(I2int(x[0]), "/", I2int(x[1]))



################################################
################################################
################################################




assert plus(two, three) == five
assert is_bigger(two, three) == True
assert is_bigger(three, three) == False
assert is_bigger(two, zero) == False
assert mul(zero, three) == zero
assert mul(two, zero) == zero
assert mul(one, three) == three
assert mul(three, one) == three
assert mul(two, two) == four
assert (
    eq_i(
        plus_i(m_one_i, one_i),
        zero_i
    )
)
assert eq_i(mul_i(one_i, one_i),  one_i)
assert eq_i(mul_i(two_i, m_one_i),  neg_i(N2I(two)))
assert I2int(mul_i(two_i, m_one_i)) == -2

# print_r(mul_r(three_quarter, three_quarter))
# print_r(div_r(three_quarter, three_quarter))
# print_r(plus_r(half, three_quarter))
# print_r(minus_r(half, three_quarter))
# print_r(neg_r(three_quarter))

