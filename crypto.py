
def crypto(text):
    text=input('Enter a text to be ')
    text=text.split()
    ALPHABET=['A','B','C','D','E,'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_text=[]
    for i in text:
        temp_word=[]
        for ii in i:
            if ord(ii) in [89,90,121,122]:
                temp_word.append(chr(ord(ii)-24))
            else:
                temp_word.append(chr(ord(ii)+2))
        new_text.append(''.join(temp_word))
    return new_text
cyrpto('ilkay arslanoglu')
        
        
        