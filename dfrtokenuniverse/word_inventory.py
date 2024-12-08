# Modulo para el inventariado y conteo de n-gramas previo a la tokenizacion
from dfrtokenuniverse.constantes import KDfrNlp 
class WordInventory:
    def __init__(self):
        self.K = KDfrNlp()
    def _dict_counter(self, ttkn, objeto, diccionario):
        """Contador sobre diccionario  a dos niveles
        args:
            ttkn: tipo de token (primer nivel)
            objeto: valor a contar (segundo nivel)
            diccionario: diccionario en formato {ttkn: {valor: num}} sobre el que contar cada valor
        """
        if ttkn in diccionario:    
            if objeto in diccionario[ttkn]:
                diccionario[ttkn][objeto] += 1
            else:
                diccionario[ttkn][objeto] = 1
        else:
            diccionario[ttkn] = {objeto: 1}
    def _single_dict_counter(self, objeto, diccionario):
        """Simple contador sobre diccionario para claridad del codigo
        args:
            objeto: valor a contar
            diccionario: diccionario en formato {valor: num} sobre el que contar cada valor
        """
        if objeto in diccionario:
            diccionario[objeto] += 1
        else:
            diccionario[objeto] = 1
    def normalize_and_count(self, ttkn, n_gram, counter_dic):
        """Codificador de n-gramas para usar siempre n-gramas en minuscula
           precedidos de una marca de mayuscula total (UPPER) o solo la primara (CAP)
        args:
            n_gram: enegrama o token a evaluar
            counter_dic: diccionario formato {ttkn: {valor: num}} sobre el que ir contando
        """
        if isinstance(n_gram, str):
            # Es un n-grama
            if n_gram[0] in self.K.TIPOS_TKN[self.K.TTKN_LET]:
                # Es una letra, comprobamos mayusculas
                if n_gram.upper() == n_gram:
                    self._dict_counter(ttkn, n_gram.lower(), counter_dic)
                elif len(n_gram) == 1:
                    self._dict_counter(ttkn, n_gram, counter_dic)
                else:
                    if n_gram[0].upper() == n_gram[0] and n_gram[1:].lower() == n_gram[1:]:
                        self._dict_counter(ttkn, n_gram.lower(), counter_dic)
                    else:
                        self._dict_counter(ttkn, n_gram.lower(), counter_dic)
            else:
                self._dict_counter(ttkn, n_gram, counter_dic)
    def explota_fragmento(self, n_grama, fragmentos_usados, excedentes, fragmentos_evaluados):
        """Funcion recursiva que busca dividir un n-grama con fragmentos evaluados contando en fragmentos usados
        args:
            n_grama: cadena de caracteres
            fragmentos_usados: diccionario sobre el que contar
        """
        cont_excedentes = 1
        cont_sub_excedentes = 0
        for fragmento in fragmentos_evaluados:
            if len(fragmento) > len(n_grama):
                continue
            elif fragmento == n_grama:
                cont_excedentes = 0  # contador a cero
                self._single_dict_counter(fragmento, fragmentos_usados)
            elif fragmento in n_grama:
                cont_excedentes = 0
                self._single_dict_counter(fragmento, fragmentos_usados)
                for x in n_grama.split(fragmento):
                    if x and x > "":
                        cont_sub_excedentes += self.explota_fragmento(x, fragmentos_usados, excedentes, fragmentos_evaluados)
                break
        if cont_excedentes > 0:
            self._single_dict_counter(n_grama, excedentes)
        return cont_excedentes + cont_sub_excedentes