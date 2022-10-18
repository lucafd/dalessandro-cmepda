"""
--- Goal
Write a class to handle a sequence of voltage measurements at different times.

--- Specifications
- the class name must be VoltgeData
- the class must be initialized with two generic iterables of the same length
  holding the numerical values of times and voltages
- alternatively the class can be initialized from a text file
- the class must expose two attributes: 'times' and 'voltages', each returning
  a numpy array of type numpy.float64 of the corresponding quantity.
- the values should be accessible with the familiar square parenthesis syntax:
  the first index must refer to the entry, the second selects time (0) or 
  voltage (1). Slicing must also work.
- calling the len() function on a class instance must return the number of 
  entries
- the class must be iterable: at each iteration, a numpy array of two 
  values (time and voltage) corresponding to an entry in the file must be
  returned
- the print() function must work on class instances. The output must show one
  entry (time and voltage), as well as the entry index, per line.
- the class must also have a debug representation, printing just the values 
  row by row
- the class must be callable, returning an interpolated value of the tension 
  at a given time
- the class must have a plot() method that plots data using matplotlib.
  The plot function must accept an 'ax' argument, so that the user can select
  the axes where the plot is added (with a new figure as default). The user
  must also be able to pass other plot options as usual
- [optional] rewrite the run_tests() function in sandbox/test_voltage_data.py
  as a sequence of proper UnitTests
- [optional] support a third optional column for the voltage errors

In sandbox stanno i files. Controlla i test con test_voltage_data. Ci sono tutte le soluzioni, ma non ha senso farle sbirciando.

TODO ESERCIZIO ALLA FINE: sono gli opzionali alla fine.
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate

class VoltageData:
    """ Class for handling a sequence of voltage measurement taken at different times.
    """
    def __init__(self, times, voltages):
        """ class constructor, times and voltages are iterables of the same length.
        """
        times = np.array(times, dtype=np.float64) # questo salva la fatica di controllare se funziona il costruttore come classe, fa tutto numpy
        # qua prima usavo self.times ma non posso passarglielo così perché non è matrice
        voltages = np.array(voltages, dtype=np.float64)
        # questo funziona anche se hanno la stessa lunghezza! possiamo sistemarlo ora ma c'è un modo più efficiente
        #if len(self.times) != len(self.voltages):
        #    raise ValueError('Times and Voltages must be of the same length!')
        # dovevamo poter inizializzare da file, ma non lo facciamo ora
        self.data = np.column_stack([times, voltages])
        self._spline = interpolate.InterpolatedUnivariateSpline(times, voltages, k=3)
    # se voglio dare un nome alle cose che erano sefinite prima come self.sth uso le properties

    @classmethod
    def from_file(cls, data_path):
        # TODO DA FINIRE

    # errore takes 0 positional argument but 1 was given: vedi se hai messo self
    @property
    def times(self):
        return self.data[:,0]
    
    @property
    def voltages(self):
        return self.data[:, 1]
    
    # per ora il vantaggio è il fatto di avere times e voltages per sapere dove sono senza dovermi dannare l'anima.
    # a un certo punto potrei anche scambiarli e non sarebbe difficile da fare

    # metodo speciale per recuperare elementi con parentesi quadre: getitem
    def __getitem__(self, index):
        # qua vanno gestiti i vari casi in base al tipo di index, è un disastro.
        # il trucco qua è riciclare numpy con la composizione
        return self.data[index]

    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        return iter(self.data) # fatto così perché l'iteratore dovrebbe operare per righe
        # sto riciclando logica già implementata il più possibile
    
    # la funzione print deve lavorare su istanze della classe, quindi voglio implementare la funzione str per bene
    def __str__(self) -> str:
        '''
        output_str = ''
        for i, row in enumerate(self):
            line = f'{i} -> {row[0]:.1f}, {row[1]:.2f}\n'
            output_str += line
        return output_str
        '''
        # altro modo per definirlo 
        header = 'Row -> Time [s], Voltage [mV]'
        return header + '\n'.join([f'{i} -> {row[0]:.1f}, {row[1]:.2f}' \
                                    for i, row in enumerate(self)])
        # join vuole un iterabile!
        # notate che possiamo aggiungere una riga di header
    
    # per fare il debugger, e passare le informazioni
    def __repr__(self) -> str:
        # return str(self.data)
        return '\n'.join([f'{row[0]}, {row[1]}' for row in enumerate(self)])
    
    def __call__(self, t):
        # devo interpolare, usando scipy
        # potrei fare una cosa raffinata tipo creare la spline solo se viene usata call la prima volta, ma è complesso e non vuole farla e la crea subito.
        return self._spline(t)
    
    def plot(self, ax=None, draw_spline=False, **plot_opts): # invece di chiamarlo kwargs, lo chiamo plot opts, solo per chiarire all'utente cosa deve passare
        if ax is None:
            plt.figure('voltage_vs_time')
        else:
            plt.sca(ax)
        plt.plot(self.times, self.voltages, label='data', **plot_opts)
        # attenzione, argomento posizionale non sono kwargs, ma sono cose senza nome. qua posso passare cose kwargs con il nome tipo color='k'
        if draw_spline:
            x = np.linspace(min(self.times), max(self.times), 100)
            plt.plot(x, self(x), label='spline', linestyle='-')
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [mV]')
        # se vogliamo possiamo restituire la figura, ma non sembra importante.



if __name__ == '__main__':
    """
    """
    t, v = np.loadtxt('./sample_data_file.txt', unpack=True)
    vdata = VoltageData(t,v)
    print(vdata.times, vdata.voltages)
    assert vdata[5, 0] == 0.6
    assert vdata[3, 1] == 0.77
    print(vdata[2:10, 0]) # check the slicing
    # lo slicing di un array di numpy restituisce un array di numpy
    # quindi mi aspetterei che esca un voltagedata se faccio lo slicing voltagedata. Vorrei che il risultato sia dello stesso tipo.
    # però è complesso perché vanno gestite le eccezioni... se slicing, vorrei restituisse cose della stessa classe e non diversa
    print(len(vdata))

    for element in vdata:
        print(element)

    vdata.plot(linestyle='', marker='o', color='k')
    plt.show()