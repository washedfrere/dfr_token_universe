# Modulo de constantes para el tokenizador
class  KDfrNlp:
    def __init__(self):
      # Tipos de token
      self.TTKN_DIG = 0
      self.TTKN_LET = 1
      self.TTKN_SEP = 2
      self.TTKN_SIM = 3
      self.TTKN_ESP = 4
      self.TTKN_UNK = 5
      self.TTKN_SIS = 6
      # Descripcion de los tipos de token
      self.TTKN_DESC = {
         0: "Dígitos",
         1: "Letras",
         2: "Separadores",
         3: "Símbolos",
         4: "Especiales",
         5: "Desconocidos",
         6: "Del Sistema"
      }

      # Atributos de token
      self.ATKN_LAT = 0
      self.ATKN_MIN = 1
      self.ATKN_MAY = 2

      # Diccionario de tipos de token asociados a sus caracteres
      # El orden se ha dispuesto por probabilidad de aparicion en textos castellanos
      self.TIPOS_TKN = {
          self.TTKN_SEP: ' ,.-":;\'/\\\n+_\xa0',
          self.TTKN_LET: 'eaonsirldtcPuCAmpbgvfyóhqíjzáéUERxkñúwüçIOÁÉÍÓÚÜBÇDFGHJKLMNÑQSTVWXYZ',
          self.TTKN_SIM: '|><)(%{}][º&$#?!ª¿¡·@€~¬',
          self.TTKN_DIG: '1029835467',
          self.TTKN_ESP: '\t\b\a\f\r\v'
      }

      # Diccionario de atributos de token asociados a sus caracteres
      self.ATRIBUTOS_TKN = {
          self.ATKN_LAT: ' eao|nsirldtcPu><CAmpbg,vfyó.hqí1jz0á2éUER9xkñ)(835ú-46w7":;%\'{/}\\\n][üº&$#+?_!ªç¿¡·@€~¬\t\xa0',
          self.ATKN_MIN: 'eaonsirldtcumpbgvfyóhqíjzáéxkñúwüç',
          self.ATKN_MAY: 'PCAUERÁOÓWÇIVÑDÉBSÜHXZJÍMYTGQLKÚFN',
      }

      # Diccionario de caracteres asociados a sus tipos de token
      # El orden es importante, ya que esta ordenado por probabilidad de aparicion
      self.CHAR_TTKN = {
          ' ': self.TTKN_SEP, 'e': self.TTKN_LET, 'a': self.TTKN_LET, 'o': self.TTKN_LET, '|': self.TTKN_SIM, 'n': self.TTKN_LET, 's': self.TTKN_LET, 'i': self.TTKN_LET,
          'r': self.TTKN_LET, 'l': self.TTKN_LET, 'd': self.TTKN_LET, 't': self.TTKN_LET, 'c': self.TTKN_LET, 'P': self.TTKN_LET, 'u': self.TTKN_LET, '>': self.TTKN_SIM,
          '<': self.TTKN_SIM, 'C': self.TTKN_LET, 'A': self.TTKN_LET, 'm': self.TTKN_LET, 'p': self.TTKN_LET, 'b': self.TTKN_LET, 'g': self.TTKN_LET, ',': self.TTKN_SEP,
          'v': self.TTKN_LET, 'f': self.TTKN_LET, 'y': self.TTKN_LET, 'ó': self.TTKN_LET, '.': self.TTKN_SEP, 'h': self.TTKN_LET, 'q': self.TTKN_LET, 'í': self.TTKN_LET,
          '1': self.TTKN_DIG, 'j': self.TTKN_LET, 'z': self.TTKN_LET, '0': self.TTKN_DIG, 'á': self.TTKN_LET, '2': self.TTKN_DIG, 'é': self.TTKN_LET, 'U': self.TTKN_LET,
          'E': self.TTKN_LET, 'R': self.TTKN_LET, '9': self.TTKN_DIG, 'x': self.TTKN_LET, 'k': self.TTKN_LET, 'ñ': self.TTKN_LET, ')': self.TTKN_SIM, '(': self.TTKN_SIM,
          '8': self.TTKN_DIG, '3': self.TTKN_DIG, '5': self.TTKN_DIG, 'ú': self.TTKN_LET, '-': self.TTKN_SEP, '4': self.TTKN_DIG, '6': self.TTKN_DIG, 'w': self.TTKN_LET,
          '7': self.TTKN_DIG, '"': self.TTKN_SEP, ':': self.TTKN_SEP, ';': self.TTKN_SEP, '%': self.TTKN_SIM, "'": self.TTKN_SEP, '{': self.TTKN_SIM, '}': self.TTKN_SIM,
          '/': self.TTKN_SEP, '\\': self.TTKN_SEP, '\n': self.TTKN_SEP, ']': self.TTKN_SIM, '[': self.TTKN_SIM, 'ü': self.TTKN_LET, 'º': self.TTKN_SIM, '&': self.TTKN_SIM,
          '$': self.TTKN_SIM, '#': self.TTKN_SIM, '+': self.TTKN_SEP, '?': self.TTKN_SIM, '_': self.TTKN_SEP, '!': self.TTKN_SIM, 'ª': self.TTKN_SIM, 'ç': self.TTKN_LET,
          '¿': self.TTKN_SIM, '¡': self.TTKN_SIM, '·': self.TTKN_SIM, '@': self.TTKN_SIM, '€': self.TTKN_SIM, '~': self.TTKN_SIM, '¬': self.TTKN_SIM, '\t': self.TTKN_ESP,
          '\xa0': self.TTKN_SEP, 'I': self.TTKN_LET, 'O': self.TTKN_LET, 'Á': self.TTKN_LET, 'É': self.TTKN_LET, 'Í': self.TTKN_LET, 'Ó': self.TTKN_LET, 'Ú': self.TTKN_LET,
          'Ü': self.TTKN_LET, 'B': self.TTKN_LET, 'Ç': self.TTKN_LET, 'D': self.TTKN_LET, 'F': self.TTKN_LET, 'G': self.TTKN_LET, 'H': self.TTKN_LET, 'J': self.TTKN_LET,
          'K': self.TTKN_LET, 'L': self.TTKN_LET, 'M': self.TTKN_LET, 'N': self.TTKN_LET, 'Ñ': self.TTKN_LET, 'Q': self.TTKN_LET, 'S': self.TTKN_LET, 'T': self.TTKN_LET,
          'V': self.TTKN_LET, 'W': self.TTKN_LET, 'X': self.TTKN_LET, 'Y': self.TTKN_LET, 'Z': self.TTKN_LET, '\x08': self.TTKN_ESP, '\x07': self.TTKN_ESP, '\x0c': self.TTKN_ESP,
          '\r': self.TTKN_ESP, '\x0b': self.TTKN_ESP
      }

      # Para construir la numeración final se debe tener en cuenta el numero de tokens
      # A fin de que la distribucion numerica real quede significativa para los modelos
      # El estandar basico es:
      # - Los tokens de control siempre permanecen en la primera decena
      # - Los tokens posteriores siempre permanece en un entero tal que el cero
      #    corresponda con la unidad divisible menor
      # Por ejemplo:
      # - si tenemos 5438 tokens, la numeracion sera de 1000 a 6438
      # - si tenemos 23253 tokens, la numeracion sera de 10000 a 33253
      # De esta forma, la numeracion real de los tokens adquiere significancia
      # Se puede hacer aun mejor: numerando los tokens por sus tipos y asignando numeraciones crecientes segun su significancia
      # Por ejemplo:
      # - Tokens del sistema: del 0 al 9
      # - Tokens de control o especiales: del 10 al 16
      # - Tokens de separacion: del 20 en adelante
      # - Tokens de simbolo: del 100 en adelante
      # - Tokens de numero: del 1000 en adelante
      # - Tokens de palabra: del 10000 en adelante

      # Codigos internos de token en formato texto
      self.PAD_TOKEN = "<|PAD|>"
      self.UPPER_TOKEN = "<|UPPER|>"
      self.LOWER_TOKEN = "<|LOWER|>"
      self.CAP_TOKEN = "<|CAP|>"
      self.START_TOKEN = "<|START|>"
      self.CONTINUE_TOKEN = "<|TBC|>"
      self.EOF_TOKEN = "<|EOF|>"
      self.UNKNOWN_TOKEN = "<|UNK|>"

      # Diccionario principal con tokens de sistema
      self.MAIN_TOKEN_DICT = {
          self.PAD_TOKEN: 0,  # Relleno 
          self.UPPER_TOKEN: 1,  # Marca de token siguientes en mayuscula
          self.LOWER_TOKEN: 2,  # Marca de token siguientes en minuscula
          self.CAP_TOKEN: 3, # Marca de primera letra mayuscula en el siguiente token
          self.START_TOKEN: 4,
          self.CONTINUE_TOKEN: 5,  # To Be Continued (partial end)
          self.EOF_TOKEN: 6,  # End Of File (o End Of Data)
          self.UNKNOWN_TOKEN: 7,  # Relleno sin nada
          "<|void1|>": 8,
          "<|vaid2|>": 9
      }