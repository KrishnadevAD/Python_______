import pywhatkit
ph_number = {'omit ':'9860486474','krishna':'9860486474'}
for k,v in ph_number:
    pywhatkit.text_to_handwriting(f'{k} hello hi , how are you ',rgb=(255,0,0))
    pywhatkit.sendwhats_image()
