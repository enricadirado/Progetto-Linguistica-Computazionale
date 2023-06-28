#importo le librerie e i moduli
import sys
import nltk
import math
from nltk import bigrams
from nltk import ne_chunk



#funzione che, dato un testo contenente i token con la PoS corrispondente, restituisce in output la lista contenente le PoS del testo 
def EstraiPOS(testoPOS):
    listaPOS=[]
    #per ogni elemento nella lista, aggiunge alla lista 'listaPOS' solo la PoS corrispondente 
    for elem in testoPOS:
        listaPOS.append(elem[1])
    return listaPOS


#funzione che, data la lista contenente le PoS del testo, restituisce in output la distribuzione con le 10 PoS più frequenti, la distribuzione con i 10 bigrammi di PoS più frequenti e la distribuzione con i 10 trigrammi di PoS più frequenti
def POS10(listaPOS):
    #distribuzione di frequenza delle PoS
    distPOS=nltk.FreqDist(listaPOS)
    #le 10 PoS più frequenti
    distPOS10=distPOS.most_common(10)

    #lista con i bigrammi di PoS
    bigrammi=list(nltk.bigrams(listaPOS))
    #distribuzione di frequenza dei bigrammi di PoS
    distBigrammi=nltk.FreqDist(bigrammi)
    #i 10 bigrammi di PoS più frequenti
    distBigrammi10=distBigrammi.most_common(10)

    #lista con i trigrammi di PoS
    trigrammi=list(nltk.trigrams(listaPOS))
    #distribuzione di frequenza dei trigrammi di PoS
    distTrigrammi=nltk.FreqDist(trigrammi)
    #i 10 trigrammi di PoS più frequenti
    distTrigrammi10=distTrigrammi.most_common(10)
    return distPOS10, distBigrammi10, distTrigrammi10


#funzione che, data una lista contenente i token con la PoS corrispondente, restituisce in output la distribuzione di frequenza dei 20 aggettivi più frequenti e la distribuzione di frequenza dei 20 avverbi più frequenti
def CalcolaDistAggAvv20(testoPOS):
    #lista delle PoS che marcano gli aggettivi
    ListaAgg=['JJ','JJS','JJR']
    #lista delle PoS che marcano gli avverbi
    ListaAvv=['RB','RBR','RBS','WRB']
    #inizializzo le liste che conterranno il token associato alla PoS
    ListaSoloAgg=[]
    ListaSoloAvv=[]
    #per ogni elemento nella lista, se il secondo elemento della tupla appartiene alla lista degli aggettivi (PoS), aggiunge il primo elemento della tupla nella lista degli aggettivi (token)
    #se il secondo elemento della tupla appartiene alla lista degli avverbi (PoS), aggiunge il primo elemento della tupla nella lista degli avverbi (token)
    for elem in testoPOS:
        if elem[1] in ListaAgg:
            ListaSoloAgg.append(elem[0])
        
        if elem[1] in ListaAvv:
            ListaSoloAvv.append(elem[0])
    #distribuzione degli aggettivi
    distAgg=nltk.FreqDist(ListaSoloAgg)
    #i 20 aggettivi più frequenti
    distAgg20=distAgg.most_common(20)
    #distribuzione degli avverbi
    distAvv=nltk.FreqDist(ListaSoloAvv)
    #i 20 avverbi più frequenti
    distAvv20=distAvv.most_common(20)
    return distAgg20, distAvv20


#funzione che, data una distribuzione di frequenza, stampa un indice (per l'ordine di frequenza decrescente), il primo elemento della tupla e la sua frequenza
def StampaDati(distribuzione):
    i=0
    for elem in distribuzione:
        i+=1
        print(i, elem[0],'\tfrequenza:', elem[1])

#funzione che, data una distribuzione di frequenza, stampa un indice (per l'ordine di frequenza decrescente), il primo e il secondo elemento della tupla e la sua frequenza
def StampaDati2(distribuzione):
    i=0
    for elem in distribuzione:
        i+=1
        print(i, elem[0][0],elem[0][1],'\tfrequenza:', elem[1])

#funzione che, data una distribuzione di frequenza, stampa un indice (per l'ordine di frequenza decrescente), il primo, il secondo e il terzo elemento della tupla la sua frequenza
def StampaDati3(distribuzione):
    i=0
    for elem in distribuzione:
        i+=1
        print(i, elem[0][0],elem[0][1],elem[0][2],'\tfrequenza:', elem[1])


#**************************************************************

