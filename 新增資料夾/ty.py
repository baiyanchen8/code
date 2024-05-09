def diffie_hellman(p, g, a, b):
    # Alice計算A = g^a mod p
    A = mod_exp(g, a, p)
    # Bob計算B = g^b mod p
    B = mod_exp(g, b, p)
    # Alice和Bob交換A和B
    # Alice計算共享金鑰K = B^a mod p
    K1 = mod_exp(B, a, p)
    # Bob計算共享金鑰K = A^b mod p
    K2 = mod_exp(A, b, p)
    # 返回共享金鑰
    return K1, K2
def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result
# 定義公共參數
p = 23  # 大質數p
g = 5   # 原根g

# Alice和Bob各自選擇私鑰
a = 6
b = 15

# 進行Diffie-Hellman金鑰交換
alice_key, bob_key = diffie_hellman(p, g, a, b)

# 輸出共享金鑰
print("Alice的共享金鑰:", alice_key)
print("Bob的共享金鑰:", bob_key)
