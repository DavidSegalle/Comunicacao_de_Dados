import matplotlib.pyplot as plt
from typing import List

# Adoro documentação redundante.

# Retorna texto criptografado (caesar cipher com dois deslocamentos).
def encrypt(message: str):
    encrypted = []
    for ch in message:
        encrypted.append(ch if ord(ch) < 32 or ord(ch) >= 128\
                         else chr((ord(ch) - 32 + 94) % 96 + 32))
    encrypted = "".join(encrypted)
    return encrypted


# Retorna texto descriptografado.
def decrypt(message: str):
    decrypted = []
    for ch in message:
        decrypted.append(ch if ord(ch) < 32 or ord(ch) >= 128\
                         else chr((ord(ch) - 32 + 2) % 96 + 32))
    decrypted = "".join(decrypted)
    return decrypted


# Retorna lista de bits a partir de um texto.
def to_binary(message: str):
    message = message.encode()
    binary = []
    for ch in message:
        for i in range(0, 8):
            binary.append(1 if ch & 1 << i != 0 else 0)
    return binary


# Retorna texto a partir de uma lista de bits.
def to_string(message: str):
    text = bytearray()
    for i in range(0, len(message), 8):
        ch = 0
        for j in range(0, 8):
            ch += 0 if message[i + j] == 0 else 1 << j
        text.append(ch)
    text = text.decode()
    return text


# Converte lista de bits para sinal digital (2B1Q).
def codLin_2b1q(binaryInfo: List[int]):
    response = []
    atN = 0
    szAns = 0
    sgn = 1
    if len(binaryInfo) % 2 == 1:
        binaryInfo.append(0)
    for i in range(0, len(binaryInfo)):
        if i % 2 == 0:
            atN +=  2 * binaryInfo[i]
            continue
        atN += binaryInfo[i]
        if atN == 0 or atN == 2:
            response.append(1)
        else:
            response.append(3)
        if atN >= 2:
            response[szAns] *= -1
        if szAns > 0 and response[szAns - 1] < 0:
            response[szAns] *= -1
        szAns += 1
        atN = 0
    return response


# Converte sinal digital para lista de bits (2B1Q).
def decodLin_2b1q(signal: List[int]):
    bitInfo = []
    ant = 1
    for el in signal:
        if ant == 1:
            if el == 1:
                bitInfo.append(0)
                bitInfo.append(0)
            elif el == 3:
                bitInfo.append(0)
                bitInfo.append(1)
            if el == -1:
                bitInfo.append(1)
                bitInfo.append(0)
            elif el == -3:
                bitInfo.append(1)
                bitInfo.append(1)
        else:
            if el == 1:
                bitInfo.append(1)
                bitInfo.append(0)
            elif el == 3:
                bitInfo.append(1)
                bitInfo.append(1)
            if el == -1:
                bitInfo.append(0)
                bitInfo.append(0)
            elif el == -3:
                bitInfo.append(0)
                bitInfo.append(1)
        ant = el > 0
    return bitInfo


# Apresenta forma de onda em gráfico.
def plot_graph(signal: List[int]):
    y = []
    if len(signal) > 0:
        y.append(signal[0])
        for el in signal:
            y.append(el)
    x = range(0, len(y))
    plt.step(x, y)
    plt.xlabel('Tempo')
    plt.ylabel('Volts')
    plt.title('Sinal mensagem')
    plt.show()

def main():

    # Teste:
    message = input()
    print(message)

    encrypted = encrypt(message)
    print(encrypted)

    binary = to_binary(encrypted)
    print(binary)

    signal = codLin_2b1q(binary)
    print(signal)
    plot_graph(signal)

    bits = decodLin_2b1q(signal)
    print(bits)

    text = to_string(bits)
    print(text)

    decrypted = decrypt(text)
    print(decrypted)

if __name__ == "__main__":
    main()