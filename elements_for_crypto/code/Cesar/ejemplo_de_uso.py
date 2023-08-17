from tools_for_letters import *
from crypto_Cesar import *


if __name__ == "__main__":
    message = 'holamundo' # no usar espacios
    print(message)
    my_list = message2list_of_digits(message)
    print("plane: ", my_list)
    my_key = 11
    my_encrypted = encrypt_Cesar(my_list, my_key)
    print("chiper: ", my_encrypted)
    my_key_decryp = len(alphabet) - my_key
    my_decrypted = decrypt_Cesar(my_encrypted, my_key_decryp)
    print("again plane: ", my_decrypted)