# Modulo que recaba informacion sobre las relaciones entre tokens
from dfrtokenuniverse.constantes import KDfrNlp 
from dfrtokenuniverse.splitter import SplitTextTokens
class TknRel():
    def __init__(self):
        self.version = "2024_12_26_21_52"
        self.K = KDfrNlp()
        self.splitter = SplitTextTokens()
        self.token_id = 1
        self.dic_token_id = { "": 0}
        # Contador de tokens
        self.dic_tokens = {} # {token_id: veces}
        # Para contar relaciones de manera absoluta
        self.dic_rel = {}
        # dic_rel = {
        #   token_id: {
        #     rel_token_id: {
        #       "count": veces,
        #       "dist": acum_distancia
        #     }  # rel_token_id
        #   )  # token_id
        # }  # dic_rel
    def _add_dic(self, id_ini, id_rel, tit_id, frase_ini, frase_rel, distancia):
        pass
    def _counter(self, frases, max_dist=50):
        """Cuenta en los diferentes diccionarios las relaciones entre ngramas
        args:
            tit_id: id del titulo entrante
            frases: lista de listas de ngramas tipo letras
        """
        len_frases = len(frases)
        # Indices de inicio
        i_fa = 0
        i_na = 0
        len_ngramas = len(frases[0])
        # Indices de siguientes
        i_fz = 0
        i_nz = 0
        len_ngramas_rel = len(frases[0])
        # Hasta llegar a la ultima frase
        while i_fa < len_frases:
            # Preparamos para comparar el siguiente token
            distancia = 0
            i_nz = i_na + 1
            if i_nz >= len_ngramas:
                i_nz = 0
                i_fz += 1
                if i_fz < len_frases:
                    len_ngramas_rel = len(frases[i_fz])
            # Hasta el final de las frases o un maximo de max_dist tokens, todos los tokens siguientes
            while i_fz < len_frases and distancia < max_dist:
                distancia += 1
                # Saltamos los tokens iguales
                if frases[i_fa][i_na] == frases[i_fz][i_nz]:
                    i_nz += 1
                    if i_nz >= len_ngramas_rel:
                        i_nz = 0
                        i_fz += 1
                        if i_fz < len_frases:
                            len_ngramas_rel = len(frases[i_fz])
                    continue
                # Contamos token y sumamos longitud
                if frases[i_fa][i_na] in self.dic_rel:
                    if frases[i_fz][i_nz] in self.dic_rel[frases[i_fa][i_na]]:
                        self.dic_rel[frases[i_fa][i_na]][frases[i_fz][i_nz]]["count"] += 1
                        self.dic_rel[frases[i_fa][i_na]][frases[i_fz][i_nz]]["dist"] += distancia
                    else:
                        # Si el token relacionado es nuevo, incluimos en diccionario
                        self.dic_rel[frases[i_fa][i_na]][frases[i_fz][i_nz]] = {
                            "count": 1,
                            "dist": distancia
                        }
                else:
                    # Si el token es nuevo, incluimos en diccionario
                    self.dic_rel[frases[i_fa][i_na]] = {
                        frases[i_fz][i_nz]: {
                            "count": 1,
                            "dist": distancia
                        }
                    }
                # Siguiente token relacionado
                i_nz += 1
                if i_nz >= len_ngramas_rel:
                    i_nz = 0
                    i_fz += 1
                    if i_fz < len_frases:
                        len_ngramas_rel = len(frases[i_fz])
            # Siguiente token origen
            i_na = i_na + 1
            if i_na >= len_ngramas:
                i_na = 0
                i_fa += 1
                if i_fa < len_frases:
                    len_ngramas = len(frases[i_fa])
            # El control del siguiente i_nz se hace antes del while

    def evaluate(self, texto, min_ngramas_by_tit=50):
        """Funcion que evalua la relacion entre tokens en un texto
        args:
            texto: texto a evaluar
            min_ngramas_by_tit: minimo de ngramas para aceptar el texto
        """
        # Dado un texto, que puede tener saltos de linea,
        # se evalua la relacion entre sus tokens
        ngramas = []
        cont_ngramas_texto = 0
        frases = []
        ngramas = []
        # Inventariamos tokens
        for ngrama in self.splitter.one_shot(texto):
            # Controlamos token nuevo
            if ngrama in self.dic_token_id:
                self.dic_tokens[self.dic_token_id[ngrama]] += 1
            else:
                self.dic_tokens[self.token_id] = 1
                self.dic_token_id[ngrama] = self.token_id
                # Nuevo token
                self.token_id += 1
            # Para las relaciones solo usamos palabras
            if ngrama[0] in self.K.CHAR_TTKN and self.K.CHAR_TTKN[ngrama[0]] == self.K.TTKN_LET:
                ngramas.append(self.dic_token_id[ngrama])  # Al proceso de relaciones debe llegar el id, no el ngrama
                cont_ngramas_texto += 1  # Para el control de minimos
            elif "\n" in ngrama:
                if len(ngramas) > 0:
                    frases.append(ngramas)
                    ngramas = []
        # No nos dejamos el ultimo bloque, por favor
        if len(ngramas) > 0:
            frases.append(ngramas)
        # Controlamos un minimo de tokens para procesar titulos y relaciones
        if cont_ngramas_texto >= min_ngramas_by_tit:
            self._counter(frases, max_dist=min_ngramas_by_tit)
