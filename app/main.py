from pyscript import document

def hashCode(self):
    input_text = document.querySelector("#text")
    input_text = input_text.value
    i = len(input_text)-1
    for _ in range(len(input_text)):
        hash_code += int(ord(input_text[_]))*31**(i)
        i-=1
    hash = genHash(hash_code)
    output_div = document.querySelector("#output")
    output_div.innerText = "Hash Code\n\n" + str(hash)

def genHash(hash_code):
    hash = hash_code % 10**32
    return hash