#Esercizio2
#funzione che, data la lista dei tokens e la lista contenente i token con la PoS corrispondente, restituisce lista dei bigrammi Aggettivo Sostantivo e lista dei bigrammi dove token ricorre più di 3 volte
def EstraiBigrammiAggSos(tokensTOT, testoPOS):
    #lista dei bigrammi di bigrammi (token, PoS)
    listaBig=list(nltk.bigrams(testoPOS))
    #inizializzo la lista che conterrà i bigrammi di bigrammi (token,PoS) formati da aggettivo e sostantivo
    bigrammiAggSosPOS=[]
    #per ogni bigramma nella lista, se il secondo elemento del primo bigramma è un aggettivo e se il secondo elemento del secondo bigramma è un sostantivo, aggiungi il bigramma principale alla lista 
    for big in listaBig:
        if((big[0][1] in ['JJ','JJR','JJS']) and (big[1][1] in ['NN','NNP','NNPS','NNS'])):
            bigrammiAggSosPOS.append(big)

    #inizializzo la lista che conterrà i bigrammi di bigrammi (token,PoS) formati da aggettivo e sostantivo, i cui token ricorrono più di 3 volte nel corpus
    bigrammiAggSos3POS=[]
    #per ogni bigramma nella lista, se la frequenza del primo elemento del primo bigramma è maggiore di tre e la frequenza del primo elemento del secondo bigramma è maggiore di 3, aggiungi il bigramma principale alla lista
    for big in bigrammiAggSosPOS:
        freqTok1=tokensTOT.count(big[0][0])
        freqTok2=tokensTOT.count(big[1][0])
        if freqTok1>3 and freqTok2>3:
            bigrammiAggSos3POS.append(big)

    #inizializzo una lista di supporto che conterrà i bigrammi
    temp=[]
    #inizializzo la lista finale che conterrà i bigrammi formati da aggettivo e sostantivo
    bigrammiAggSos=[]
    #per ogni bigramma nella lista, aggiungo ad una lista il primo elemento del primo bigramma e il primo elemento del secondo bigramma
    for big in bigrammiAggSos3POS:
        bigramma_locale=[]
        bigramma_locale.append(big[0][0])
        bigramma_locale.append(big[1][0])
        #trasformo il la lista in un bigramma
        bigramma=list(nltk.bigrams(bigramma_locale))
        #aggiungo il bigramma creato alla lista di supporto
        temp.append(bigramma)

    #per ogni lista nella lista di bigrammi e per ogni lista interna, aggiungo alla lista finale il primo elemento della lista 
    for lista in temp:
        for elem in lista:
            bigrammiAggSos.append(lista[0])
    return bigrammiAggSos


