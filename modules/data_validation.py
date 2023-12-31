import re

def input_noTelepon(nomor):
    try :
        if len(str(nomor)) == 12: 
            try:
                regex_pattern = re.compile(r'\b08\d{10}\b')
                nomor_hp = regex_pattern.search(str(nomor))
                return str(nomor_hp.group(0))
            except AttributeError as err:
                return err
        else:
            return Exception
    except AssertionError as err:
        return err
    
def input_nama(nama):
    if bool(nama) == True:
        return str(nama)
    else:
        return Exception
