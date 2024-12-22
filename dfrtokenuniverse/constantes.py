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

      self.AUTO_SPLITTERS = {
        "inter": ["in", "ter"],
        "intér": ["in", "tér"],
        "ultra": ["ul", "tra"],
        "anti": ["an", "ti"],
        "auto": ["au", "to"],
        "extra": ["ex", "tra"],
        "multi": ["mul", "ti"],
        "micro": ["mi", "cros"],
        "micro": ["mi", "cro"],
        "macro": ["ma", "cro"],
        "sobre": ["so", "bre"],
      }  
      self.SILABICOS = {
        'contrai': 6, 'contrao': 6,
        'contrau': 6, 'contrai': 6, 'contrahi': 6, 'contrahu': 6,
        'pseudoi': 6, 'pseudoo': 6, 'pseudohi': 6, 'pseudoho': 6,
        'ultrai': 5, 'ultrau': 5, 'ultrahi': 5, 'ultrahu': 5,
        'infrai': 5, 'infrau': 5, 'infrahi': 5, 'infrahu': 5,
        'intrai': 5, 'intrau': 5, 'intrahi': 5, 'intrahu': 5,
        'extrai': 5, 'extrau': 5, 'extrahi': 5, 'extrahu': 5,
        'sobrei': 5, 'sobreu': 5, 'sobrehi': 5, 'sobrehu': 5,
        'suprai': 5, 'suprau': 5, 'suprahi': 5, 'suprahu': 5,
        'parain': 4, 'parahin': 4, 'parau': 4, 'parahi': 4, 'parahu': 4,
        'semiai': 4, 'semiau': 4, 'semiahi': 4, 'semiahu': 4,
        'afroi': 4, 'afroo': 4, 'afrohi': 4, 'afroho': 4,
        'antia': 4, 'antie': 4, 'antii': 4, 'antio': 4, 'antiu': 4,
        'antiha': 4, 'antihe': 4, 'antihi': 4, 'antiho': 4, 'antihu': 4,
        'antei': 4, 'anteu': 4, 'antehi': 4, 'antehu': 4,
        'agroi': 4, 'agroa': 4, 'agroe': 4, 'agroo': 4, 'agrou': 4,
        'hipoa': 4, 'hipoe': 4, 'hipoi': 4, 'hipoo': 4, 'hipou': 4,
        'hipoha': 4, 'hipohe': 4, 'hipohi': 4, 'hipoho': 4, 'hipohu': 4,
        'prei': 3, 'prehi': 3, 'preu': 3, 'prehu': 3,
        'desha': 3, 'deshe': 3, 'deshi': 3, 'desho': 3, 'deshu': 3,
        'deshá': 3, 'deshé': 3, 'deshí': 3, 'deshó': 3, 'deshú': 3,
        'hipn': 3, 'inob': 2, 'inap': 2, 'iner': 2, 'inex': 2, 'inoc': 2, 'inof': 2, 'inop': 2,
        'bst': 2, 'ioi': 2, 'ioe': 2, 'shb':2, 'cht': 2, 'chr': 2, 'chd': 2, 'chf': 2, 'chp': 2,
        'coins': 2, 'cohip': 2,
        'nst': 2, 'rsp': 2, 'stp': 2, 'stm': 2, 'lft': 1, 'stc': 2, 'sts': 2, 'rst': 2,'stg': 2, 'std': 2,
        'ftw': 2, 'nsh': 2, 'nsp': 2, 'nsc': 2, 'nsf': 2, 'nsr': 2, 'nsl': 2, 'nsn': 2, 'nsq': 2, 'nsb': 2,
        'xcr': 1, 'xcl': 1, 'str': 1, 'ntr': 1, 'btr': 1, 'gtr': 1, 'dtr': 1, 'ftr': 1, 'ltr': 1, 'tll': 1,
        'mtr': 1, 'rtr': 1, 'vtr': 1, 'jtr': 1, 'qtr': 1, 'ktr': 1, 'wtr': 1, 'xtr': 1, 'ytr': 1,  'tt': 1,
        'scr': 1, 'ncr': 1, 'zcr': 1, 'ccr': 1, 'pcr': 1, 'bcr': 1, 'gcr': 1, 'fcr': 1, 'lcr': 1, 'xfr': 1,
        'aa': 1,  'ae': 1,  'ao': 1,  'ea': 1,  'ee': 1,  'eo': 1,  'oa': 1,  'oe': 1,  'oo': 1,  'aha': 1, 
        'ahe': 1, 'aho': 1, 'eha': 1, 'ehe': 1, 'eho': 1, 'oha': 1, 'ohe': 1, 'oho': 1, 'aí': 1,  'aú': 1,
        'ii': 1,  'oo': 1,  'rw': 1,  'cg': 1,  'zn': 1,  'zr': 1,  'zv': 1,  'zj': 1,  'cs':1,   'bx': 1,
        'eí': 1,  'eú': 1,  'oí': 1,  'oú': 1,  'ahí': 1, 'ahú': 1, 'ehí': 1, 'ehú': 1, 'ohí': 1, 'ohú': 1, 
        'ía': 1,  'úa': 1,  'íe': 1,  'úe': 1,  'ío': 1,  'úo': 1,  'íha': 1, 'úha': 1, 'íhe': 1, 'úhe': 1, 
        'ího': 1, 'úho': 1, 'nd': 1,  'nt': 1,  'nc': 1,  'mp': 1,  'nk': 1,  'ng': 1,  'nq': 1,  'nr': 1,
        "dh": 1,  'bt': 1,  'sk': 1,  'xn': 1,  'bb': 1,  'dc': 1,  'dg': 1,  'gd': 1,  'dk': 1,
        'nl': 1,  'nb': 1,  'nm': 1,  'nz': 1,  'nñ': 1,  'nh': 1,  'xc': 1,  'rf': 1,  'nv': 1,  'tn': 1,  
        'rj': 1,  'sb': 1,  'kn': 1,  'dm': 1,  'mb': 1,  'mc': 1,  'mp': 1,  'mt': 1,  'md': 1,  'mf': 1,  
        'mg': 1,  'ml': 1,  'ms': 1,  'mz': 1,  'mñ': 1,  'mh': 1,  'lv': 1,  'xt': 1,  'rv': 1,  'bj': 1,
        'zc': 1,  'tm': 1,  'ck': 1,  'bd': 1,  'ld': 1,  'lt': 1,  'lc': 1,  'lp': 1,  'lb': 1,  'nn': 1,
        'lk': 1,  'lg': 1,  'lq': 1,  'lr': 1,  'lm': 1,  'ls': 1,  'lz': 1,  'lñ': 1,  'gn': 1,  'gm': 1,  
        'zg': 1,  'nf': 1,  'pc': 1,  'bv': 1,  'zm': 1,  'sp': 1,  'dl': 1,  'ct': 1,  'cc': 1,  'zl': 1,  
        'sl': 1,  'sp': 1,  'sd': 1,  'sg': 1,  'sm': 1,  'sn': 1,  'sr': 1,  'sq': 1,  'sv': 1,  'sf': 1,  
        'sx': 1,  'nj': 1,  'tb': 1,  'bc': 1,  'xp': 1,  'rd': 1,  'jl': 1,  'rt': 1,  'rc': 1,  'dj': 1,
        'rp': 1,  'rb': 1,  'rn': 1,  'rk': 1,  'rg': 1,  'rq': 1,  'rl': 1,  'rm': 1,  'rz': 1,  'bm': 1,
        'rñ': 1,  'rh': 1,  'lf': 1,  'cn': 1,  'mm': 1,  'pt': 1,  'zt': 1,  'ln': 1,  'np': 1,  'zq': 1,
        'sc': 1,  'xb': 1,  'dv': 1,  'bp': 1,  'cd': 1,  'sj': 1,  'dq': 1,  'xh': 1,  'bg': 1,  'fk': 1,
        '*mn': 1, '*yr': 1, '*yl': 1, '*ym': 1, '*yp': 1, '*yn': 1,  'xg': 1,  'xm': 1, '*yc': 1, '*yd': 1,
        '*yf': 1, '*ys': 1, '*yt': 1, '*yv': 1, '*yw': 1, '*yx': 1, '*yy': 1, '*yz': 1, '*yñ': 1, '*yh': 1,
        '*sy': 1,
        '*nya': 0, '*nye': 0, '*nyo': 0, '*nyi': 0, '*nyu': 0,
        '*ya': 0, '*ye': 0, '*yo': 0, '*yi': 0, '*yu': 0, '*yá': 0, '*yé': 0, '*yó': 0, 
        '*yí': 0, '*yú': 0, '*qu': 0, '*gu': 0, '*ch': 0, '*ll': 0, '*rr': 0, '*ps': 0, '*zz': 0, '*br': 0, 
        '*cr': 0, '*dr': 0, '*fr': 0, '*gr': 0, '*pr': 0, '*tr': 0, '*vr': 0, '*bl': 0, '*cl': 0, '*fl': 0, 
        '*gl': 0, '*kl': 0, '*pl': 0, '*tl': 0, '*vl': 0, '*ba': 0, '*be': 0, '*bi': 0, '*bo': 0, '*bu': 0, 
        '*bá': 0, '*bé': 0, '*bí': 0, '*bó': 0, '*bú': 0, '*bü': 0, '*ca': 0, '*ce': 0, '*ci': 0, '*co': 0, 
        '*cu': 0, '*cá': 0, '*cé': 0, '*cí': 0, '*có': 0, '*cú': 0, '*cü': 0, '*da': 0, '*de': 0, '*di': 0, 
        '*do': 0, '*du': 0, '*dá': 0, '*dé': 0, '*dí': 0, '*dó': 0, '*dú': 0, '*dü': 0, '*fa': 0, '*fe': 0, 
        '*fi': 0, '*fo': 0, '*fu': 0, '*fá': 0, '*fé': 0, '*fí': 0, '*fó': 0, '*fú': 0, '*fü': 0, '*ga': 0, 
        '*ge': 0, '*gi': 0, '*go': 0, '*gu': 0, '*gá': 0, '*gé': 0, '*gí': 0, '*gó': 0, '*gú': 0, '*gü': 0, 
        '*ha': 0, '*he': 0, '*hi': 0, '*ho': 0, '*hu': 0, '*há': 0, '*hé': 0, '*hí': 0, '*hó': 0, '*hú': 0, 
        '*hü': 0, '*ja': 0, '*je': 0, '*ji': 0, '*jo': 0, '*ju': 0, '*já': 0, '*jé': 0, '*jí': 0, '*jó': 0, 
        '*jú': 0, '*jü': 0, '*ka': 0, '*ke': 0, '*ki': 0, '*ko': 0, '*ku': 0, '*ká': 0, '*ké': 0, '*kí': 0, 
        '*kó': 0, '*kú': 0, '*kü': 0, '*la': 0, '*le': 0, '*li': 0, '*lo': 0, '*lu': 0, '*lá': 0, '*lé': 0, 
        '*lí': 0, '*ló': 0, '*lú': 0, '*lü': 0, '*ma': 0, '*me': 0, '*mi': 0, '*mo': 0, '*mu': 0, '*má': 0, 
        '*mé': 0, '*mí': 0, '*mó': 0, '*mú': 0, '*mü': 0, '*na': 0, '*ne': 0, '*ni': 0, '*no': 0, '*nu': 0, 
        '*ná': 0, '*né': 0, '*ní': 0, '*nó': 0, '*nú': 0, '*nü': 0, '*ña': 0, '*ñe': 0, '*ñi': 0, '*ño': 0, 
        '*ñu': 0, '*ñá': 0, '*ñé': 0, '*ñí': 0, '*ñó': 0, '*ñú': 0, '*ñü': 0, '*pa': 0, '*pe': 0, '*pi': 0, 
        '*po': 0, '*pu': 0, '*pá': 0, '*pé': 0, '*pí': 0, '*pó': 0, '*pú': 0, '*pü': 0, '*qa': 0, '*qe': 0, 
        '*qi': 0, '*qo': 0, '*qu': 0, '*qá': 0, '*qé': 0, '*qí': 0, '*qó': 0, '*qú': 0, '*qü': 0, '*ra': 0, 
        '*re': 0, '*ri': 0, '*ro': 0, '*ru': 0, '*rá': 0, '*ré': 0, '*rí': 0, '*ró': 0, '*rú': 0, '*rü': 0, 
        '*sa': 0, '*se': 0, '*si': 0, '*so': 0, '*su': 0, '*sá': 0, '*sé': 0, '*sí': 0, '*só': 0, '*sú': 0, 
        '*sü': 0, '*ta': 0, '*te': 0, '*ti': 0, '*to': 0, '*tu': 0, '*tá': 0, '*té': 0, '*tí': 0, '*tó': 0, 
        '*tú': 0, '*tü': 0, '*va': 0, '*ve': 0, '*vi': 0, '*vo': 0, '*vu': 0, '*vá': 0, '*vé': 0, '*ví': 0, 
        '*vó': 0, '*vú': 0, '*vü': 0, '*wa': 0, '*we': 0, '*wi': 0, '*wo': 0, '*wu': 0, '*wá': 0, '*wé': 0, 
        '*wí': 0, '*wó': 0, '*wú': 0, '*wü': 0, '*xa': 0, '*xe': 0, '*xi': 0, '*xo': 0, '*xu': 0, '*xá': 0, 
        '*xé': 0, '*xí': 0, '*xó': 0, '*xú': 0, '*xü': 0, '*ya': 0, '*ye': 0, '*yi': 0, '*yo': 0, '*yu': 0, 
        '*yá': 0, '*yé': 0, '*yí': 0, '*yó': 0, '*yú': 0, '*yü': 0, '*za': 0, '*ze': 0, '*zi': 0, '*zo': 0, 
        '*zu': 0, '*zá': 0, '*zé': 0, '*zí': 0, '*zó': 0, '*zú': 0, '*zü': 0, '*sh': 0,
        'reins': 2, 'reimp': 2, 'croin': 3, 'croim': 3, 'brein': 3, 'troin': 3, 'troim': 3,
        'miabs': 2, 'rrou': 3, 'toins': 2, 'ciour': 3,
      }
      # Divisores de silaba teoricos por si no aparecen en los patrones reales
      for consonante in [
          'b','c','d','f','g','h','j','k','l','m','n','ñ','p','q','r','s','t','v','w','x','y','z',
          'ns', 'bs', 'rs', 'st', 'ft',
      ]:
          for vocal in "aeiouáéíóú":
              silabico = "*" + consonante + vocal
              if silabico not in self.SILABICOS:
                self.SILABICOS[silabico] = 1
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