#funzione che, data la lista dei tokens e la lista contenente i bigrammi (aggettivo, sostantivo) filtrata sulle condizioni, restituisce i dizionari della frequenza, probabilità condizionata e local mutual information
#inoltre restituisce il bigramma con frequenza massima e la relativa frequenza, il bigramma con probabilità condizionata massima e la relativa probabilità, il bigramma con LMI massima e la relativa LMI
def CreaDizionari(tokensTOT, listaBigrammiAS):
    #lunghezza del corpus
    n=len(tokensTOT)
    #lista dei bigrammi formati da tokens
    bigrammiTOT=list(nltk.bigrams(tokensTOT))
    #vocabolario dei bigrammi formati da token (aggettivo,sostantivo)
    vocBigrammiAS=set(listaBigrammiAS)

    #inizializzo i dizionari
    dizionarioFrequenze={}
    dizionarioProbabilità={}
    dizionarioLMI={}

    #inizializzo i valori della frequenza, probabilità condizionata e lmi
    frequenza=0
    probCond=0.0
    lmi=0.0

    #inizializzo i valori della frequenza massima, probabilità condizionata massima e lmi massima
    freqMAX=0
    probCondMAX=0.0
    lmiMAX=0.0

    #inizializzo il bigramm con frequenza massima, il bigramma con probabilità condizionata massima e il bigramma con LMI massima
    bigrammaFreqMAX='true'
    bigrammaProbCondMAX='true'
    bigrammaLmiMAX='true'

    #per ogni bigramma nel vocabolario 
    for bigramma in vocBigrammiAS:
        #calcolo la frequenza del bigramma sulla lista dei bigrammi (aggettivo,sostantivo) e inserisco il bigramma con la relativa frequenza nel dizionario
        frequenza=listaBigrammiAS.count(bigramma)
        dizionarioFrequenze[bigramma]=frequenza
        
        #calcolo la frequenza del primo token del bigramma sulla lista dei tokens totali
        primo_elemento=tokensTOT.count(bigramma[0])
        a=primo_elemento*1.0
        #calcolo la frequenza del secondo elemento del bigramma
        secondo_elemento=tokensTOT.count(bigramma[1])
        b=secondo_elemento*1.0
        c=n*1.0
        d=frequenza*1.0

        #calcolo la probabilità condizionata
        probCond=frequenza/primo_elemento
        #arrotondo la probabilità a 5 cifre dopo la virgola
        probCondR=round(probCond,5)
        #inserisco il bigramma con la relativa probabilità nel dizionario
        dizionarioProbabilità[bigramma]=probCondR

        #calcolo la local mutual information
        lmi=frequenza* math.log2((d*c)/(a*b))
        #arrotondo la lmi a 4 cifre dopo la virgola
        lmiR=round(lmi,4)
        #inserisco il bigramma con la relativa lmi nel dizionario
        dizionarioLMI[bigramma]=lmiR

        #se la frequenza del bigramma è maggiore della frequenza massima, la frequenza del bigramma massima assume il valore della frequenza del bigramma e il bigramma con frequenza massima diventa il bigramma stesso
        if frequenza>freqMAX:
            freqMAX=frequenza
            bigrammaFreqMAX=bigramma
        #se la probabilità del bigramma è maggiore della probabilità massima, la probabilità del bigramma massima assume il valore della probabilità del bigramma e il bigramma con probabilità massima diventa il bigramma stesso
        if probCondR>probCondMAX:
            probCondMAX=probCondR
            bigrammaProbCondMAX=bigramma
        #se la LMI del bigramma è maggiore della LMI massima, la LMI del bigramma massima assume il valore della LMI del bigramma e il bigramma con LMI massima diventa il bigramma stesso
        if lmiR>lmiMAX:
            lmiMAX=lmiR
            bigrammaLmiMAX=bigramma

    return dizionarioFrequenze, dizionarioProbabilità, dizionarioLMI, bigrammaFreqMAX, freqMAX, bigrammaProbCondMAX, probCondMAX, bigrammaLmiMAX, lmiMAX
        


#funzione che, dato in input un dizionario, restituisce in output il dizionario ordinato in ordine decrescente
def Ordina(dizionario):
    dictOrd=sorted(dizionario.items(), key=lambda x: x[1], reverse=True)
    return dictOrd

#funzione che, dato il dizionario ordinato, restituisce in output una lista contente i primi 20 elementi del dizionario
def Dict20(dizionario):
    #inizializzo la lista che conterrà gli elementi
    listaTupleOrdinate20=[]
    #calcolo il numero di elementi del dizionario
    n=len(dizionario)
    #inizializzo il contatore
    i=0
    #per ogni elemento del dizionario, se il contatore è miniore di 20, aggiungi l'elemento alla lista 
    for elem in dizionario:
        if i<20:
            listaTupleOrdinate20.append(elem)
        #aggiorno il contatore
        i+=1
    return listaTupleOrdinate20



#funzione che, data una lista, per ogni elemento della lista stampa il primo elemento del bigramma, il secondo elemento del bigramma e la frequenza del bigramma
def StampaDatiFrequenze(lista):
    for elem in lista:            
        print('Bigramma:',elem[0][0], elem[0][1],'\tFrequenza:',elem[1])

#funzione che, data una lista, per ogni elemento della lista stampa il primo elemento del bigramma, il secondo elemento del bigramma e la probabilità condizionata del bigramma
def StampaDatiProbabilità(lista):
    for elem in lista:            
        print('Bigramma:',elem[0][0], elem[0][1],'\tProbabilità condizionata:',elem[1])

#funzione che, data una lista, per ogni elemento della lista stampa il primo elemento del bigramma, il secondo elemento del bigramma e la LMI del bigramma
def StampaDatiLMI(lista):
    for elem in lista:            
        print('Bigramma:',elem[0][0], elem[0][1],'\tLMI:',elem[1])
    
#************************************************************

#Esercizio3

