def create_dict(map_from, map_to, code):
#    print (map_from)
#    print(map_to)
#    print(code)
    i=0
    dict_cipher=dict()
    for i in range(len(map_from)):
        key=map_from[i]
        value=map_to[i]
        try:
            dict_cipher[key]=value
        except:
            pass
    return dict_cipher

def coding(dict_cipher, code):
    l_message=list()
    for letter in code:
        l_message.append(dict_cipher[letter])
    s_message=''.join(l_message)
    return s_message


def cipher(map_from, map_to, code):
    #create a cipher dictionary
    dict_cipher=dict()
    dict_cipher=create_dict(map_from, map_to, code)
#    print(dict_cipher)

    #code the message
    message=coding(dict_cipher, code)
#    print(message)

    #compile the result as the requested format
    result=(dict_cipher, message)
#    print(result)
    return result