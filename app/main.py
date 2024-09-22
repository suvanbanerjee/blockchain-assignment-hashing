from pyscript import document

def hashCode(self):
    input_text = document.querySelector("#text")
    input_text = input_text.value
    hash_code = 0
    i = len(input_text)-1
    for _ in range(len(input_text)):
        hash_code += int(ord(input_text[_]))*31**(i)
        i-=1
    hash = hash_code % 10**32
    hash = hex(hash)
    if input_text == "":
        hash = "Seriously? What are you expecting black magic?"
    output_div = document.querySelector("#output")
    output_div.innerText = "Hash - " + str(hash)