#funzione che, data la lista dei tokens e la lista di frasi filtrata sulle condizioni ('le frasi con almeno 6 token e più corta di 25 token'), restituisce la lista di frasi filtrata sulla nuova condizione ('ogni token occorre almeno 2 volte nel corpus di riferimento')
def EstrarreFrasi(tokensTOT, frasi):
    #inzializzo la lista che conterrà le frasi filtrate sulla condizione('ogni token occorre almeno 2 volte nel corpus di riferimento')
    listaFrasi2=[]
    #per ogni frase nella lista di frasi
    for frase in frasi:
        #calcolo la lista de tokens della frase
        tokens=nltk.word_tokenize(frase)
        #calcolo il numero di tokens della frase
        n=len(tokens)
        #inzializzo il contatore
        i=0
        #finchè il contatore è minore del numero di tokens della frase (scorre la lista)
        while i<n:
            #calcolo la frequenza del token i-esimo sulla lista dei tokens totale
            freq=tokensTOT.count(tokens[i])
            #se la frequenza è maggiore o uguale a 2
            if freq>=2:
                #aggiorna il contatore (va avanti nella lista di tokens)
                i+=1
                #se il contatore è uguale al numero di tokens della frase (se si arriva alla fine della lista)
                if i==n:
                    #aggiungo la frase alla lista di frasi filtrate
                    listaFrasi2.append(frase)
                continue
            #altrimenti se il token ricorre meno di 2 volte
            elif freq<2:
                #esci dal ciclo
                break                

    return listaFrasi2



#funzione che, data la lista di tokens totali e la lista di frasi filtrata sulle condizioni ('le frasi con almeno 6 token e più corta di 25 token','ogni token occorre almeno 2 volte nel corpus di riferimento'), restituisce la frase con la media della distribuzione di frequenza dei token più alta, la relativa distribuzione media di frequenza, la frase con la media della distribuzione di frequenza dei token più bassa e la relativa distribuzione media di frequenza
def DistribuzioneMedia(tokensTOT, frasi):
    #inizializzo la variabile che conterrà la somma di tutte le frequenze dei tokens della frase
    freqTOT=0
    #inzializzo la media della distribuzione di frequenza dei token della frase corrente, la media della distribuzione di frequenza dei token massima e la media della distribuzione di frequenza dei token minima
    lunghezzaMediaFrase=0
    lunghezzaMediaFraseMAX=0
    lunghezzaMediaFraseMIN=0
    #inizializzo la frase con media della distribuzione di frequenza dei token minima 
    fraseMIN='true'
    #per ogni frase nella lista di frasi
    for frase in frasi:
        #calcolo la lista contenente i tokens della frase corrente
        tokens=nltk.word_tokenize(frase)
        #calcolo il numero di tokens della frase
        n=len(tokens)
        #per ogni token nella lista di tokens della frase
        for tok in tokens:
            #calcolo la frequenza del token sulla lista dei tokens del corpus
            freq=tokensTOT.count(tok)
            #aggiorno la somma delle frequenze dei tokens
            freqTOT=freqTOT+freq
        #calcolo la lunghezza media della frase come il rapporto della somma di frequenze dei tokens e il numero dei tokens della frase
        lunghezzaMediaFrase=freqTOT/n
        #se la lunghezza media della frase è maggiore della lunghezza media massima
        if lunghezzaMediaFrase>=lunghezzaMediaFraseMAX:
            #la variabile della lunghezza media massima assume il valore della lunghezza media corrente
            lunghezzaMediaFraseMAX=lunghezzaMediaFrase
            #la frase corrente diventa la frase con lunghezza media massima
            fraseMAX=frase
        #se la lunghezza media della frase è minore della lunghezza media massima
        if lunghezzaMediaFrase<lunghezzaMediaFraseMAX:
            #se la frase con lunghezza media della frase minima ha come valore 'true'
            if fraseMIN=='true':
                #la variabile della lunghezza media minima assume il valore della lunghezza media corrente
                lunghezzaMediaFraseMIN=lunghezzaMediaFrase
                #la frase corrente diventa la frase con lunghezza media minima
                fraseMIN=frase
            #se la lunghezza media della frase è minore o uguale alla lunghezza media minima
            if lunghezzaMediaFrase<=lunghezzaMediaFraseMIN:
                #la variabile della lunghezza media minima assume il valore della lunghezza media corrente
                lunghezzaMediaFraseMIN=lunghezzaMediaFrase
                #la frase corrente diventa la frase con lunghezza media minima
                fraseMIN=frase                

    return lunghezzaMediaFraseMAX, lunghezzaMediaFraseMIN, fraseMAX, fraseMIN
        

