#Modulo que contiene un divisor basico a partir de caracters
from dfrtokenuniverse.constantes import KDfrNlp 
class SplitTextTokens():
    def __init__(self):
        self.version = "0.3"
        self.K = KDfrNlp()
        self.splitted = []
        self.fragmento = ""
        self.tipo_fragmento = 0
    def reset(self):
        self.splitted = []
    # Funcion interna que evalua el caracter segun el tipo de caracter
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
    # Funcion que divide un texto en tokens segun el tipo de caracter
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
           precedidos de una marca numerica de mayuscula total (UPPER) o solo la primara (CAP)
        args:
            n_gram: enegrama o token a evaluar
        return:
            list con tokens y n-grama normalizados
        """
        if isinstance(n_gram, str):
            # Es un n-grama
            if n_gram[0] in self.K.TIPOS_TKN[self.K.TTKN_LET]:
                # Es una letra, comprobamos mayusculas
                if n_gram.upper() == n_gram and n_gram.lower() == n_gram:
                    # No hay letras
                    return [n_gram]
                elif n_gram.upper() == n_gram:
                    # Hay letras y en mayusculas
                    return [self.K.MAIN_TOKEN_DICT[self.K.UPPER_TOKEN], n_gram.lower(), self.K.MAIN_TOKEN_DICT[self.K.LOWER_TOKEN]]
                elif len(n_gram) == 1:
                    # Con una sola letra no podemos comprobar capitalizada
                    return [n_gram]
                else:
                    if n_gram[0].upper() == n_gram[0] and n_gram[1:].lower() == n_gram[1:]:
                        # Es una palabra capitalizada
                        return [self.K.MAIN_TOKEN_DICT[self.K.CAP_TOKEN], n_gram.lower()]
                    else:
                        # O no es una capitalizada o es en minusculas o es otra cosa
                        return [n_gram.lower()]
            else:
                return [n_gram.lower()]
        else:
            return [n_gram]
    # Funcion que divide una palabra en silabas
    def _split_silaba(self, palabra, dic_splitter):
        """Funcion interna que divide un texto en silabas
        """
        silabizado = []
        for silabico in self.K.SILABICOS:
            if "*" in silabico:
                prueba = silabico.replace("*", "")
                i_ini = 0
                while prueba in palabra[i_ini:]:
                    i_silaba = i_ini + palabra[i_ini:].index(prueba)
                    if i_silaba > 0 and palabra[i_silaba - 1] in "aeiouáéíóú":
                        if silabico in dic_splitter:
                            dic_splitter[silabico] += 1
                        else:
                            dic_splitter[silabico] = 1
                        silabizado.extend(self._split_silaba(palabra[:i_silaba + self.K.SILABICOS[silabico]], dic_splitter))
                        if i_silaba + self.K.SILABICOS[silabico] < len(palabra):
                            silabizado.extend(self._split_silaba(palabra[i_silaba  + self.K.SILABICOS[silabico]:], dic_splitter))
                        return silabizado
                    i_ini = i_silaba + 1
            elif silabico in palabra:
                i_silaba = palabra.index(silabico)
                if (i_silaba > 0) or len(silabico) > 3:
                    if silabico in dic_splitter:
                        dic_splitter[silabico] += 1
                    else:
                        dic_splitter[silabico] = 1
                    silabizado.extend(self._split_silaba(palabra[:i_silaba + self.K.SILABICOS[silabico]], dic_splitter))
                    if i_silaba + self.K.SILABICOS[silabico] < len(palabra):
                        silabizado.extend(self._split_silaba(palabra[i_silaba  + self.K.SILABICOS[silabico]:], dic_splitter))
                    return silabizado
        silabizado.append(palabra)
        return silabizado
    # Funcion que divide un texto en tokens - silabas (lista de n-gramas)
    def text_tokens(self, texto, dic_splitter):
        """Funcion que divide un texto en silabas
        """
        # Lanza funcion recursiva con cada fragmento entre espacios
        silabas = []
        for ttkn, n_grama in self.split_by_type(texto):
            if ttkn != self.K.TTKN_LET:
                silabas.append(n_grama)
                continue
            objetos = self.normalize_n_gram(n_grama)
            if len(objetos) == 1:
                ngrama = objetos[0]
            elif len(objetos) == 2:
                ngrama = objetos[1]
            elif len(objetos) == 3:
                ngrama = objetos[1]
            else:
                ngrama = ""
            silabizado = self._split_silaba(ngrama, dic_splitter)
            if len(silabizado) > 1 and len(silabizado[-1]) == 1 and silabizado[-1] in "bcdfghjklmnñpqrstvwxyz":
                silabizado[-2] += silabizado[-1]
                silabizado.pop()
            # Rellena los tokens de sistema, si los hay
            if len(objetos) > 1:
                silabas.append(objetos[0])
            silabas.extend(silabizado)
            if len(objetos) == 3:
                silabas.append(objetos[2])
        return silabas
