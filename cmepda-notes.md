<!-- Appunti di CMEPDA -->

**CONVERTI QUESTO FILE IN LATEX, CONVIENE!**
- [Lezione 02, giovedì 23/09/2022 - Python Basics](#lezione-02-giovedì-23092022---python-basics)
- [Lezione 03, giovedì 29/09/2022](#lezione-03-giovedì-29092022)
  - [Correzione assegnamento](#correzione-assegnamento)
  - [Algoritmica](#algoritmica)
- [Lezione 04, lunedì 3/10/2022](#lezione-04-lunedì-3102022)
- [Lezione 05, giovedì 6/10/2022](#lezione-05-giovedì-6102022)
    - [Array](#array)
    - [Funzioni](#funzioni)
- [Lezione 07, lunedì 10/10/2022](#lezione-07-lunedì-10102022)
  - [Testing and Documenting](#testing-and-documenting)
    - [Testing](#testing)
    - [Documenting](#documenting)
  - [Numpy and SciPy](#numpy-and-scipy)
    - [Maschere](#maschere)
- [Lezione 08 e laboratorio, giovedì 13/10/2022](#lezione-08-e-laboratorio-giovedì-13102022)
  - [Assegnamento 2](#assegnamento-2)
  - [Errori ed altro](#errori-ed-altro)
- [Lezione 09, lunedì 17/10/2022](#lezione-09-lunedì-17102022)
  - [Iteratori](#iteratori)
  - [Generators](#generators)
  - [Lambda functions](#lambda-functions)

# Lezione 02, giovedì 23/09/2022 - Python Basics

"The Zen of Python" sembra una cosa strana però dà l'idea di buone pratiche di programmazione.
Ora fa le convenzioni per scrivere codice ordinato.
[https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/):
questo link serve come linea guita ma è tanto dettagliato, anche troppo non ti serve tutto questo.
Sulle slides ci sono anche dei linters, ma vabbè.
Ok, ora ci sono le cose base delle variabili.

**TODO** to be finished.

# Lezione 03, giovedì 29/09/2022

## Correzione assegnamento

Un file `.py` lo chiamo modulo. Con i moduli ci posso fare cose: eseguirli o importarli in un altro modulo.
Serve per distinguere se file invocato dall'interprete o se invocato da un altro modulo. Viene fatto con la variabile speciale che si chiama `'__main__'`. 
Si chiama "main" se eseguiamo a top level, ma ha un nome diverso se lo importiamo.
modo standard per distinguere se eseguiamo o lo importiamo.
Se lo eseguo, entro dentro name e faccio quanto scritto. Altrimenti, ignoro e l'interprete si limita a leggere la parte che c'è sopra.
Se non mettessi 'main' allora avrei problemi di importazioni! Perché lo eseguirebbe tutto e non quello che voglio io.
`parser` serve a leggere tutte le cose che gli passiamo da  CLI. 
Da **PEP8**: sempre spazi ai lati dell'uguale!
`print` mai usarlo, sempre usare il logging.
`pylint` si può runnare su un file e farglielo. Usalo su un codice, è statico.
    - se cancello spazi bianchi in fondo alla riga, e se pusho e faccio diff non lo vedo nemmeno ma fa brutto!
    - su vscode: trim whitespaces and space indentation.
    - psf/black python. Lo trasforma in una cosa compliant con pep8. Sconsigliato se non sai che stai facendo.
    - righe troppo lunghe: massimo 80 caratteri, e mando indietro. Forse ha senso mandarla giù e splittarla in tre linee.
    - alle variabili in genere non si danno i nomi dei caratteri, a meno che tipo sto facendo scatter plot e vabbè lo chiamo x e y; non bellissimo ma vabbè.
    - le funzioni in python restituiscono sempre qualcosa, e se non restituisce sappiamo che la funzione restituirà `None`.
    - redefining built-in dict: l'argomento gli ha dato il nome di una parola riservata, e non ha motivo di farlo
In python, un dizionario posso farlo come `{1:'ciao','test':2}`
altro modo sensato è `dict(LEGGI BENE LA SINTASSI)`
Cerca le "built-in functions" per evitarle.
`snake_case` underscore per spezzare parole diverse. Si lamenta perché è un carattere solo!
```python
def process(file_path):
    """
    here you have to insert the explaination of the function!
    """
```
_fun fact_: matplotlib è scritta in python, numpy in C per la maggiorparte.
nella maggiorparte dei casi, fra i `"""` si trova roba fatta in modo che se fai `--help` riesci ad estrarre la documentazione.
Docstream si chiama, è importante perché la documentazione è estratta dal codice che estraete.
Uso del context manager per aprire un file:
```python
with open(file_path, 'r') as input_file:
    text = input_file.read()
```
perché questo `with` è una parola speciale di python, serve perché all'uscita del blocco con il `with` poi il file è chiuso e non devi pensarci più, e sappiamo che il file è chiuso e tranquillo nel file-system.
Le stringhe hanno `"string".lower()` e evita loop sul dizionario per mettere in lowercase.
Si poteva fare `input_file.read.lower()`
```python
ascii_dict = {chr(i): 0 for i in range(128)}
```
Il dizionario era la struttura dati giusta per risolvere questo assegnamento, e sarebbe stato più inefficiente la sincronizzazione.

## Algoritmica

Che struttura dati devo usare? come rispondo a questa domanda.
Definizione di algoritmo: serie di istruzioni. Deve essere scritta in modo non ambiguo! Usare l'algoritmo giusto modifica anche la scala dei tempi.
Esempio della ricerca, confronto della ricerca binaria con il _brute force_.
Confronto degli ordini di grandezza.
**Complessità**: dice quanto scala il tempo di esecuzione in funzione della dimensione delle cose.
!!! ha messo `list_` perché `list` è una parola riservata e quindi per evitare il clash con il built-in metto un underscore davanti.
Come computarla: conto il numero minimo di istruzioni fondamentali quando eseguo il codice.
Ok però non ha senso solo perché il tempo di esecuzione per i cicli if per esempio dipendono dal linguaggio, dal sistema operativo, quindi il tempo qua non cambia. Comunque ordine di grandezza delle operazioni elementari è un buon modo per stimare il tempo di esecuzione, tanto è indipendente dal portatile questo numero.
!!! Il numero di operazioni fondamentali non è determinato a priori, ma dipende anche dall'input, e di conseguenza anche il _running time_. Perciò esistono i casi di ordini di grandezza di _worst case_, _best case_, _average_.

**Asymptotic notation**: se il numero di istruzioni fondamentali è $N=f(n)$ dove $n$ è la lunghezza dell'input, allora uso la potenza dominante per $f(n)$.
Come si misura? 
    - brute force: implemento l'algoritmo, lo faccio runnare su vari dati di ingresso e plot the running time vs imput size.
    - by analysis, conto le istruzioni, e valuto il meglio, il peggio e il medio.
    - by eye: one loop -> O(n), two sequential loops -> O(n), two nested loops: O(n^2).

Gli ordini che vedremo sono: `log(n)`, `n`, `n*log(n)`, `n^2` (in genere significa che sto facendo qualche pigrizia e potevo risolverlo con meno).
A informatica fanno un intero anno di questo, di capire la complessità di algoritmi.
"The Complexity of Songs" di Donald E. Knuth, che a quanto pare LateX è un side project, mentre O(n) è una sua notazione. Ad esempio, "99-bottles-of-beer.net"

**Strutture dati**: Per le _liste_. Le operazioni ci sonn sulle slides, e sono fra ordine 1 e ordine n. Costo delle operazioni, dipende anche dal linguaggio di programmazione usato. Anche nel manuale del linguaggio lo dice.
Su python hanno indice, positivo che parte da 0 e arriva a (n-1), negativo che parte da "-n" e finisce a "-1". 
In base ai costi dell'operazione, non conviene o conviene usare certe strutture dati: tipo, se usi due liste per una rubrica, non conviene, ma obv esistono usi sensati.
Altra struttura: _hash table_. Funzione che mappa qualsiasi cosa in ingresso con la cosa in uscita, con funzione hash. Ci sono alcune cose da tenere in considerazione tipo conflitti e altro, ma in python sono già ottimizzati i dizionari, perché sostanzialmente tutto è un dizionario in python.
Per la copia? sempre ordine n in qualunque struttura dati
Più è piena una tabella hash, più è facile avere conflitti, quindi devo tenerla vuota. Dove brillano? in inserzione e cancellazione. Per la cancellazione ho o(1), mentre inserzione è o(n). È molto ridotto rispetto alla lista.

**Sorting**: algoritmo più studiato. Libro, The Art of Computer Programming, ancora la bibbia per queste cose, uno dei sei volumi è "searching and sorting".
La maggior parte hanno complessità medie di O(n log(n)). Python usa la funzione `sorted()` che in realtà è `timsort`, dall'autore dell'artimetica di python.
"Quick sort with Hungarian, folk dance". Ci sono tutti i balletti.

**Numpy and Scipy**: librerie utilizzate tantissimo, in genere per analisi dati. Sono importanti per moli grandi di dati.
Costruzione di array multidimensionale.
```python
import numpy as np
np.linspace(1, 10, 5) # 5 passi equispaziati da 1 a 10 
np.geomspace(1, 10, 5) # 5 passi logaritmicamente spaziati da 1 a 10
```
Perché abbiamo bisogno degli array rispetto alle liste? siccome implementato in C, le cose sono implementate in vario modo, ma sono array omogenei. Dentro lo stesso array non possiamo mescolare due tipi diversi, mentre nelle liste non ho cose del genere.
Qual è il vantaggio della limitazione dell'omogeneità?
Perché posso gestire meglio la memoria: se so già quale tipo mi serve, posso metterli contigui in memoria, so quanto spazio devo allocare a priori, in generale è davvero comodo.
Per le liste, `list_a + list_b` concatena le liste, invece se `np.array` somma i numeri come vettori! Perché ha senso per noi fisici.
Questi array non sono molto fatti per aumentare o diminuire la propria dimensione, anzi in generale è efficiente per la gestione della memoria.
Altra cosa fondamentale, **broadcast**. Vuol dire che su questi array posso fare operazioni molto più generali di banale somma. Moltiplicare membro a membro, fare operazioni membro a membro ha senso.
`a.shape` è la dimensione degli array in numpy.
`c = np.linspace(1, 16, 16),reshape((4, 4))` esempio di trasformazioni di array.
La cosa più sorprendente è invece:
```python
a1 = np.array([1, 2])
a2 = np,array([1, 2], [3, 4])
a1 + a2 # somma il primo vettore a tutte le righe
```
Somma sulle regole di broadcast! Però se `a1` avesse lunghezza 3, non lo somma e esce errore: parte di broadcast della documentazione di numpy, ha conseguenze incredibili.
Ogni volta che operiamo su array, l'operazione avviene in C. Numpy è una libreria con funzioni compilate e poi usate in python. C è molto più veloce di python. 
Quindi se sostituisco loop in python con operazione fra array in numpy, è molto più veloce! ma di un fattore costante ma elevato, tipo fattore 100 che cambia molto nel tempo!
```python
import numpy as np
import time
n = 1000000
v1 = [i for i in range(n)]
v2 = [i**2 for i in range(n)]

s = 0
t0 = time.time()
for v1, v2 in zip(v1, v2): # zip serve per iterable array allo stetto tempo
    s += v1 * v2
elapsed_time = time.time()-t0

print(s)
print(elapsed_time)

# se invece vettorizzo

v1 = np.array(v1)
v2 = np.array(v2)


t0 = time.time()
s = (v1 * v2).sum()
elapsed_time = time.time()-t0

print(s)
print(elapsed_time)
```
**Vettorizzazione**: trasformazione da ciclo for a array. Python lento rispetto a compilato, MA. Se manipolo stringhe o cose web, chissene se lento per micro o millisecondi. Se processo moli significative di numeri è sensato!
Se problema è complesso ma si può vettorizzare, la velocità è quella di C! Quindi parsing di file è facile ed ha i vantaggi di python e la velocità di C.

# Lezione 04, lunedì 3/10/2022

Lecture Basics 5 dalle slides della cartella git.

# Lezione 05, giovedì 6/10/2022

Lecture basic 6, dalle slides.
Oggi invece delle slides proviamo a scivere il codice live.
Scorsa volta introdotto che cos'è una classe e problemi specifici.
Noi vogliamo una classe per gestire vettori in 2D, in vita vera c'è numpy ma questo è un esempio didattico.

Operatore costruttore: `init` 

```python
import math

class Vector2d:

    "Class representing a Vector in 2 dimensions.
    "

    def __init__(self, x, y):
        self.x = float(x) 
        self.y = float(y) # necessario per irrobustire il codice e non fare casino
    # ci definiamo un metodo per farci stampare le coordinate e vedere che abbia funzionato
    def print_coordinates(self):
        print(f'Vector2d({self.x:.3f}, {self.y:.3f})')
        # quella che segue è una f string e python sostituisce il valore delle funzioni nella stringa.
        # invece si poteva scriverr
        print('Vector2d(%.3f, %.3f))' % {self.x, self.y})
        # ne esiste un'altra ma non sono riuscito a copiarla
    # qua definisco le funzioni modulo e somma mentre prima avevo solo la definizione di attributi e uso la funzione print che è un po' particolare
    def module(self):
        return math.sqrt(self.x**2+self.y**2)
    
    def add(self, other):
        return Vector2d(self.x + other.x, self.y+other.y)

if __name__ == '__main__':
    v = Vector2d(0., 1.)
    v.print_coordinates()
    print('the module of v is: {v.module():.3f}')
    v2 = Vector2d(1., 0.)
    v3 = v.add(v2)# devo chamare la funzione add su v passando v2 come adder
    v3.print_coordinates()
```

Quello fatto finora funziona ma non è comodo... tipo la funzione add non è una sintassi naturale, e in questa sintassi non c'è simmeetria fra v e v2 nella somma. Non è intuitivo che come funzione non simmetrica ho una simmetrica.
Sia in python che in C++ esiste un modo per fare che gli operatori + e altri funzionano su classi!
Come? metodi speciali con il doppio underscore, metodi magici o Dunder Methods.
esempio? 

```python
def __add__(self, other):
    return Vector2d(self.x + other.x, self.y+other.y)
```

Non è che ogni cosa che scriviamo funziona, ma i medodi magici sono codificati e sostituiscono le operazioni classiche.
Descriviamone un'altro, tipo il modulo
Potrebbe essere più elegante! con che metodo si fa? con `__abs__` che definisce il modulo.
Ultimo, il print non è bellissimo, dato che vorrei `print(v)` scriva qualcosa. Se ora lo faccio, esce una cosa che dice è una classe e dove si trova sulla memoria.
Si può definire un metodo magico che dice come questo oggetto vada convertito in una stringa.
Non è flessibile come l'ho definito io, invece sarebbe meglio se ritornasse la stringa e basta, e poi lo decida il programmatore!
come lo modifichi?

```python
def __str__(self):
    return (f'Vector2d({self.x:.3f}, {self.y:.3f})')
```
quello che fa l'interprete quando trova print è cercare la funzione str, e se non c'è cerca la funzione `__repr__`, che è pensata per il debug:

```python
def __str__(self):
    return (f'({self.x:.3f}, {self.y:.3f})')
def __repr__(self):
    return (f'Vector2d({self.x:.3f}, {self.y:.3f})')
```

tipo di differenza tipico.
Se str non esiste, l'interprete cerca repr. Se non definita repr, questa viene definita di default con la cosa del nome dell'oggetto e dell'allocazione di memoria.

Ad esempio, cosa c'è nel namespace di un oggetto lo fa la funzione `dir`. Se lo si fa da terminale escono tutti i metodi definiti dall'interprete in automatico.
```python
class Empty:
    pass

empty = Empty()
dir(empty)
```
DocString (`__doc__`) è la cosa fra i doppi hyphen, per la documentazione.
La funzione `help` invece dice la docstring, i metodi definiti e altro.
In generale fare subito un buon metodo per stampare più informazioni possibili.
Se uno vuole sostituire il metodo sottrazione, 
```python
def __sub__(self, other):
    return Vector2d(self.x - other.x, self.y-other.y)
```

Possiamo sfruttare il metodo str delle tuple e riciclare nella nostra funzione `__str__`.
Ad esempio:
```python
def __str__(self):
    return str(tuple(self.x, self.y)) # non è necessario scrivere tuple!
```
Molto importante perché così ci si risparmia alcune cose, tipo definizione di oggetti. Potevo definire la funzione multiply come ho fatto con la somma, ma non ci piace.

Le funzioni di moltiplicazione sono diverse e non abeliane! su che elemento agisce? non è detto che siano dello stesso tipo, lui comincia sempre dall'elemento a sinistra.
Se scrivo `v*2` va a cercare il metodo giusto, invece se scrivo `2*v`, va a cercare il metodo `mul` per gli interi! ma non sa cosa fare in quel caso, ed allora per farlo funzionare introduciamo il metodo `rmul`. ! metodo cercato prima nell'elemento a sinistra, e se non c'è viene trovato per elemento a destra. Non fa la divisione perché possiamo cercarcela noi.
```python
def __mul__(self, scalar):
    return Vector2d(scalar * self.x, scalar * self.y)
def __rmul__(self, scalar):
    # Right multiplication - because a * Vector is different from Vector * a
    return self * scalar # We just call __mul__, no code duplication if it is already defined! This is if we want to make it abelian.
```
Se le operazioni sono *in-place* (cioè assegati sulla stessa variabile, cambiata a seguito dell'operazione), nel caso di `add` e `mul` posso usare `iadd` e `imul` e scrivo per gli attributi `self.x += other.x` e idem su `y` (equivalente se `*=`). Questo mi consente di implementare `+=` e `*=` sui vettori creati.
Concettualmente diversa da quell'altra. Stiamo modificando il vettore self, quindi non è la stessa cosa!

```python
def __iadd__(self, other):
    self.x += other.x
    self.y += other.y
    return self
def __imul__(self, other):
    self.x *= other.x
    self.y *= other.y
    return self
```
! ACHTUNG: devi sempre ritornare self, perché se no non so dove riassegnare la modifica fatta, se non lo ritorno ho perso il puntatore alla variabile. Se la funzione non ha un return, la funzione assegna il valore `None` alla variabile. Tutto quello che vedi agisce all'interno della funzione per tutta la classe.

La definizione di questi metodi rispettano il criterio di minima sorpresa: il codice fa la cosa che uno si aspetta, la più ovvia.
Il codice va scritto con nomi che riflettono quello che il codice fa, e ci sono tool che fa sì che quando viene chiamata la funzionalità è intuitivo cosa sto facendo. Buona norma scriverlo in modo che funzioni così.

Tutti i metodi della classe hanno accesso a tutti gli attributi, come anche i metodi.

Garbage collector: libera memoria nel sistema operativo di cose che non servono più.

Ok altri metodi sono invece nel caso dei confronti fra le cose.
Gli operatori definiti in questo caso sono `eq`, `ge`, `lt`, `gt`, `le`. Alcune cose tipo == sono già definite, e penso che faccia di confrontare le locazioni di memoria.

```python
def __eq__(self, other):
    # Implement the ’==’ operator
    return ((self.x, self.y) == (other.x, other.y))
def __ge__(self, other):
    # Implement the ’>=’ operator
    return abs(self) >= abs(other)
def __lt__(self, other):
    # Implement the ’<’ operator
    return abs(self) < abs(other)
```
In effetti, se si nota, l'utente potrebbe passarmi qualunque cosa al posto di x e y, e allora forse per irrobustirlo posso fare il cast del codice. L'ho modificato alla sorgente.
Printarlo bello:
```python
def __repr__(self):
    # We define __repr__ for showing the results nicely
    class_name = type(self).__name__
    return (’{}({}, {})’.format(class_name, self.x, self.y))
```

Un modo per evitare == errori con float, uso il medoto delle tuple, che è quello mostrato nel codice sopra.
Ora gli ordinamenti mostrati sopra sono scelti a caso.
La funzione maggiore sono `g` = greater, `l` = less, e poi `e` = or equal, e infine `t` = than.
Si può definire anche la funzione sort, ma per farla:
```python
# Tho make the following line work we need to implement either __ge__ and __lt__
# or __gt__ and __le__ (we need a complementary pair of operator)
vector_list.sort()
```

Adesso.

**Hashing** dei vettori. Noi ne abbiamo sentito parlare per i dizionari. Noi vogliamo che sia qualcosa di hashabile.
Deve avere qualche caratteristica, tipo:

  - l'oggetto deve essere immutabile, se no cambia il suo valore! ad esempio stringhe o interi sono mutabili, mentre le liste no, ad esempio appendo un numero e simile. Se cambia, la sua hash function non ritorna più la stessa chiave.
  - serve una `__eq__` function per paragonare elementi della stessa classe;
  - ha bisogno di una funzione hash.

Regole per una buona hash sono sulle slides. Il metodo è `__hash__`.

Ok, adesso diciamo al programma che è read only, mettendo invece di `self.x` la funzione `self._x` e diventa privata. Ok posso anche pensare di modificare aggiungendo gli underscore ovunque, ma è non banale. 
Uso allora le properties, cioè

```python
@property # è un decoratore, lo facciamo settimana prossima
def x(self):
    """ Provides read only access to x - since there is no setter"""
    return self._x
@property
def y(self):
    """ Provides read only access to y - since there is no setter"""
    return self._y 
```
Questa cosa vale anche se il valore che ritorno me lo calcolo nella funzione, posso fare cose non per forza definite prima.

Come cambia nelle funzioni di somma?
Se la funzione è read only, abbiamo rotto le cose di somma. Se ci serve per una funzione di hash, dobbiamo rinunciare alla funzione di hash.
Il fatto che esce una property _getter_ ma non esiste una property _setter_ dice all'interprete che non posso usarla. Come la passo?

```python
@x.setter
def x(self, value):
    self._x = float(value)
```

Ok, se ora ho setter, questo fa funzionare iadd. Sembra esserci duplicazione nel costruttore, dove all'inizio ho definito le cose. Allora come lo modifico eliminando tutto? anche nel costruttore ora posso scrivere
```python
def __init__(self, x, y):
    self.x = x
    self.y = y
```
Funziona!
Il vero costruttore si chiama `new`, mentre `init` è un inizializzatore, quindi l'oggetto esiste già, e posso chiamare tutti i metodi e le proprietà.
Ok però se metto il setter non è più read only, quindi non vedo il senso, tanto valeva lasciarla pubblica. Unico guadagno è che potessi convertirlo al float, invece prima lo controllavo solo nel costruttore: quando costruivo doveva essere ragionevole, mentre dopo potevo cambiarlo a qualunque cosa. 
Così invece no.

Noi non vogliamo il setter ora, vogliamo che sia tutto read only.

Che funzioni di hash sono buone? Boh si ricicla quella dei reali di python:
```python
def __hash__(self):
    """ As hash value we provide the logical XOR of the hash of 
    the two coordinates """
    return hash(self.x) ^ hash(self.y)
```

### Array

Perché un array di numpy è meglio di usare le liste? perché non posso definire una classe con liste? Liste non sono pensate per fare operazioni matematiche, sono lente.
Una lista in python è una lista di puntatori, non è garantita la contiguità in memoria, ed ha un impatto sulle performances!
Se ho due array, contigui in memoria, sono tutti un blocco, e il processore recupera da un unico accesso alla ram tutti gli elementi che gli servono e li mette nella cache del processore.
Risparmia il tempo tantissimo, perché accesso dati da cache a processore è molto veloce.
Quindi, salviamo il nostro vettore come array da lib di python. 
Ora uso la composizione, cioè salvo come oggetto di una classe l'oggetto di un'altra classe.
In python, gli array nativi vanno specificati il tipo di dato da salvare.
Siccome in questa classe dobbiamo rappresentare solo numeri reali, questo typecode ce lo possiamo salvare solo come attributo della classe.
Qual è la differenza? 
Gli attributi della classe sono condivisi fra tutte le istanze della classe, non c'è self, e quindi scritto in un posto solo e prima di tutto.

```python
import math
from array import array

class Vector:
    """ Classs representing a multidimensional vector"""
    typecode = ’d’ #We use a class attribute to save the code required for array

    def __init__(self, components):
        self._components = array(self.typecode, components)
        # quando accediamo agli attributi della classe, dobbiamo comunque accedere con self; posso anche scrivere Vector.typecode, però vabbè.

    def __repr__(self):
        """ Calling str() of an array produces a string like
        array(’d’, [1., 2., 3., ...]). We remove everything outside the
        square parenthesis and add our class name at the beginning."""
        components = str(self._components) # prendo la stringa restituita
        components = components[components.find(’[’): -1] # la manipolo per ottenere le cose formattate bene.
        class_name = type(self).__name__
        return ’{}({})’.format(class_name, components)

    def __str__(self):
        return str(tuple(self._components)) # Using str() of tuples as before
        # perché mi piace molto come formattazione semplice.

v = Vector([5., 3., -1, 8.])
print(v)
print(repr(v))

#[Output]
#(5.0, 3.0, -1.0, 8.0)
#Vector([5.0, 3.0, -1.0, 8.0])
```

Vogliamo riciclare il metodo string del mio array di python per stampare. Il risultato non mi piace molto, perché scrive la stringa come nel commento. Allora, piuttosto proviamo a riscriverla meglio come si vede nel codice.

Altra cosa più interessante. Ora, `_components` è privato e quindi non posso scrivere `v._components[0]`, ma vorrei `v[0]`. Esiste un metodo che lo fa da solo, che è 
```python
def __getitem__(self, index):
    return self._components[index]
```
questo è il tipico esempio di composizione, nei metodi della mia classe uso metodi usati dall'altra classe, in questo caso l'array.
Per impostare valore di variabili private:

```python
def __setitem__(self, index, value):
    self._components[index] = value

def __len__(self):
    return len(self._components)
```

Quello non ancora implementato esplicitamente è iterare alla maniera delle liste, cioè vorrei poter scrivere:

```python
for element in v: 
    print(element)
```

invece di 

```python
for i in range(len(v)):
    print(v[i])
```


Ora, funziona già, e perché python è sveglio. In genere per funzionare si deve usare il metodo iter:

```python
def __iter__(self):
    # deve restituire un iteratore, ma lo vedremo
    # per ora che siamo pigri, un array della lib array è iterabile, e quindi ci facciamo restituire l'iteratore della variabile components
    return iter(self._component)
```

che cos'è un iteratore? una cosa che ha un next che definisce le cose. 
In genere non ha senso farlo perché posso sempre riciclare le cose da altre librerie.
Perché funzionava però senza avere definito iter? beh avendo definito getitem e len, chiama in ordine tutti gli elementi dell'array.
Perché vuoi definirlo esplicitamente? perché è meglio essere espliciti che impliciti. Vuoi che iterazione sia una cosa per cui la classe è pensata.
Comoda l'iterazione perché così ogni volta che python si aspetta un iterabile possiamo mettere il nostro vettore! Moltissime volte funzioni accettano iterabili. Significa posso creare un vettore da un altro vettore per esempio perché accetta iterabili.
Ad esempio se uso la funzione `zip` di python, che mi dà un elemento da ciascun iterabile alla volta (si ferma appena finisce l'iterabile più corto)

```python
for element1, element2 in zip(v1, v2):
    print(element1, element2)
```

Concetto che si chiama _duck typing_. Non importa cosa sia un oggetto, ma importa cosa l'oggetto sa fare!

> If it looks like a duck and quacks like a duck, it must be a duck.

Purché implementino il metodo giusto, il codice funziona! non importa il nome della funzione basta che l'interfaccia ci sia. Ovviamente, anche la segnatura fa parte dell'interfaccia. Tutto quello che implementa il metodo iter, lo posso passare alle funzioni di python che si aspetta un iterabile, non importa il tipo ma solo l'interfaccia. Si chiama polimorfismo, è un concetto generale.
In linguaggi fortemente tipizzati tipo c++ non si può fare il polimorfismo, mentre in python sì. Se linguaggio tipizzato, non si può. In python invece ci interessa solo se iterabile.
In c++ il polimorfismo si fa con classi base che definiscono il concetto comune e da queste si fanno derivare le classi figlie.
**Sulle slides pagina 24 ci sono le funzioni che accettano un elemento iterabile come input**.

Una molto comoda, tutte le permutazioni due a due delle coppie, ma esiste già nella libreria `itertools`.

Un esempio di come far funzionare la classe con iterabilità

```python
def __add__(self, other):
    Vector([x+y for x, y in zip(self, other)])
    # questo metodo per la creazione delle liste, crea una lista con la somma elemento per elemento dei due array.
```

Concetto identico per altre funzioni.
```python
def __abs__(self):
    return math.hypot(*self._components)
    # la cosa interessante era la funzone hypot, che faceva il modulo se vuoi
```

### Funzioni
Le **funzioni** sono classi, ognuna è un oggetto della classe function. Anche gli oggetti delle nostre classi possono comportarsi come funzioni... vogliamo fare sì che l'oggetto sia chiamabile da un metodo `__call__`. Vorrei qualcosa chiamabile con le tonde, e passare quella al fit. Nel corpo della classe posso fare cose più facili.
Altra cosa che si può fare, un esempio è una funzione che conta il numero di chiamate.
Come lo faccio? Creo un wrapper, aggiungo un layer di funzionalità intermedie.
Un oggetto che prende come attributo una funzione.
Per accettare tutti gli argomenti, `__call__(self, *args, **kwargs)`, dove i primi sono argomenti con il nome e il secondo argomenti senza nome.
gli passo la funzione wrappata e curvefit, se gli arriva un chiamabile, non si la menta.
Attenzione, curvefit va a vedere la lista degli argomenti per capire quanti ne deve fittare, a meno che gli passo p0 con 2 elementi. Quindi dobbiamo passargli per forza p0.

# Lezione 07, lunedì 10/10/2022

## Testing and Documenting

### Testing

Non c'è modo di sapere che sia sempre corretto il programma, e quindi per sua natura sarà non corretto o ci sarà un caso in cui si rompe.
Quali sonon le tecniche per sapere all'incirca che il nostro programma sta facendo la cosa giusta?
Molto difficile per un linguaggio interpretato come python. Se compilato certe verifiche le fa il compilatore, mentre se interpretato non lo sa nessuno a priori.
Due attività:
    - analisi statica della sintassi, analisi del codice e di verifiche della sintassi. **Pylint**, usalo!
    - *unit testing*, test dell'unità. Isolare funzionalità il più possibile elementari, e verificare che quel pezzettino faccia la cosa giusta. Piccolo test, verificato in una cosa relativamente piccola ed ho una metrica che lo controlla. L'esempio non è per dire che in ogni caso fa la cosa giusta, ma vanno isolati i casi interessanti. Spezzo il codice in parti elementari. Le funzioni più sono piccole e focalizzate più sono fatte meglio. Va realizzato con una scelta oculata di funzioni e classi.

**variabili d'ambiente**: sono la chiave per il funzionamento del sistema operativo. Su internet si trova. Scrivere un backslash in modo che sia un backslash davvero? `\\`.

**Encoding**: modo di codificare i caratteri del sistema. Corrispondenza fra un glifo e un numero binario/esadecimale. Windows in automatico usa Latin1, non UTF-8. Errori di Unicode: codificare un file con un codice diverso da quello con cui è stato scritto.

**TODO**: a casa leggi il questionario e cercati le cose che non sai e imparale.

`assert`, è una parola riservata, valuta un espressione, se è vera non fa nulla, se è falsa genera un `AssertingError`. In generale non va usato mai l'assert, perché in caso di errore non posso modificarlo in corsa. Sensata solo quando si è certi del risultato e usato nel debugging.

Per i test però non ha senso fare tanti piccoli test manuali, voglio trovare un modo generalissimo di farlo. All'aumentare della complessità del programma, capita che fai un cambiamento e questo cambiamento distrugge altre parti che interagiscono con il programma se fatto male.
Se cresce organicamente con una serie di unit tests, riesce a crescere bene e senza rompersi.
Una funzione deve incapsulare una funzione semplice e ben definita. Unit testing è assicurarsi che ogni pezzo faccia quello che deve fare.
Un paradigma particolare è il Test-Driven Development (TDD): prima di scrivere la funzione scrivo il test, poi scrivo il corpo vuoto della funzione, e alla fine implemento la funzione fino a quando il test non passa. Verifica sempre che si può fare prima il test!
Una cosa da convincere è che il test e la documentazione vanno fatti fin dall'inizio.
Forzarsi a scrivere la documentazione e il test.

Nell'esempio naïve delle slides, va sistemata la tipizzazione e i controlli su quello che viene passato. Vanno pensati i test per tutti i casi in cui viene usata.
Io non voglio fare nulla a mano però, completamente inutile. Voglio allora usare qualche framework per gli unittest, in particolare `unittest`, oppure `pytest`. Oggi tutti usano la seconda ma non è detto si a più efficace.
Test sono fatti in modo da poter runnare automaticamente. Nei test deve essere chiaro cosa voglio testare, e deve essere chiaro cosa voglio ottenere:

```python
import unittest

def square(x):
    """Function returning the suare of x.
    In real life this would be in a differnt module!
    """
    return x**2.

class TestSquare(unittest.TestCase):

    def test(self):
    """Dumb unit test---make sure that the square of 2. is 4.
    """
    self.assertAlmostEqual(square(2.), 4.) # usato almost equal per il discorso di float.

if __name__ == ’__main__’:
    unittest.main()
```

Se guardo un repo, ci sono due cartelle, test e docs. Ci sonon un certo numero di test. Il repo di esempio di github è `ixpeobssim` su github da lucabaldini.
Tipicamente uno di questi test non leggi mai l'output. Ma passa da solo. Non devo essere io che la triggero. A me interessa solo quando fallisce, ed è il concetto di continuous integration, ed è il concetto di _Action_ su github.

**TODO**: attaccare il repo ad un CI/CD.

Poi fa pylint.

Static typing/annotations, posso annotare le funzioni in modo che sappia che sono di un certo tipo. Però è per la leggibilità del codice, è solo annotazione.

```python
def square(x):
    """Return the square of a number, but without annotations
    """
    return x**2.
def annotated_square(x: float) -> float:
    """Return the square of a number; this is the structure of an annotation.
    It just increases legibility.
    """
    return x**2.
```

### Documenting

Le pagine di documentazione non sono fatte a mano. Basta vedere il link al codice sorgente della funzione. 
Va notato che nella documentazione c'è il commento nella docstring.
Documentazione vive dentro il codice, e il meccanismo di documentazione sono le docstrings, fra apici tripli.
Non sono un posto dove le cose sono fatte a caso, ma permette a un tool automatico (sphynx) di generare automaticamente la documentazione.
Quali argomenti prende in ingresso, cosa fa, qualunque cosa in cui dobbiamo stare attenti.
How to use sphynx, learn it. `readthedocs` è open source.
Fare il tag di una nuova versione?
Automatizzare le cose, o lo sono automatiche o non succedono.
Per il progetto finale ce lo si aspetta.

## Numpy and SciPy

Introdotto il concetto di applicabilità all'array elemento per elemento, e il concetto di broadcasting, cioè fra array di dimensioni opportune posso eseguire operazioni artmetiche.
`np.full((2,4), 3.)` fa una matrice 2x4 piena di soli tre.
In generale le operazioni le fa elemento per elemento, anche il prodotto. Però devono avere la stesssa dimensione.
Se hanno la stessa lunghezza, è ovvio moltiplicarlo, se con lunghezze diverse non è banale cosa significa.
Se usi broadcasting e ci si ragiona bene, fattore 100 sulla velocità.
`dir(object)` fornisce tutte le operazioni definite su quell'oggetto.

Quali sono le regole del broadcasting? Sulla documentazione di Scipy. Sono complesse.

### Maschere

Supponiamo che vogliamo vedere dove convertono i fotoni nel silicio, la lunghezza di assorbimento.

```python
import random
import time
import numpy as np
import matplotlib.pyplot as plt

N = 1000000 # numero di fotoni
THICKNESS = 0.200 # mm, spessore del materiale del fotorilevatore

lambda_ = 0.100 # mm, e lambda in realtà è riservata e quindi uso l'underscore per poter usare quel nome

num_absorbed = 0.
abs_z = []

t0 = time.time()
# abbiamo notato l'errore dalla fisica e notiamo cosa fa expovariate, quindi vuole 1/lambda e non lambda
for i in range(N):
    z = random.expovariate(1. / lambda_)
    if z < THICKNESS:
        num_assorbed += 1
        abs_z.append(z)
elapsed_time = time.time() - t0
print(f'Running time: {elapsed_time}')

quantum_efficiency = num_absorbed / N
print(f'Quantum efficiency: {quantum_efficiency}')
# me la aspetto circa 1-e^-2, quindi circa 90%, non così poca.

plt.hist(abs_z, bins=100)
plt.yscale('log')
plt.show()
```
Questo programma lavora linearmente con N, quindi non è banale il fatto che voglia risparmiare di tempo... 
Vettorizzare significa eliminare cicli for e sostituirlo con operazioni fra vettori. Quando possibile, questo fa la differenza come tempistiche.

```python
import random
import time
import numpy as np
import matplotlib.pyplot as plt

N = 1000000 # numero di fotoni
THICKNESS = 0.200 # mm, spessore del materiale del fotorilevatore

lambda_ = 0.100 # mm, e lambda in realtà è riservata e quindi uso l'underscore per poter usare quel nome
def eff_simple():
    abs_z = []
    t0 = time.time()
    for i in range(N):
        z = random.expovariate(1. / lambda_)
        if z < THICKNESS:
            num_assorbed += 1
            abs_z.append(z)
    elapsed_time = time.time() - t0
    print(f'Running time: {elapsed_time}')
    return abs_z

# ora vettorizziamo la funzione. Notiamo che numpy genera random in array, la numpy random.exponential
def eff_vectorized(num_events):
    # invece di generare un loop for, le genero tutte assieme, ma avviene in C e non in python che è lento.
    abs_z = np.random.exponential(lambda_, size=num_events)
    print(abs_z, len(z)) # questo solo di test per vedere che funziona.
    # questa si chiama maschera
    abs_z = abs_z[abs_z <= THICKNESS]
    elapsed_time = time.time() - t0
    print(f'Running time: {elapsed_time}')
    return abs_z

z = eff_simple(N)
quantum_efficiency = len(z) / N
print(f'Quantum efficiency: {quantum_efficiency}')
# me la aspetto circa 1-e^-2, quindi circa 90%, non così poca.
z = eff_vectorized(N)
quantum_efficiency = len(z) / N
print(f'Quantum efficiency: {quantum_efficiency}')
#
#plt.hist(abs_z, bins=100)
#plt.yscale('log')
#plt.show()
```
Lo slicing invece cos'è? e Indexing, cioè come si fa in Numpy a prendere sottoinsiemi di array. Comunque sulle slides c'è.

Prima di tutto che cos'è una maschera? 
```python
import numpy as np

a = np.random.uniform(size=10)
mask = a > 0.5
```
In questo esempio, il nuovo array mask creato è un array con soli true e false, un array di booleani dove è scritto in ogni cella se è vera o falsa la condizione scritta.
ma posso anche fare
```python
a[mask]
```
e questo, passando una maschera con parentesi quadre, restituisce un array in cui gli elementi presenti corrispondono ai true della maschera.

Comunque si vede dal codice che è un risparmio notevole. Nella vita si fa questo, vettorizzo problemi che non si sanno fare altrimenti.
Per esempio se su un immagine ho cose sensate. In generale siamo abituati ai loop, ma non è efficiente.
Esempio di qualcosa di difficile da vettorizzare, nel mondo della fisica delle particelle.
Se faccio assorbire un fotone nel silicio di 5 keV, se 3.6, sono circa 1500 in media di coppie generate. Qual è la varianza su questo? Non è una poissoniana, perché c'è un fenomeno che non conosco. 
Siccome il numero non è fisso, questa è una cosa difficile da vettorizzare.

Libreria importante è pandas, che può fare comodo.
In generale leggere e scrivere file excel con python lo si fa con pandas.
```python
import pandas as pd
```

assignment basic 4

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate import InterpolatedUnivariateSpline

class ProbabilityDensityFunction(InterpolatedUnivariateSpline):
    # in teoria potrei anche commentare tutto e fare pass, perché in pratica sto rinominando la funzione con il programma base.
    def __init__(self, x, y):
        """ Construct
        """
        super().__init__(x, y)

if __name__ == '__main__':
    x = np.linspace(0., np.pi, 20)
    y = np.sin(x)
    f = ProbabilityDensityFunction(x, y)

    print(f.integral(0., np.pi) # le spline hanno il metodo integral, e così posso normalizzare

    plt.plot(x, y, 'o')
    _x = np.linspace(0., np.pi, 200)
    plt.plot(_x, f(_x))

# parte da griglia, e interpola da griglia una funzione.
```

Come si fa a generare un numero random? Primo metodo, hit or miss, e quindi da random uniforme creo coppie di punti e se y è sotto f(x) accetto x o meno.

Altrimenti, uso la funzione cumulativa e la ppf (percent-point function). La cumulativa mappa il punto nel quantile, se ruoto invece di 90 gradi, la nuova funzione mappa il quantile nel suo valore.
E se si prende un array random fra 0 e 1 e gli applico la ppf, avremo un array generato come la funzione di densità di probabilità. Si chiama inverse transform. L'abbiamo fatto a Analisi Statistica dei Dati. Esponenziale è un caso in cui la ppf si può generare analiticamente.
**TODO**: capire cos'è una spline. una funzione interpolatrice. Queste funzioni sono facilmente integrabili e derivabili. Facilmente normalizzabili, la cdf è gratis per l'integrale, e allora per generare numeri random vanno generati fra 0 e 1, ci applico la ppf e ho finito.

`splrand` sembra esserci più o meno un'implementazione davvero funzionante.

Questo è complesso come assegnamento. Prendere come ispirazione.

# Lezione 08 e laboratorio, giovedì 13/10/2022

## Assegnamento 2

Generare numeri random in due modi diversi, una con le spline functions, una per generare con l'inverso della fourier transform.
Ora guardo la funzione da pdf.py e voglio vedere come calcolare la cdf. Fa vedere che sto applicando gli argomenti giusti e calcolo correttamente la cdf. 
Unica cosa, non è detto che la lista che passo sia ordinata, quindi forse andrebbe specificato nella documentazione.
La cdf non è difficile da calcolare, invertirla è un casino, è il calcolo della ppf.
Se ho zone in cui prob è zero, allora ho problemi: la cdf sarà costante e allora nella spline gli passo valori tutti uguali, e per la spline è un casino.
Come filtro un array?

```python
a = np.array([1., 2., 2., 3., 4., 4.])
np.unique(a)
# questo ritorna solo i valori unici della y, 
np.unique(a, return_index = True)
```

Concettualmente, il debugging che faccio a mano sul codice ha senso farlo nell'unittest.
Linea 69 del test, noti che se plotti con più punti, le discontinuità si fanno vedere! la spline non converge benissimo, perché di ordine 3...
Se invece di farla di ordine tre la faccio di ordine 1, interpoli, è molto più bello
In generale le funzioni discontinue vanno trattate in modo diverso... 
Negli strumenti che costruiscono gli astronomi, hanno i bordi perché sono oltre il k_edge degli specchi in astronomia.

La normalizzazione va fatta a mano? cioè va fatta automaticamente.
fra la def di init e super(). Va rifatto a manina.

```python
norm = InterpolatedUnivariateSpline(x, y, k=k).integral(x[0], x[-1])
y /= norm
```

**TODO** vedi a casa come si fa a vedere se l'array è ordinato.

## Errori ed altro

`Traceback` e il tipo di errore.
Qua dice esattamente qual è il problema! Al contrario di git.
`lecture_advanced_2`
In C si ritorna codici di errore numerici, 0 tutto ok, numero diverso non ok.
In Python si usa altro, il meccanismo delle eccezioni (exceptions).
Nelle slides pagina tre c'è perché ha senso usare eccezioni e non flags.

```python
iterable_array[:5] # è lo slicing dell'array dalla posizione in 5 in poi
```

Se guardo la funzione `cut_before` implementata a pagina 4, noto che dà un errore molto chiaro.
In python la filosofia di base è evitare di inventare. Ha senso. In generale posso inventarmi molte cose, molti modi di maneggiare, però fagli sputare l'errore direi che è la cosa migliore! Se la sottostringa non c'è, io gli ritorno il value error e lo sa che non sta passando.
Come intercetto però un errore e gli dico che voglio fare qualcosa di specifico?
Eccezioni.
Cosa sono? È un oggetto, che eredita da una classe di oggetti.
È `raised` quando lo segnalo che è andato male.
Posso intercettare (`caught`) l'eccezione, e posso dire che con il meccanismo di TryExcept:

```python
def cut_before(input_string, substring):
    try:
        result = input_string[:(input_string.index(substring))]
        print(’This line is not executed if an exception is raised in the try block’)
        return result
    # Catch the correct exception type with ’except’
    except ValueError:
        print(’This line is executed only if a ValueError is raised in the try block’)
```

Se non si sollevano eccezioni, siamo nel primo branch, se invece incontro un eccezione, andiamo nel branch except corrispondente. 
Nota che l'except può essere eseguito in base al tipo di errore!
Qual è la logica? Non crasha!! E continuo a fare cose se so che tipo di errore esce sempre.
Si possono intercettare, e posso
Ok, `except:` si può fare ma preferirei non farlo e specifico il tipo di errore.
Tipico errore, try except KeyError, in generale dobbiamo intercettare l'errore nel modo più specifico possibile.
Cioè, un conto è se manca la chiave, un conto è se manca tutto il dizionario!
`else` e `finally` sono altri statement da usare.
Se le cose fossero solo così, non sono molto meglio. Però in generale il trick è che l'errore manda indietro tutto l'oggetto, l'_eccezione_, e quindi passo tutte le informazioni che servono a ricostruire l'errore del file.
Molto generale, in cui ci sono gerarchie di eccezioni molto ricche che consentono di fare la gestione degli errori.
Pagina 10 c'è la gestione degli errori.
`with`. Se lo facciamo in modo brutale, solo con open, lascia le cose incasinate, ma posso usare with che è più sicuro.

```python
try:
    with open (’i_do_not_exist.txt’) as lab_data_file:
        """ Do some process here...
        """
        pass

except FileNotFoundError as e: # we assign a name to the the exception, e la passiamo e maneggiamo come un oggetto!!
    print(e)

# We can be less specific by catching a parent exception
except OSError as e: # OSError is a parent class of FileNotFoundError
    print(e)

# catching Exception will catch almost everything!
except Exception as e:
    print(e)
```

Generalmente, non dovremmo mai chiamare `Exception` perché è troppo generale.
Even worse, you should never catch for BaseException as that would even prevent the user for from aborting the execution with a KeyboardInterrupt (e.g. Ctrl-C).

Asking permission: prima guardo se c'è il file e poi lo apro. In Python come costo computazionale è il contrario, è più facile provare e otterere l'errore che il contrario! Differenza filosofica grande. In C è il contrario.

fare `if: else:` non conviene!

Esiste il logging, non lo ha guardato.

Possiamo sollevare eccezioni da noi!

Ad esempio pagina 20 delle slides, `raise RuntimeError`
Ricorda, in Python si può fare cose violente, tipo `sys.exit()`. Questa è un opzione, ma va valutata! Se metto l'uscita, non posso intervenire! Se invece uso l'errore, chi usa il codice e lo estende, ha l'opzione di estendere il codice e può intercettare e gestire l'eccezione. Sollevare l'opzione, lascia la scelta all'utente.

Possiamo creare un eccezione in maniera granulare addirittura, con una classe appostita che eredita da `(Exception)`.

Ad esempio, pagina 23 fa la value too large exception.
Dove vanno intercettate le eccezioni il prima possibile!
In generale le eccezioni vanno fatte subito, non mettendo un blocco grossissimo di funzione all'interno di un blocco tryexcept. I blocchi devono essere il più piccoli e specifici possibili.

`split()` per stringa usata per separare cose.

Ha fatto l'esempio di vario codice, e non torna! Bisogna imparare a capire dove cercare gli errori.

Funzione che fa parsing di una singola linea. ! **si può iterare sui file**!

Qua non ho nemmeno gestito l'errore, e vorrei invece sapere nel file quale linea è problematica.

```python
def parse_line(line):
    """ Parse a line of the file and return the values as float"""
    values = line.strip(’\n’).split(’ ’)
    # the following two lines may generate exceptions if they fail!
    time = float(values[0])
    tension = float(values[1])
    return time, tension

with open(’snippets/data/fake_measurements.txt’) as lab_data_file:
    for line in lab_data_file:
        if not line.startswith(’#’): # skip comments
            time, tension = parse_line(line)
            print(time, tension)
```

Qua invece sto prendendo l'errore troppo presto, non passo info interessanti.

```python
def parse_line(line):
    """ Parse a line of the file and return the values as float"""
    values = line.strip(’\n’).split(’ ’)
    try:
        time = float(values[0])
        tension = float(values[1])
    except ValueError as e:
        print(e) # This is not useful - which line of the file has the error?
        return None # We can’t really return something meaningful
    return time, tension

with open(’snippets/data/fake_measurements.txt’) as lab_data_file:
    for line in lab_data_file:
        if not line.startswith(’#’): # skip comments
            time, tension = parse_line(line)
            print(time, tension) # This line still crash badly!
```

In questo caso è quello giusto da fare, così capisco anche la linea.

```python
def parse_line(line):
""" Parse a line of the file and return the values as float"""
    values = line.strip(’\n’).split(’ ’)
    time = float(values[0])
    tension = float(values[1])
    return time, tension

with open(’snippets/data/fake_measurements.txt’) as lab_data_file:
    for line_number, line in enumerate(lab_data_file): # get the line number
        if not line.startswith(’#’): # skip comments
            try:
                time, tension = parse_line(line)
                print(time, tension)
            except ValueError as e:
                print(’Line {} error: {}’.format(line_number, e))
```

Consiglio su cosa va usato. Quantità di codice scritto in Fortran e C è enorme e usati ovunque, quindi c'è valore nel saper programmare in queste cose. Se cominci ora da zero a scrivere qualcosa, scrivilo in C++ o Python, ma saper programmare in Fortran ha un valore solo per il materiale che c'è in giro.
Python puro è lento, ma ci sono molte librerie scritte in linguaggi compilati che consentono di fare cose velocemente. Ci sono cose che come tempo contano 0 e però ha tempo di sviluppo di molto.

```python
from splrand.pdf import ProbabilityDensityFuncion
import numpy as np

x = np.linspace(0., 1., 100)
y = 2. * x
pdf = ProbabilityDensityFunction(x, y)

# ora non chiamo il costruttore, ma un oggetto creato, e che ha un metodo chiamato call
pdf(0.5)
> [Output]: array(1.)
```

Ad esempio, supponiamo di fare una classe, 

```python

class Dummy:

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    d = Dummy('ciao')
    print(d.name)
    print(d(3))
    # che succede? type error, perché non è chiamabile!
```

Questo metodo magico chiamato `__call__` è l'unico che consente di chiamare le cose, se lo aggiungo come 

```python
def __call__(self, value):
    return value * 3.
```

Pagina sul data model di python, fra le varie cose abbiamo le basic customization, metodi magici che mimicano un certo numero di comportamenti dei tipi standard di python.
Chiamare il costruttore della classe è una cosa, che restituisce l'istanza di una classe; a quel punto dipende se l'oggetto ha un metodo per essere chiamato.
Sulla documentazione dice cosa succede per ogni metodo. Se non fai overload, il metodo della classe genitore viene utilizzato.
Quando invece di fare i loop sulle funzioni, tutte fatte nella funzione max di python, basta dire come due oggetti si confrontano, molto più facile da leggere e meno difficile da sbagliare.
Anche il [datamodel](https://docs.python.org/3/reference/datamodel.html) da avere come la bibbia.

# Lezione 09, lunedì 17/10/2022

## Iteratori

Parlato di come si fa a rendere un oggetto iterabile alla python, che fa fare il ciclo for. Come si fa? si usa il metodo magico `__iter__`. Noi l'avevamo fatto riciclando il metodo `iter` della libreria `array`.
Un iteratore ha implementato il metodo `__next__`. In pratica si sa qual'è il prossimo elemento da restituire. Chiamando l'oggetto, vi restituisce quello successivo. Quando è finita l'iterazione, deve sollevare un'eccezione chiamata `StopIteration()`.
Perché devo implementare `iter` che usa `next` e devo implementare next? Perché così posso avere più iteratori attivi sullo stesso tipo di oggetto iterabile.
Motivo per cui un iteratore è tecnicamente un iterabile, ma non il viceversa è sempre vero!
Ora fa un esempio per capire che il ciclo for è equivalente a un ciclo infinito di chiamate fino a quando non esce l'eccezione:

```python
my_list = [1., 2., 3.]

# For-loop syntax
for element in my_list:
    print(element)

# This is equivalent (but much less readible and compact)
list_iterator = iter(my_list)
    while True:
        try:
            print(next(list_iterator))
        except StopIteration:
            break
```

Notiamo che se implementiamo `getitem` e `len` l'interprete si fa da sé l'iteratore.

Il seguente metodo funziona per le liste e non per i dizionari perché non solleva il `KeyError`.

```python
class SimpleIterator:
    """ Class implementing a super naive iterator"""
    def __init__(self, container):
        self._container = container
        self.index = 0
    
    def __next__(self):
        try:
            # Note: here we are calling the __getitem__ method of self._container
            item = self._container[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return item
    def __iter__(self):
        return self

class SimpleIterable:
    """ A very basic iterable """
    def __init__(self, *elements):
        # We use a list to store elements internally.
        # This provide us with the __getitem__ function
        self._elements = list(elements)
    
    def __iter__(self):
        return SimpleIterator(self._elements)
```

Questo è un generatore basico. In generale posso fare iteratori a caso, tipo in `crazy_iterator` lo fa diverso e strano.

Esistono metodi che dato un iterabile ritornano un singolo valore.

Iteratori, sono utili da usare wrappando i container.
Infine, gli iteratori operano su dati esistenti!

## Generators

Qualcosa che ad ogni interazione calcola il prossimo, per risparmiare memoria. Per calcolare qualcosa un attimo prima di usarla e non prima. 
Un minimo di procrastinazione.
Possiamo iterare su elementi che non esistono prima ma vengono calcolati mano mano. 
Ci sono due modi, o con le _generator expressions_, o con le _generator functions_. In realtà nella vita vera le generatrici li dà python, ad esempio `range()` in python3.
Una volta che abbiamo il generatore, possiamo usarlo per il for loop.

```python
for i in range(4): # generators act like iterators in for loop
    print(i)

data = [12, -1, 5]
square_data_generator = (x**2 for x in data) # generator expression!
# qua la differenza rispetto alle [] è che non viene calcolata o creata la lista, ma calcolato tutto solo dentro un loop.
for square_datum in square_data_generator: # again, works like an iterator
    print(square_datum)
```

Siccome la lista nell'esempio di sopra non è calcolata per intero prima, se modifico `data` in corso di loop, anche la generazione segue le modifiche della lista, dato che non è calcolata prima.

la **funzione generatrice** è una funzione che si crea e dopo un po' c'è uno `yield`. Il risultato di quando lo creo è che viene restituito un generatore. 
Il generatore è un oggetto che ha il metodo `next`. Che fa? esegue tutto il codice fino a `yield`, dove ritorna il valore che segue `yield`. Quando finisce solleva `StopIteration`.
Di solito i generatori sono scritti con un loop all'interno.

```python
# Generator function that provides infinte fibonacci numbers
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# We need to impose a stop condition externally to use it
max_n = 7
fib_numbers = []
for i, fib in enumerate(fibonacci()):
    if i >= max_n:
        break
    else:
        fib_numbers.append(fib)
print(fib_numbers)

# Another way of doing that is using ’islice’ from itertools
import itertools
# Generator expression
fib_gen = (fib for fib in itertools.islice(fibonacci(), max_n))
print(list(fib_gen))
```

Qua la funzione `fibonacci()` non restituisce nulla, ma viene creato un oggetto tipo generatore e restituito. Quando poi lo uso, metto una condizione di stop esterna.
Modo elegante è `.islice()` dalla libreria `itertools`. In pratica, crea con un generatore e un massimo, restituisce un iterabile. In generale, comunque, va notato come `fib_gen` non ho calcolato nulla, perché ho le parentesi tonde e non quadre.

Il generatore serve quando voglio generare elementi in maniera lazy.
Le funzioni generatrici di python sono davvero tantissime, la pagina 43 delle slides `lecture_advanced_2` ne elenca alcune e poi fa qualche esempio.

Un metodo carino è il groupby, in generale si usa e c'è anche in pandas.

## Lambda functions

**Anonimous Functions** are a construct typical of functional programming, tipo _Lambda calculus_.
In Python, crea una funzione in corsa senza dargli un nome. Sono limitate a espressioni singole, ritornate all'utente. Molti degli usi tipici della lambda function sono fatte dalle espressioni generatrici e _list comprehension_.

la sintassi è 
```python
multiply = lambda x, y: x * y
```
Questa è una funzione a una riga, e quindi mi serve una funzione al volo e non la devo definire prima.

`map` applica una funzione ad un iterabile.
In generale il loro use case è coperto dal linguaggio normale.
L'uso delle `lambda` è solo quando la funzione dopo è molto breve.

L'esercizio di ricapitolazione finale aveva senso ma non è molto illuminante, dice che preferisce esercitazione, lui che scrive codice.

Ora facciamo assignment advanced 2.
Cosa sono i class methods? Cose usate per costruire istanze della classe che non sono self.
