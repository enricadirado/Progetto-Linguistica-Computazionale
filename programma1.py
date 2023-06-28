import sys
import nltk

#funzione che, data la lista delle frasi e il numero di frasi, restituisce la lista dei tokens, il numero di tokens totali e lunghezza media delle frasi
def Tokenizzatore(frasi, lun_frasi):
    tokensTOT=[]
    #per ogni frase nella lista delle frasi
    for frase in frasi:
        #calcolo i tokens della frase
        tokens=nltk.word_tokenize(frase)
        #aggiorno la lista contente i tokens totali del testo
        tokensTOT=tokensTOT+tokens
    #calcolo il numero dei tokens totali del testo
    num_tokensTOT=len(tokensTOT)
    #calcolo la lunghezza media delle frasi come il rapporto tra la somma delle frequenze dei tokens e il numero delle frasi nel testo
    lun_mediaFrasi=num_tokensTOT/lun_frasi
    #arrotondo la lunghezza media a 4 cifre dopo la virgola
    lun_mediaFrasiR=round(lun_mediaFrasi,4)
    return tokensTOT, num_tokensTOT, lun_mediaFrasiR
        

#funzione che, data la lista di tutti i token del testo, restituisce la lunghezza media dei tokens del testo
def CalcoloCaratteriMedia(tokensTOT):
    #inizializzo la lista che conterrà i token che sono segni di punteggiatura e la lista contenete tutti i token che non sono segni di punteggiatura 
    t_punt=[]
    t_nonpunt=[]
    #inizializzo variabile che conterrà i caratteri totali
    num_carTOT=0
    #lista che contiene i segni di punteggiatura possibili
    punteggiatura=[',',';','.','...',':','-','--','_','[',']','+','*','^','?','=',')','(','/','&','"','!',"'",'|','<','>']
    #per ogni token nella lista dei tokens totali
    for tok in tokensTOT:
        #se il token è nella lista della punteggiatura, aggiungo il token alla lista dei token che sono segni di punteggiatura
        if tok in punteggiatura:
            t_punt.append(tok)
        else:
            #altrimenti, aggiungo il token alla lista dei token che non sono segni di punteggiatura
            t_nonpunt.append(tok)
            #calcolo il numero di caratteri del token
            num_car=len(tok)
            #aggiorno la lista che contiene i caratteri totali del testo
            num_carTOT=num_carTOT+num_car

    #calcolo la lunghezza media dei tokens come il rapporto tra il numero di caratteri totali del testo e la somma tra il numero di elementi nella lista dei token che sono segni di punteggiatura e il numero di elementi della lista di token che non sono segni di punteggiatura
    lun_mediaTokens=num_carTOT/(len(t_punt)+len(t_nonpunt))
    #arrotongo la lunghezza media dei tokens a 4 cifre dopo la virgola
    lun_mediaTokensR=round(lun_mediaTokens, 4)
    return lun_mediaTokensR


#grandezza del vocabolario: numero di token che compone vocabolario
#ricchezza lessicale (ttr): voc/c
#in questo caso calcolo la ttr con vocabolario e corpus delle porzioni

