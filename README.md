# Crawler-GenerazionePrototipi

Progetto tesi di laurea:

Sistema per la raccomandazione di musica basato su logiche descrittive, probabilità e combinazione di prototipi

## Descrizione del contenuto della repository

Questo repository contiene sia gli script Python per ottenere ed elaborare i dati, sia i dati di output che genereremo:
* la cartella “𝑐𝑜𝑐𝑜𝑠” contiene appunto l’intero programma CoCoS, con le modifiche al fine di poter limitare il numero di attributi che CoCoS deve tenere in considerazione per la produzione dell’output;
* la cartella “𝑐𝑜𝑐𝑜𝑠_𝑔𝑒𝑛𝑟𝑒𝑠” contiene i file per la creazione dell’input di CoCoS, ossia ogni genere con le 5 proprietà tipiche selezionate ed eventualmente quelle rigide;
* la cartella “𝑔𝑒𝑛𝑟𝑒𝑠” contiene i file dei generi con l’elenco completo di tutte le proprietà estratte;
* la cartella “𝑝𝑟𝑜𝑡𝑜𝑡𝑖𝑝𝑖” contiene tutti i file di input per CoCoS, e quindi anche il risultato fornito in seguito alla combinazione dei generi;
* la cartella “𝑠𝑜𝑛𝑔𝑠” contiene i file delle canzoni e delle loro proprietà;
* il file “𝑎𝑡𝑡𝑟𝑖𝑏𝑢𝑡𝑒𝑠” contiene l’elenco degli attributi più utilizzati;
* il file “𝑑𝑎𝑡𝑎” è un file di tipo JSON contenente tutti i dati reperiti da AllMusic.

## Guida all'esecuzione

I passi per eseguire tutto il codice sono:

<ol>
<li> eseguire “𝐶𝑟𝑎𝑤𝑙𝑒𝑟. 𝑝𝑦”, non ha bisogno di parametri e genera il file data; </li>
<li> eseguire “𝑝𝑟𝑜𝑡𝑜𝑡𝑦𝑝𝑒𝑟𝐺𝑒𝑛𝑟𝑒. 𝑝𝑦” che riempirà la cartella genres; </li>
<li> eseguire “𝑝𝑟𝑜𝑡𝑜𝑡𝑦𝑝𝑒𝑟𝑆𝑜𝑛𝑔. 𝑝𝑦”, che riempirà la cartella songs grazie a “𝑆𝑜𝑛𝑔. 𝑝𝑦”; </li>
<li> a questo punto bisogna scegliere le proprietà rigide e tipiche, quindi creare dei file della forma seguente e con nome il genere da inserire alla cartella “𝑐𝑜𝑐𝑜𝑠_𝑔𝑒𝑛𝑟𝑒𝑠”:

𝑆𝑖𝑛𝑔 − 𝐴𝑙𝑜𝑛𝑔𝑠 <br>
𝐴𝑚𝑖𝑎𝑏𝑙𝑒/𝐺𝑜𝑜𝑑 − 𝑁𝑎𝑡𝑢𝑟𝑒𝑑

𝐶ℎ𝑖𝑙𝑑𝑟𝑒𝑛′𝑠 𝐹𝑜𝑙𝑘:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0.7857142857142857 <br>
𝐹𝑎𝑚𝑖𝑙𝑦 𝐺𝑎𝑡ℎ𝑒𝑟𝑖𝑛𝑔𝑠:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0.7714285714285715 <br>
𝑊ℎ𝑖𝑚𝑠𝑖𝑐𝑎𝑙:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0.7571428571428571 <br>
𝐿𝑎𝑖𝑑 − 𝐵𝑎𝑐𝑘/𝑀𝑒𝑙𝑙𝑜𝑤:&nbsp;&nbsp;&nbsp;&nbsp; 0.7428571428571429 <br>
𝐸𝑛𝑒𝑟𝑔𝑒𝑡𝑖𝑐:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0.7285714285714286 <br>

(A supporto della decisione delle proprietà rigide può essere utile utilizzare “𝑆𝑢𝑔𝑔𝑒𝑠𝑡𝑖𝑜𝑛. 𝑝𝑦”, che genera il file “𝑎𝑡𝑡𝑟𝑖𝑏𝑢𝑡𝑒𝑠”, con l’elenco di tutti gli attributi più utilizzati);
</li>
<li> eseguire “𝐹𝑖𝑙𝑒𝐹𝑜𝑟𝐶𝑜𝑐𝑜𝑠𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟. 𝑝𝑦”, che si occupa di riempire la cartella prototipi a partire dai file creati nel punto 4, con ogni possibile loro combinazione; </li>
<li> eseguire “𝑒𝑥𝑒𝑐𝑢𝑡𝑜𝑟. 𝑝𝑦”, che si occuperà di eseguire CoCoS per ogni file creato nel punto 5. Questa operazione richiede moltissimo tempo, ma può essere interrotta in qualsiasi momento. </li>
</ol>