
import os
import logging
import argparse
import numpy as np
import matplotlib.pyplot as plt


logging.basicConfig(level=logging.INFO)


def conteggio_lettere(file_path):
    
    #aprire il file e leggo il contenuto
    logging.info('Apro il file "%s"', file_path)
    with open(file_path) as input_file:
       s = input_file.read()
    logging.info('Fatto. %d character(s) found.', len(s))
    
    #creo il dizionario vuoto
    lettere = 'abcdefghijklmnopqrstuvwxyz'
    freq = {}
    for ii in lettere:
        freq[ii] = 0
     
    for ii in s.lower():
        if ii in lettere:  
            freq[ii] += 1
            
    for ii, freq in freq.items():
        print('{}: {}'.format(ii, freq))
        plt.bar(ii, freq) 
    plt.xlabel('Lettere')
    plt.ylabel('Occorrenze')  
    plt.show()  


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lettura file')
    parser.add_argument('infile', help='path to the input file')
    args = parser.parse_args()
    conteggio_lettere(args.infile) 
  
   
