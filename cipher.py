import matplotlib.pyplot as plt
from typing import List


def encrypt(message: str):
    encrypted = []
    for ch in message:
        # Utiliza cifra de cesar com tres deslocamentos.
        # Afeta somente caracteres ASCII imprimiveis.
        encrypted.append(ch if ord(ch) < 32 or ord(ch) >= 128 \
                         else chr((ord(ch) - 32 + 3) % 96 + 32))
    return ''.join(encrypted)


def decrypt(message: str):
    decrypted = []
    for ch in message:
        # -3 = 93 (mod 96).
        decrypted.append(ch if ord(ch) < 32 or ord(ch) >= 128 \
                         else chr((ord(ch) - 32 + 93) % 96 + 32))
    return ''.join(decrypted)


def to_binary(text: str):
    text = text.encode('latin_1')
    # Converte texto para lista de bits.
    binary = []
    for ch in text:
        for i in range(0, 8):
            binary.append(0 if ch & 1 << i == 0 else 1)
    return binary


def to_text(binary: List[int]):
    # Converte lista de bits para texto.
    text = bytearray()
    for i in range(0, len(binary), 8):
        ch = 0
        for j in range(0, 8):
            ch += 0 if binary[i + j] == 0 else 1 << j
        text.append(ch)
    text = text.decode('latin_1')
    return text


def encode_2b1q(binary: List[int]):
    # Converte dados digitais para sinal digital.
    signal = []
    if len(binary) % 2 == 1:
        binary.append(0)
    for i in range(0, len(binary), 2):
        el = (binary[i] << 1) + binary[i + 1]
        if el == 0 or el == 2:
            signal.append(1)
        else:
            signal.append(3)
        if el >= 2:
            signal[-1] *= -1
        if len(signal) > 1 and signal[-2] < 0:
            signal[-1] *= -1
    return signal


def decode_2b1q(signal: List[int]):
    # Converte sinal digital para dados digitais.
    binary = []
    is_prev_positive = True
    for el in signal:
        if is_prev_positive:
            if el == 1:
                binary.extend([0, 0])
            elif el == 3:
                binary.extend([0, 1])
            if el == -1:
                binary.extend([1, 0])
            elif el == -3:
                binary.extend([1, 1])
        else:
            if el == 1:
                binary.extend([1, 0])
            elif el == 3:
                binary.extend([1, 1])
            if el == -1:
                binary.extend([0, 0])
            elif el == -3:
                binary.extend([0, 1])
        is_prev_positive = el > 0
    return binary


def plot_graph(signal: List[int], title: str):
    plt.clf()
    y = []
    if len(signal) > 0:
        y.append(signal[0])
        for el in signal:
            y.append(el)
    x = range(0, len(y))
    plt.step(x, y)
    plt.xlabel('Tempo')
    plt.ylabel('Nível')
    plt.title(title)
    #plt.show()
    return plt.gcf()


def send_signal(signal: List[int]):
    data = bytearray()
    for el in signal:
        if el == -3:
            data.append(0)
        elif el == -1:
            data.append(1)
        elif el == 1:
            data.append(2)
        elif el == 3:
            data.append(3)
    return data


def receive_signal(data):
    signal = []
    for ch in data:
        if ch == 0:
            signal.append(-3)
        elif ch == 1:
            signal.append(-1)
        elif ch == 2:
            signal.append(1)
        elif ch == 3:
            signal.append(3)
    return signal


def main():
    # Teste:
    message = input()
    print(message)

    encrypted = encrypt(message)
    print(encrypted)

    binary = to_binary(encrypted)
    print(binary)

    signal = encode_2b1q(binary)
    print(signal)
    plot_graph(signal)

    bits = decode_2b1q(signal)
    print(bits)

    text = to_text(bits)
    print(text)

    decrypted = decrypt(text)
    print(decrypted)

if __name__ == "__main__":
    main()
