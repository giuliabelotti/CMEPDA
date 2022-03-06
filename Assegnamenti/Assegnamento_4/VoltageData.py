
import os
import numpy as np
import math
import matplotlib.pyplot as plt 
from scipy import interpolate 
import argparse


class VoltageData:

    def __init__(self, times, voltage):
        self.times = np.array(times, dtype=np.float64)
        self.voltage = np.array(voltage, dtype=np.float64)
        if len(times) == len(voltage):
            self.data = np.column_stack([self.times, self.voltage])
        else:
            print('I vettori hanno lunghezze diverse')    
        self.spline = interpolate.InterpolatedUnivariateSpline(self.times, self.voltage)
    
    @classmethod
    def from_file(cls, file_path):
        times, voltage = np.loadtxt(file_path, unpack=True)
        return cls(times, voltage)    
     
    @property
    def t(self):
        return self.data[:, 0]
    
    @ property 
    def v(self):
        return self.data[:, 1]
     
    def __getitem__(self, index):
        return self.data[index] 
     
        
    def __len__(self):
        return len(self.data)
        
    def __iter__(self):
        return iter(self.data)
    
    
    def __repr__(self):
        """ Print the full content row by row """
        # Use a generator expression
        return '\n'.join('{} {}'.format(row[0], row[1]) for row in self)
    
    def __str__(self):
        """ Print the full content row-by-row with a nice formatting"""
        row_fmt = 'Row {} -> {:.1f} s, {:.2f} mV'
        return '\n'.join(row_fmt.format(i, entry[0], entry[1]) \
                         for i, entry in enumerate(self))    
    
    def __call__(self, tempo):
        return self.spline(tempo)   
    
    def plot(self, ax):
        ax = plt.figure()
        plt.plot(self.t, self.v)
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [mV]')
        plt.grid(True)
        return ax
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lettura file')
    parser.add_argument('infile', help='path to the input file')
    args = parser.parse_args()
    a = VoltageData.from_file(args.infile)

    #print(a.data)
    a.plot(a.times)
    plt.show()
    
    
                    