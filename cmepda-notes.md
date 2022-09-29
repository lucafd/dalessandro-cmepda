# Appunti di CMEPDA

CONVERTI QUESTO FILE IN LATEX, CONVIENE!

[TOC]

## Basics

### Python

#### lezione 2

"The Zen of Python" sembra una cosa strana però dà l'idea di buone pratiche di programmazione.
Ora fa le convenzioni per scrivere codice ordinato.
[https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)
questo link serve come linea guita ma è tanto dettagliato, anche troppo non ti serve tutto questo.
Sulle slides ci sono anche dei linters, ma vabbè.
Ok, ora ci sono le cose base delle variabili.

**TODO** to be finished.

#### lezione 3 29/09/2022

##### correzione assegnamento

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

##### Algoritmica

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
```pyhton
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