#Modulo que contiene un divisor basico a partir de caracters
from dfrtokenuniverse.constantes import KDfrNlp 
class TextSplitter():
    def __init__(self):
        self.K = KDfrNlp()
        self.splitted = []
        self.fragmento = ""
        self.tipo_fragmento = 0
    def reset(self):
        self.splitted = []
    def _evalua_char_in(self, caracter, tipo_entrante, max_len=50):
        """ Funcion interna que contabiliza segun el tipo de caracter
        """
        if self.tipo_fragmento == tipo_entrante:
            if len(self.fragmento) >= max_len:
                self.splitted.append((self.tipo_fragmento, self.fragmento))
                self.fragmento = caracter
            else:
                self.fragmento += caracter
        else:
            if self.fragmento > "":
                self.splitted.append((self.tipo_fragmento, self.fragmento))
            self.fragmento = caracter
            self.tipo_fragmento = tipo_entrante
    def split_by_type(self, texto, max_len=50):
        self.splitted = []
        if isinstance(texto, bytes):
            texto_ok = texto.decode("utf-8")
        else:
            texto_ok = f"{texto}"
        self.fragmento = ""
        self.tipo_fragmento = ""
        for caracter in texto_ok:
            if caracter in self.K.CHAR_TTKN:
                if caracter == "\xa0":
                    self._evalua_char_in(" ", self.K.CHAR_TTKN[caracter], max_len)
                else:
                    self._evalua_char_in(caracter, self.K.CHAR_TTKN[caracter], max_len)
            else:
                self._evalua_char_in(caracter, self.K.TTKN_UNK, max_len)
                self.splitted.append((self.tipo_fragmento, self.fragmento))
                self.fragmento = ""
                self.tipo_fragmento = ""
        if self.fragmento > "":
            self.splitted.append((self.tipo_fragmento, self.fragmento))
        return self.splitted
    def normalize_n_gram(self, n_gram):
        """Codificador de n-gramas para usar siempre n-gramas en minuscula
           precedidos de una marca de mayuscula total (UPPER) o solo la primara (CAP)
        args:
            n_gram: enegrama o token a evaluar
        return:
            list con tokens y n-grama normalizados
        """
        if isinstance(n_gram, str):
            # Es un n-grama
            if n_gram[0] in self.K.TIPOS_TKN[self.K.TTKN_LET]:
                # Es una letra, comprobamos mayusculas
                if n_gram.upper() == n_gram:
                    return [self.K.UPPER_TOKEN ,n_gram.lower(), self.K.LOWER_TOKEN]
                elif len(n_gram) == 1:
                    return [n_gram.lower()]
                else:
                    if n_gram[0].upper() == n_gram[0] and n_gram[1:].lower() == n_gram[1:]:
                        return [self.K.CAP_TOKEN ,n_gram.lower()]
                    else:
                        return [n_gram.lower()]
            else:
                return [n_gram.lower()]
        else:
            return [n_gram]
