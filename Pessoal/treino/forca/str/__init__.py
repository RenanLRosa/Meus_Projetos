import re
def teste_acento(palavra):
    if 'á' or 'ã' or 'à' or 'â' in palavra:
        palavra = re.sub(r'[âãáà]', 'a', palavra)
    if 'é' or 'è' or 'ê' in palavra:
        palavra = re.sub(r'[éèê]', 'e', palavra)
    if 'í' or 'ì' or 'î' in palavra:
        palavra = re.sub(r'[íìî]', 'i', palavra)
    if 'ó' or 'õ' or 'ò' or 'ô' in palavra:
        palavra = re.sub(r'[óòõô]', 'o', palavra)
    if 'ú' or 'ù' or 'û' in palavra:
        palavra = re.sub(r'[úùû]', 'u', palavra)
    return palavra