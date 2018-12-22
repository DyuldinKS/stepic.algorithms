def init():
    dict_len = int(input().split(' ')[0])

    huffman_dict = {}
    for i in range(0, dict_len):
        [char, code] = input().split(': ')
        huffman_dict[code] = char

    encoded_str = input()

    return (encoded_str, huffman_dict)


def decode(enc_str, huffman_dict):
    i = 0
    enc_char = ''
    dec_str = ''
    while i < len(enc_str):
        enc_char += enc_str[i]
        if enc_char in huffman_dict:
            dec_str += huffman_dict.get(enc_char)
            enc_char = ''

        i += 1

    return dec_str

(encoded_str, huffman_dict) = init()
res = decode(encoded_str, huffman_dict)
print(res)