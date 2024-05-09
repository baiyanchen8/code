import random
import sympy

def generate_rsa_keypair(bits):
    # 隨機選擇兩個大質數
    p = sympy.randprime(2**(bits//2), 2**(bits//2 + 1))
    q = sympy.randprime(2**(bits//2), 2**(bits//2 + 1))
    
    # 計算n和phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # 選擇一個與phi(n)互質的整數e
    e = random.randint(2, phi_n - 1)
    while sympy.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    
    # 計算私鑰d
    d = sympy.mod_inverse(e, phi_n)
    
    # 返回公鑰和私鑰
    return (n, e), (n, d)
def encrypt(message, public_key):
    n, e = public_key
    # 將消息轉換為整數
    m = int.from_bytes(message.encode(), 'big')
    # 使用公鑰中的指數e進行加密
    c = pow(m, e, n)
    return c

def decrypt(ciphertext, private_key):
    n, d = private_key
    # 使用私鑰中的指數d進行解密
    m = pow(ciphertext, d, n)
    # 將解密後的整數轉換為消息
    message = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
    return message
# 生成RSA金鑰對
public_key, private_key = generate_rsa_keypair(128)

# 輸出公鑰和私鑰
print("公鑰 (n, e):", public_key)
print("私鑰 (n, d):", private_key)

# 輸入要加密的消息
message = "Hello, RSA!"

# 加密消息
ciphertext = encrypt(message, public_key)
print("加密後的密文:", ciphertext)

# 解密消息
decrypted_message = decrypt(ciphertext, private_key)
print("解密後的消息:", decrypted_message)
