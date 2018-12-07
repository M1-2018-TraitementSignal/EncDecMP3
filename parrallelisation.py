
# coding: utf-8

# In[2]:

import sys
from numpy import *
from scipy import *
from matplotlib import *
import scipy.io.wavfile


# In[3]:


freq, data = scipy.io.wavfile.read('test.wav')

# args:
# 1: fichier
# 2: debut

fichier = sys.argv[1]
debutechantillon = int(sys.argv[2])

step = int(len(data) / 8)
print(step)

finechantillon = debutechantillon + step
print("le debut du suivant sera: ", finechantillon)


tableau = data[debutechantillon:finechantillon]

print(len(tableau))

# In[9]:


# print(len(data) % 8)


# In[30]:





# In[31]:



# In[29]:

def parrallelisation(nomfichier, debut, fin, data):
    print("Debut parrallelisation ..................")
    tab = fourierparpartie(data, debut, fin, 10)
    tab2 = conversionpropre(data)
    tab2.dump(nomfichier)


def fourierparpartie(data, debut, fin, taillefenetre):
    print("Debut fourier ..................")
    res = []
    taille = fin - debut
    reste = taille % taillefenetre
    newtaille = int((taille - reste) / taillefenetre)
    for k in range(0, newtaille):
        liste = data[(taillefenetre * k):(taillefenetre * (k+1))]
        tmp = numpy.fft.fft2(liste)
        res = res + [tmp]
    if reste > 0:
        liste = data[(fin - reste): fin]
        res = res + [numpy.fft.fft2(liste)]
    return res


def conversionpropre(tab, taillefenetre):
    print("Debut conversion ..................")
    reste = len(tab[len(tab) - 1])
    tab2 = []
    for i in range(0, (len(tab) - 1)):
        for j in range(0, taillefenetre):
            tab2 = tab2 + tab[i][j].tolist()
    if reste > 0:
        j = len(tab) % taillefenetre - 1
        for i in range(0,reste):
            tab2 = tab2 + tab[j][i].tolist()
    tab2 = asarray(tab2)
    return tab2

parrallelisation(fichier, debutechantillon, finechantillon, tableau)


# for i in range(0, step):
