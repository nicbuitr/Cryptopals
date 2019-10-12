def encrypt_char(c, key_index, key_bytes):
    '''
    XORs a given character's integer representation with the key byte
    corresponding to the given key index. Returns the formatted result.
    '''
    encrypted_hex = hex(ord(c) ^ key_bytes[key_index])
    formatted_hex_str = encrypted_hex[2:].zfill(2)

    return formatted_hex_str


def main():
    plaintext = ("Burning 'em, if you ain't quick and nimble\n"
                 "I go crazy when I hear a cymbal")
    key = "ICE"
    key_bytes = [ord(c) for c in key]

    # Define a list comprehension that sequentially encrypts each ptext char
    ctxt_list = [
        encrypt_char(plaintext[i], i % 3, key_bytes)
        for i in range(len(plaintext))
    ]
    ciphertext = "".join(ctxt_list)  # Join all byte strings into one

    # Check if the our ciphertext matches the one provided by Cryptopals
    given_ctxt = ("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a2"
        "6226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b2028"
        "3165286326302e27282f")
    assert ciphertext == given_ctxt
    print(f"Successful encryption: the encrypted plaintext is {ciphertext}")


if __name__ == "__main__":
    main()