#funzione che data la lista dei tokens del primo corpus e la lista dei tokens del secondo corpus, per ogni corpus stampa la porzione incrementale di corpus analizzata, il nome del corpus analizzato, la grandezza del suo vocabolario e la sua Type Token Ratio
def AndamentoCrescita500(tokensTOT1, tokensTOT2):
    #nome dei due corpus
    nome1="'A Vindication of the Rights of Woman'"
    nome2='Ted Talks'
    #inizializzo le variabili che conterranno il numero di parole tipo del vocabolario (grandezza del vocabolario)
    num_voc1=0
    num_voc2=0
    #inizializzo le variabili che conterranno l'indice di ricchezza lessicale (Type Token Ratio)
    ttr1=0.0
    ttr2=0.0
    #inizializzo il contatore del ciclo while a 0
    i=0
    #inizializzo una variabile n che segnala il numero di parole tipo per porzione da analizzare
    n=500
    #calcolo il numero dei tokens totali del corpus
    x1=len(tokensTOT1)
    x2=len(tokensTOT2)

    #se il corpus 1 è più grande del corpus 2, x assume il valore del numero di token del corpus 1
    if x1>=x2:
        x=x1
    #se il corpus 2 è più grande del corpus 1, x assume il valore del numero di token del corpus 2
    if x1<x2:
        x=x2

    #finchè il contatore i è minore o uguale a n 
    while i<=n:
        #aggiorno il contatore
        i+=1
        #quando i è uguale a n (quando si raggiunge l'i-esimo token, stabilito come limite della porzione da analizzare)
        if i==n:
            #calcolo le liste dei token da 0 a n
            L1=tokensTOT1[0:n]
            L2=tokensTOT2[0:n]
            #calcolo il vocabolaio delle liste e il numero di parole del vocabolario
            voc1=list(set(L1))
            num_voc1=len(voc1)
            voc2=list(set(L2))
            num_voc2=len(voc2)
            #calcolo il numero di tokens della lista dei token da 0 a n
            c1=len(L1)
            c2=len(L2)
            v1=len(voc1)
            v2=len(voc2)
            #calcolo la ricchezza lessicale dei due testi tramite la Type Token Ratio come il rapporto tra il numero di parole tipo della porzione incrementale che sto analizzando e il numero di token della porzione di corpus stessa
            #arrotondo la TTR a 4 cifre dopo la virgola
            ttr1=round((v1/c1),4)
            ttr2=round((v2/c2),4)
            #se il numero di token del corpus 1 è inferiore al contatore i, il vocabolario e la TTR assumono il valore 'none'
            if x1<i:
                num_voc1='none'
                ttr1='none'
            #se il numero di token del corpus 2 è inferiore al contatore i, il vocabolario e la TTR assumono il valore 'none'
            elif x2<i:
                num_voc2='none'
                ttr2='none'
            #stampa il numero dei token della porzione incrementale di corpus analizzata, il nome del corpus analizzato, la grandezza del suo vocabolario e la sua Type Token Ratio
            print('0 -',n,'tokens --->','\tVocabolario',nome1,':',num_voc1,'\t',nome2,':',num_voc2, '\tTTR',nome1,':',ttr1,'\t',nome2,':',ttr2)
            #aggiorna il limite della porzione incrementale di 500
            n+=500
        #se il contatore i è uguale al numero di token del corpus più grande, esce dal ciclo
        if i==x:
            break
        

#funzione che, data la lista dei tokens totali del corpus, calcola il numero di Hapax sui primi 1000 tokens
def Hapax1000(tokensTOT):
    #inizializzo la lista che conterrà gli Hapax
    hapax=[]
    #calcolo la lista dei primi 1000 tokens
    tokensTOT_1000=tokensTOT[0:1000]
    #calcolo la lista delle parole tipo a partire dalla lista dei primi 1000 tokens
    voc_1000=list(set(tokensTOT_1000))
    #per ogni elemento nel vocabolario 
    for x in voc_1000:
        #calcolo la frequenza della parola tipo sulla lista dei primi 1000 tokens
        freqTok=tokensTOT_1000.count(x)
        #se la parola tipo ricorre solo una volta
        if freqTok==1:
            #aggiungo la parola tipo alla lista degli Hapax (ovvero le parole tipo la cui frequenza è pari a 1)
            hapax.append(x)
    #calcolo il numero di parole tipo nella lista degli Hapax
    num_hapax_1000=len(hapax)
    return num_hapax_1000