#funzione che, dati in input la distribuzione di frequenza dei token del corpus di riferimento, il numero di tokens del corpus di riferimento, i bigrammi del corpus di riferimento, la distribuzione di frequenza dei bigrammi del corpus di riferimento, i trigrammi del corpus di riferimento, la distribuzione di frequenza dei trigrammi del corpus di riferimento, restituisce in output la probabilità calcolata attraverso un modello di Markov di ordine 2 della frase
def CatenaMarkov(distribuzioneFreq, n, bigrammi, distribuzioneFreqBigrammi, trigrammi, distribuzioneFreqTrigrammi):
    #primo elemento del primo bigramma (primo token)
    primoTok=bigrammi[0][0]
    #frequenza del primo token 
    primoTokFreq=distribuzioneFreq[primoTok]
    #probabilità del primo token calcolata come il rapporto tra la sua frequenza e il numero di tokens del corpus
    prob1=primoTokFreq/n

    #primo bigramma nella lista dei bigrammi
    primoBig=bigrammi[0]
    #frequenza del primo bigramma
    primoBigFreq=distribuzioneFreqBigrammi[primoBig]
    #probabilità del primo bigramma calcolata come il rapporto tra la sua frequenza e la frequenza del primo elemento del bigramma stesso 
    prob2=primoBigFreq/primoTokFreq

    #inizializzo la variabile che conterrà la probabilità totale
    #assegno alla variabile il prodotto tra la probabilità del primo token e la probabilità del primo bigramma
    prob=prob1*prob2
    #per ogni trigramma nella lista dei trigrammi
    for trigramma in trigrammi:
        #calcolo la frequenza del trigramma corrente
        freqTrigramma=distribuzioneFreqTrigrammi[trigramma]
        #calcolo la frequenza del bigramma formato dai primi due elementi del trigramma
        freqBigramma=distribuzioneFreqBigrammi[(trigramma[0],trigramma[1])]
        #calcolo la probabilità del trigramma come il rapporto tra la frequenza del trigramma e la frequenza del bigramma
        p=freqTrigramma/freqBigramma
        #aggiorno la probabilità totale 
        prob=prob*p
    return prob


#*************************************************************
#ESERCIZIO 4

#funzione che, data la lista di frasi totali, stampa un indice per l'ordine di frequenza, 
def EstraiNE(frasi):
    #inizializzo il contatore
    i=0
    #inizializzo la lista che conterrà i nomi propri 
    nomi=[]
    #per ogni frase nella lista delle frasi
    for frase in frasi:
        #calcolo la lista dei tokens della frase
        tokens=nltk.word_tokenize(frase)
        #calcolo la lista delle tuple formate dal token e la PoS corrispondente
        tokensPOS=nltk.pos_tag(tokens)
        #calcolo l'albero delle entità nominate a partire dalle tuple token,PoS
        analisi=nltk.ne_chunk(tokensPOS)
        #per ogni nodo nell'albero
        for nodo in analisi:
            #inizializzo la variabile che conterrà il nome proprio di persona 
            NE=''
            #se il nodo è nodo intermedio
            if hasattr(nodo, 'label'):
                #se l'etichetta del nodo intermedio è uguale a 'PERSON' (corrisponde a un nome di persona)
                if nodo.label()=='PERSON':
                    #per ogni elemento della lista di foglie del nodo
                    for partNE in nodo.leaves():
                        #aggiorno la variabile con la prima parte della tupla (token,PoS)
                        NE=NE+' '+partNE[0]
                        #aggiungo alla lista che contiene i nomi propri di persona la variabile NE
                        nomi.append(NE)

    #distribuzione di frequenza dei nomi propri
    DistNomiPropri=nltk.FreqDist(nomi)
    #i 15 nomi propri più frequenti
    ordered_freq=DistNomiPropri.most_common(15)
    #per ogni nome nella distribuzione di frequenza con i 15 nomi più frequenti
    for nome in ordered_freq:
        #aggiorna il contatore
        i+=1
        #stampa un indice di ordine di frequenza, il nome e la sua frequenza
        print(i,nome[0], '\tFrequenza:', nome[1])
    

