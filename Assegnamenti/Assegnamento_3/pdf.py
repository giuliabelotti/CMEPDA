
import numpy as np
import math
from scipy.interpolate import InterpolatedUnivariateSpline
import scipy.integrate as integrate
import matplotlib.pyplot as plt

""" 
L'obiettivo è creare una classe ProbabilityDensityFunction in grado di generare numeri casuali con una data distribuzione (in questo caso uniforme)

"""

class ProbabilityDensityFunction:
    
    def __init__(self, x, y):
        """ x e y sono due array di numpy"""
        self.x = x
        self.y = y
        self.pdf = InterpolatedUnivariateSpline(x, y)
    
        ycf = np.array([self.pdf.integral(self.x[0], xcf) for xcf in self.x])
       
        self.ycfmax = ycf.max()
        self.ycfmin = ycf.min()
        
        self.cdf = InterpolatedUnivariateSpline(self.x, ycf)
        self.ppf = InterpolatedUnivariateSpline(ycf, self.x)
       
        
    def random(self, size = 1000):
        """Deve generare un array uniformemente distribuito, su cui agisce la ppf"""
        q = np.random.uniform(self.ycfmin, self.ycfmax, size = size)
        #print(f'q = {q}')
        return self.ppf(q)    
        
    def prob(self, x1, x2):
        """Return the probability for the random variable to be included
        between x1 and x2.
        """
        return self.cdf(x2) - self.cdf(x1)    

    def __call__(self, x):
        """Devo inserirla a mano perchè non ho fatto ereditare alla classe """
        return self.pdf(x)
        

def funzione():
    x = np.linspace(0., 1, 200) 
    
    #print(x)
    y1 = x[0:100]
    y2 = 1 - x[100:200]
    y = np.concatenate((y1, y2))
    #print(y)
    pdf = ProbabilityDensityFunction(x, y) #istanza della classe
    b = np.array([0.2, 0.6])
    print(pdf(b))
    plt.figure(1)
    plt.hist(pdf.random(50000))
    plt.figure(2)
    plt.plot(x, pdf.pdf(x))
    plt.figure(3)
    plt.plot(x, pdf.cdf(x))
    plt.figure(4)
    xppf = np.linspace(0,0.25,100)
    plt.plot(xppf, pdf.ppf(xppf))
    
    
    
if __name__ == '__main__':
    
    funzione()
    plt.show()
    
    

   
    

        
    
  
        