#funzione che data la lista di tutti i tokens del corpus, restituisce la percentuale dell’insieme delle parole piene, la percentuale dell'insieme delle parole funzionali, la distribuzione di frequenza delle parole piene e la distribuzione di frequenza delle parole funzionali
def PosTagging(tokensTOT):
    #inizializzo la lista che conterrà le PoS
    listaPOS=[]
    #la lista che conterrà i token la cui PoS appartiene alla lista 'piene'
    listaPiene=[]
    #la lista che conterrà i token la cui PoS appartiene alla lista 'funzionali'
    listaFunzionali=[]
    #calcolo il numero di token totali del corpus
    numTok=len(tokensTOT)
    #lista che contiene le PoS corrispondenti a Aggettivi, Sostantivi, Verbi e Avverbi
    piene=['JJ','JJR','JJS','NN','NNP','NNS','NNPS','RB','RBR','RBS','VB','VBD','VBG','VBN','VBP','VBZ','WRB','MD']
    #lista che contiene le PoS corrispondenti a Articoli, Preposizioni, Congiunzioni e Pronomi
    funzionali=['CC','DT','TO','IN','PDT','PRP','PRP$','WP','WP$']
    #creo la lista delle tuple formate dal token e la PoS corrispondente
    tokensPOS=nltk.pos_tag(tokensTOT)
    #per ogni tupla nella lista delle tuple (token,PoS), aggiungo il secondo elemento della tupla alla lista che contiene le sole PoS
    for elem in tokensPOS:
        listaPOS.append(elem[1])
    #per ogni PoS nella lista delle PoS
    for elem in listaPOS:
        #se la PoS appartiene alla lista delle PoS delle parole piene, aggiungo la PoS alla lista delle parole piene
        if elem in piene:
            listaPiene.append(elem)
        #se la PoS appartiene alla lista delle PoS delle parole funzionali, aggiungo la PoS alla lista delle parole funzionali
        if elem in funzionali:
            listaFunzionali.append(elem)
            
    #calcolo la distribuzione di frequenza della lista delle parole piene e delle parole funzionali
    distPiene=nltk.FreqDist(listaPiene)
    distFunzionali=nltk.FreqDist(listaFunzionali)

    #calcolo la percentuale dell'insieme delle parole piene come il rapporto tra il numero delle PoS della lista delle parole piene e il numero dei token totali del corpus, moltiplicando per 100 e arrotondando a 4 cifre dopo la virgola
    numPiene=round(((len(listaPiene)/(numTok))*100),4)
    #calcolo la percentuale dell'insieme delle parole funzionali come il rapporto tra il numero delle PoS della lista delle parole funzionali e il numero dei token totali del corpus, moltiplicando per 100 e arrotondando a 4 cifre dopo la virgola
    numFunzionali=round(((len(listaFunzionali)/(numTok))*100),4)
    
    return numPiene, numFunzionali, distPiene, distFunzionali


#funzione che, data una distribuzione, per ogni elemento nella distribuzione, stampa l'elemento corrente e la sua frequenza
def StampaDistribuzioniPOS(distribuzione):
    for x in distribuzione:
        print('PoS:', x, '\tFrequenza:', distribuzione[x])

        
#le seguenti funzioni per il confronto tra i 2 corpus variano in base ai dati che si vanno a confrontare, ma sono identiche nel funzionamento
#in particolare, la differenza riguarda l'uso di preposizioni/verbi diversi nel momento in cui si va a costruire la stringa che verrà successivamente stampata (nome1, nome2)
        
#funzione che, dati due valori, restituice in output il nome del corpus con il valore maggiore e il nome del corpus con il valore minore
def Confronto1(x1,x2):
    #nomi dei due corpus
    nomeFile1="'A Vindication of the Rights of Woman'"
    nomeFile2='Ted Talks'
    #inizializzo le variabili che conterranno i nomi finali dei file
    nome1='true'
    nome2='true'
    #se il primo valore è maggiore del secondo, il nome del primo file assume il nome del corpus 1 e il nome del secondo file assume il nome del corpus 2
    if x1>x2:
        nome1=nomeFile1+ ' ha'
        nome2='dei '+nomeFile2+'.'
    else:
    #altrimenti il nome del primo file assume il nome del corpus 2 e il nome del secondo file assume il nome del corpus 1
        nome1='i '+nomeFile2+' hanno'
        nome2='di '+nomeFile1+'.'
    return nome1, nome2