#*************************************************************
#funzione che, data la lista di frasi, restituisce in output la lista contenente tutti i token del corpus, la lista contenente le tuple formate dal token e la PoS corrispondente e la lista con le frasi filtrate sulla condizione ('le frasi con almeno 6 token e più corta di 25 token')
def AnnotazioneLinguistica(frasi):
    #inizializzo le liste
    tokensTOT=[]
    tokensPOS=[]
    listaFrasiFiltrate=[]
    #per ogni frase nella lista di frasi
    for frase in frasi:
        #calcola la lista dei tokens della frase corrente
        tokens=nltk.word_tokenize(frase)
        #calcola il numero di tokens della frase corrente
        lunghezza_frase=len(tokens)
        #se la frase è lunga tra 6 e 24 tokens, aggiungi la frase alla lista delle frasi filtrate
        if lunghezza_frase>=6 and lunghezza_frase<25:
            listaFrasiFiltrate.append(frase)
        #calcola la lista delle tuple (token,Pos)
        pos=nltk.pos_tag(tokens)
        #aggiorna le liste 
        tokensTOT=tokensTOT+tokens
        tokensPOS=tokensPOS+pos
    return tokensTOT, tokensPOS, listaFrasiFiltrate



def main(file1, file2):
    fileInput1= open(file1, mode='r', encoding='utf-8')
    fileInput2= open(file2, mode='r', encoding='utf-8')
    #nomi dei corpus
    nome_file1="'A Vindication of the Rights of Woman'"
    nome_file2='Ted Talks'
    #contenuto dei corpus
    raw1= fileInput1.read()
    raw2= fileInput2.read()
    #carico il tokenizzatore
    s_tokenizer= nltk.data.load('tokenizers/punkt/english.pickle')
    #calcolo la lista delle frasi
    frasi1= s_tokenizer.tokenize(raw1)
    frasi2= s_tokenizer.tokenize(raw2)
    #calcolo la lista contenente tutti i token del corpus, la lista contenente le tuple formate dal token e la PoS corrispondente e la lista con le frasi filtrate sulla condizione ('le frasi con almeno 6 token e più corta di 25 token')
    testoToken1, testoPOS1, listaFrasiFiltro6Token_1=AnnotazioneLinguistica(frasi1)
    testoToken2, testoPOS2, listaFrasiFiltro6Token_2=AnnotazioneLinguistica(frasi2)

    
    #ESERCIZIO 1
    #calcolo la lista contenente le PoS del testo 
    listaPOS1=EstraiPOS(testoPOS1)
    listaPOS2=EstraiPOS(testoPOS2)
    #calcolo la distribuzione delle 10 PoS più frequenti
    distPOS10_1, distBigrammi10_1, distTrigrammi10_1=POS10(listaPOS1)
    distPOS10_2, distBigrammi10_2, distTrigrammi10_2=POS10(listaPOS2)
    #calcolo la distribuzione dei 20 aggettivi e dei 20 avverbi più frequenti
    distAgg20_1, distAvv20_1=CalcolaDistAggAvv20(testoPOS1)
    distAgg20_2, distAvv20_2=CalcolaDistAggAvv20(testoPOS2)

    
    #ESERCIZIO 2 
    bigrammiAggSos_1=EstraiBigrammiAggSos(testoToken1, testoPOS1)
    bigrammiAggSos_2=EstraiBigrammiAggSos(testoToken2, testoPOS2)
    #dizionari frequenza, probabilità condizionata e LMI
    #bigramma con frequenza massima e la sua frequenza, bigramma con probabilità condizionata massima e la sua probabilità, bigramma con LMI massima e la sua LMI 
    dictFreq1, dictProb1, dictLMI1, bigrammaFreqMAX1, freqMAX1, bigrammaProbCond1, probCondMAX1, bigrammaLmiMAX1, lmiMAX1=CreaDizionari(testoToken1, bigrammiAggSos_1)
    dictFreq2, dictProb2, dictLMI2, bigrammaFreqMAX2, freqMAX2, bigrammaProbCond2, probCondMAX2, bigrammaLmiMAX2, lmiMAX2=CreaDizionari(testoToken2, bigrammiAggSos_2)
    #dizionati ordinati
    dictFreqOrd1=Ordina(dictFreq1)
    dictProbOrd1=Ordina(dictProb1)
    dictLMIOrd1=Ordina(dictLMI1)
    dictFreqOrd2=Ordina(dictFreq2)
    dictProbOrd2=Ordina(dictProb2)
    dictLMIOrd2=Ordina(dictLMI2)
    #primi 20 elementi dei dizionari ordinati
    listaFrequenzeOrdinate20_1=Dict20(dictFreqOrd1)
    listaProbabilitàOrdinate20_1=Dict20(dictProbOrd1)
    listaLMIOrdinate20_1=Dict20(dictLMIOrd1)
    listaFrequenzeOrdinate20_2=Dict20(dictFreqOrd2)
    listaProbabilitàOrdinate20_2=Dict20(dictProbOrd2)
    listaLMIOrdinate20_2=Dict20(dictLMIOrd2)


    #ESERCIZIO 3
    listaFrasi2_1=EstrarreFrasi(testoToken1, listaFrasiFiltro6Token_1)
    listaFrasi2_2=EstrarreFrasi(testoToken2, listaFrasiFiltro6Token_2)
    lunghezzaMediaFraseMAX_1, lunghezzaMediaFraseMIN_1, fraseMAX_1, fraseMIN_1 =DistribuzioneMedia(testoToken1, listaFrasi2_1)
    lunghezzaMediaFraseMAX_2, lunghezzaMediaFraseMIN_2, fraseMAX_2, fraseMIN_2 =DistribuzioneMedia(testoToken2, listaFrasi2_2)

    bigrammi_1=list(nltk.bigrams(testoToken1))
    bigrammi_2=list(nltk.bigrams(testoToken2))
    trigrammi_1=list(nltk.trigrams(testoToken1))
    trigrammi_2=list(nltk.trigrams(testoToken2))
    
    distribuzioneFreq_1=nltk.FreqDist(testoToken1)
    distribuzioneFreq_2=nltk.FreqDist(testoToken2)
    distribuzioneFreqBigrammi_1=nltk.FreqDist(bigrammi_1)
    distribuzioneFreqBigrammi_2=nltk.FreqDist(bigrammi_2)

    distribuzioneFreqTrigrammi_1=nltk.FreqDist(trigrammi_1)
    distribuzioneFreqTrigrammi_2=nltk.FreqDist(trigrammi_2)
    n1=len(testoToken1)
    n2=len(testoToken2)

    
    #inizializzo le variabiili che conterranno le probabilità 
    prob_MarkovMAX1=0.0
    prob_MarkovMAX2=0.0
    #inizializzo le variabili che conterranno la frase con probabilità massima e la frase con probablità minima
    frase_MarkovMAX1='true'
    frase_MarkovMAX2='true'
    #per ogni frase nella lista di frasi filtrata sulla condizione ('ogni token occorre almeno 2 volte nel corpus di riferimento')
    for frase_a in listaFrasi2_1:
        #calcola i tokens della frase corrente
        tokens_frase1=nltk.word_tokenize(frase_a)
        #calcola i bigrammi della frase corrente
        bigrammi_frase1=list(nltk.bigrams(tokens_frase1))
        #calcola i trigrammi della frase corrente
        trigrammi_frase1=list(nltk.trigrams(tokens_frase1))
        #calcolo la probabilità della frase attraverso un modello di Markov di ordine 2
        prob_frase1=CatenaMarkov(distribuzioneFreq_1, n1, bigrammi_frase1, distribuzioneFreqBigrammi_1, trigrammi_frase1, distribuzioneFreqTrigrammi_1)
        #se la probabilità della frase corrente è maggiore della probabilità massima
        if prob_frase1>prob_MarkovMAX1:
            #la variabile della probabilità massima assume il valore della probabilità corrente
            prob_MarkovMAX1=prob_frase1
            #la frase corrente diventa la frase con probabilità massima
            frase_MarkovMAX1=frase_a


        

    for frase_b in listaFrasi2_2:
        tokens_frase2=nltk.word_tokenize(frase_b)
        bigrammi_frase2=list(nltk.bigrams(tokens_frase2))
        trigrammi_frase2=list(nltk.trigrams(tokens_frase2))
        prob_frase2=CatenaMarkov(distribuzioneFreq_2, n2, bigrammi_frase2, distribuzioneFreqBigrammi_2, trigrammi_frase2, distribuzioneFreqTrigrammi_2)
        if prob_frase2>prob_MarkovMAX2:
            prob_MarkovMAX2=prob_frase2
            frase_MarkovMAX2=frase_b
            
    #stampa le informazioni        
    print()
    print('Enrica Di Rado')
    print()
    print('Programma 2')
    print()
    print('Informazioni sul file:', nome_file1)
    print()
    print()
    print('Le 10 Pos più frequenti:')
    print()
    StampaDati(distPOS10_1)
    print()
    print('I 10 bigrammi di PoS più frequenti:')
    print()
    StampaDati2(distBigrammi10_1)
    print()
    print('I 10 trigrammi di PoS più frequenti:')
    print()
    StampaDati3(distTrigrammi10_1)
    print()
    print('I 20 aggettivi più frequenti:')
    print()
    StampaDati(distAgg20_1)
    print()
    print('I 20 avverbi più frequenti:')
    print()
    StampaDati(distAvv20_1)
    print()
    print()


    print()
    print()
    print('I 20 bigrammi formati da aggettivo e sostantivo ordinati per frequenza:')
    print()
    StampaDatiFrequenze(listaFrequenzeOrdinate20_1)
    print()
    print('Il bigramma con frequenza massima è',bigrammaFreqMAX1,'e la sua frequenza corrisponde a',freqMAX1)
    print()
    print()
    print('I 20 bigrammi formati da aggettivo e sostantivo ordinati per probabilità condizionata:')
    print()
    StampaDatiProbabilità(listaProbabilitàOrdinate20_1)
    print()
    print('Il bigramma con probabilità condizionata massima è', bigrammaProbCond1, 'e la sua probabilità corrisponde a', probCondMAX1)
    print()
    print()
    print('I 20 bigrammi formati da aggettivo e sostantivo ordinati per Local Mutual Information:')
    print()
    StampaDatiLMI(listaLMIOrdinate20_1)
    print()
    print('Il bigramma con Local Mutual Information massima è', bigrammaLmiMAX1, 'e la sua LMI corrisponde a', lmiMAX1)
    print()
    print()
    
    print()
    print("La frase con la media della distribuzione di frequenza di token più alta è '", fraseMAX_1, "', la cui media di distribuzione di frequenza è", lunghezzaMediaFraseMAX_1)
    print()
    print("La frase con la media della distribuzione di frequenza di token più bassa è'", fraseMIN_1,  "', la cui media di distribuzione di frequenza è", lunghezzaMediaFraseMIN_1)
    print()
    print("La frase con la probabilità più alta, stimata attraverso un modello di Markov di ordine 2, è'",frase_MarkovMAX1, "', la cui probabilità è", prob_MarkovMAX1)
    print()
    print()
    
    print('I 15 nomi propri di persona più frequenti:')
    print()
    EstraiNE(frasi1)
    print()
    print()
    print()
    print()


    
    print('Informazioni sul file:', nome_file2)
    print()
    print()
    print('Le 10 Pos più frequenti:')
    print()
    StampaDati(distPOS10_2)
    print()
    print('I 10 bigrammi di PoS più frequenti:')
    print()
    StampaDati2(distBigrammi10_2)
    print()
    print('I 10 trigrammi di PoS più frequenti:')
    print()
    StampaDati3(distTrigrammi10_2)
    print()
    print('I 20 aggettivi più frequenti:')
    print()
    StampaDati(distAgg20_2)
    print()
    print('I 20 avverbi più frequenti:')
    print()
    StampaDati(distAvv20_2)
    print()
    print()


    print()
    print()
    print('I 20 bigrammi formati da aggettivo e sostantivo ordinati per frequenza:')
    print()
    StampaDatiFrequenze(listaFrequenzeOrdinate20_2)
    print()
    print('Il bigramma con frequenza massima è',bigrammaFreqMAX2,'e la sua frequenza corrisponde a',freqMAX2)
    print()
    print()
    print('I 20 bigrammi formati da aggettivo e sostantivo ordinati per probabilità condizionata:')
    print()
    StampaDatiProbabilità(listaProbabilitàOrdinate20_2)
    print()
    print('Il bigramma con probabilità condizionata massima è', bigrammaProbCond2, 'e la sua probabilità corrisponde a', probCondMAX2)
    print()
    print()
    print('I 20 bigrammi formati da aggettivo e sostantivo ordinati per Local Mutual Information:')
    print()
    StampaDatiLMI(listaLMIOrdinate20_2)
    print()
    print('Il bigramma con Local Mutual Information massima è', bigrammaLmiMAX2, 'e la sua LMI corrisponde a', lmiMAX2)
    print()
    print()
    
    print()
    print("La frase con la media della distribuzione di frequenza di token più alta è'", fraseMAX_2, "', la cui media di distribuzione di frequenza è", lunghezzaMediaFraseMAX_2)
    print()
    print("La frase con la media della distribuzione di frequenza di token più bassa è'", fraseMIN_2, "', la cui media di distribuzione di frequenza è", lunghezzaMediaFraseMIN_2)
    print()
    print("La frase con la probabilità più alta, stimata attraverso un modello di Markov di ordine 2, è'",frase_MarkovMAX2, "', la cui probabilità è", prob_MarkovMAX2)
    print()
    print()
    
    print('I 15 nomi propri di persona più frequenti:')
    print()
    EstraiNE(frasi2)
    

main(sys.argv[1], sys.argv[2])