def Confronto2(x1,x2):
    nomeFile1="'A Vindication of the Rights of Woman'"
    nomeFile2='Ted Talks'
    nome1='true'
    nome2='true'
    if x1>x2:
        nome1='di '+nomeFile1
        nome2='dei '+nomeFile2+'.'
    else:
        nome1='dei '+nomeFile2
        nome2='di '+nomeFile1+'.'
    return nome1, nome2


def Confronto3(x1,x2):
    nomeFile1="'A Vindication of the Rights of Woman'"
    nomeFile2='Ted Talks'
    nome1='true'
    nome2='true'
    if x1>x2:
        nome1=nomeFile1+' ha'
        nome2='dei '+nomeFile2+'.'
    else:
        nome1='i '+nomeFile2+' hanno'
        nome2='di '+nomeFile1+'.'
    return nome1, nome2


def Confronto4(x1,x2):
    nomeFile1="'A Vindication of the Rights of Woman'"
    nomeFile2='Ted Talks'
    nome1='true'
    nome2='true'
    if x1>x2:
        nome1='in '+nomeFile1
        nome2='nei '+nomeFile2+'.'
    else:
        nome1='nei '+nomeFile2
        nome2='in '+nomeFile1+'.'
    return nome1, nome2
    

def main(file1, file2):
    fileInput1= open(file1, mode='r', encoding='utf-8')
    fileInput2= open(file2, mode='r', encoding='utf-8')
    #nomifiles
    nome_file1="'A Vindication of the Rights of Woman'"
    nome_file2='Ted Talks'
    #variabile che contiene tutto il testo
    raw1= fileInput1.read()
    raw2= fileInput2.read()
    #carico il tokenizzatore
    s_tokenizer= nltk.data.load('tokenizers/punkt/english.pickle')
    #frasi dei due corpus
    frasi1= s_tokenizer.tokenize(raw1)
    frasi2= s_tokenizer.tokenize(raw2)
    #calcolo il numero delle frasi
    num_frasi1=len(frasi1)
    num_frasi2=len(frasi2)
    #calcolo la lista dei tokens, il numero dei tokens totali e il numero medio di tokens per frase
    tokensTOT1, num_tokens1, lunghezzaFrasi_media1=Tokenizzatore(frasi1, num_frasi1)
    tokensTOT2, num_tokens2, lunghezzaFrasi_media2=Tokenizzatore(frasi2, num_frasi2)
    #calcolo il numero medio di caratteri per token
    lunghezzaTokens_media1=CalcoloCaratteriMedia(tokensTOT1)
    lunghezzaTokens_media2=CalcoloCaratteriMedia(tokensTOT2)
    #vocabolario
    vocabolario1=list(set(tokensTOT1))
    vocabolario2=list(set(tokensTOT2))

    #calcolo il numero di hapax sui primi 1000 token
    numHapax1000_1=Hapax1000(tokensTOT1)
    numHapax1000_2=Hapax1000(tokensTOT2)
   
    #calcolo percentuale dell'insieme delle parole piene, dell'insieme della parole funzionali e la loro distribuzione
    percentualePiene1, percentualeFunzionali1, distribuzionePiene1, distribuzioneFunzionali1=PosTagging(tokensTOT1)
    percentualePiene2, percentualeFunzionali2, distribuzionePiene2, distribuzioneFunzionali2=PosTagging(tokensTOT2)

    #output dei confornti tra i corpus
    cFrasi1, cFrasi2=Confronto1(num_frasi1, num_frasi2)
    cTokens1, cTokens2=Confronto1(num_tokens1, num_tokens2)
    cLunFrasi1, cLunFrasi2=Confronto2(lunghezzaFrasi_media1, lunghezzaFrasi_media2)
    cLunTok1, cLunTok2=Confronto2(lunghezzaTokens_media1, lunghezzaTokens_media2)
    cHapax1, cHapax2=Confronto3(numHapax1000_1, numHapax1000_2)
    cPiene1, cPiene2=Confronto4(percentualePiene1, percentualePiene2)
    cFunz1, cFunz2=Confronto4(percentualeFunzionali1, percentualeFunzionali2)
    

    #stampe dei dati e dei confronti
    print()
    print('Enrica Di Rado')
    print()
    print('Programma 1')
    print()
    print(nome_file1, 'contiene', num_frasi1, 'frasi, mentre i', nome_file2, 'contengono', num_frasi2, 'frasi.')
    print('Quindi,', cFrasi1, 'più frasi', cFrasi2)
    print()
    print()
    print(nome_file1, 'contiene', num_tokens1, 'tokens, mentre i', nome_file2, 'contengono', num_tokens2, 'tokens.')
    print('Quindi,', cTokens1, 'più tokens', cTokens2)
    print()
    print()
    print('Mediamente, le frasi di', nome_file1, 'sono lunghe', lunghezzaFrasi_media1, 'tokens, mentre le frasi dei', nome_file2, 'sono lunghe', lunghezzaFrasi_media2, 'tokens.')
    print('Quindi, le frasi', cLunFrasi1, 'sono mediamente più lunghe delle frasi', cLunFrasi2)
    print()
    print()
    print('Mediamente, i tokens di', nome_file1, 'sono lunghi', lunghezzaTokens_media1, 'caratteri, mentre i tokens dei', nome_file2, 'sono lunghi', lunghezzaTokens_media2, 'caratteri.')
    print('Quindi, i tokens', cLunTok1, 'sono mediamente più lunghi dei token', cLunTok2)
    print()
    print()
    print('Sui primi 1000 tokens di', nome_file1, 'ci sono ', numHapax1000_1, 'hapax, mentre sui primi 1000 tokens dei', nome_file2, 'ci sono', numHapax1000_2, 'hapax.')
    print('Quindi, sui primi 1000 tokens', cHapax1, 'più hapax', cHapax2)
    print()
    print()
    print('Analisi della grandezza del vocabolario e della ricchezza lessicale per porzioni incrementali di 500 token di', nome_file1, 'e dei', nome_file2,' :')
    print()
    AndamentoCrescita500(tokensTOT1, tokensTOT2)
    print()
    print()
    print('Distribuzione parole piene di', nome_file1)
    print()
    StampaDistribuzioniPOS(distribuzionePiene1)
    print()
    print()
    print('Distribuzione parole funzionali di', nome_file1)
    print()
    StampaDistribuzioniPOS(distribuzioneFunzionali1)
    print()
    print()
    print('Distribuzione parole piene dei', nome_file2)
    print()
    StampaDistribuzioniPOS(distribuzionePiene2)
    print()
    print()
    print('Distribuzione parole funzionali dei', nome_file2)
    print()
    StampaDistribuzioniPOS(distribuzioneFunzionali2)
    print()
    print()
    print('In',nome_file1,'il',percentualePiene1,'%','di parole sono piene, mentre in',nome_file2,'le parole piene sono il',percentualePiene2,'%.')
    print('Quindi, la percentuale di parole piene', cPiene1, 'è più alta che', cPiene2)
    print()
    print('In',nome_file1,'il',percentualeFunzionali1,'%','di parole sono funzionali, mentre in',nome_file2,'le parole fuzionali sono il',percentualeFunzionali2,'%.')
    print('Quindi, la percentuale di parole funzionali', cFunz1, 'è più alta che', cFunz2)
    
    
    
    
 
    
main(sys.argv[1], sys.argv[2])
    
