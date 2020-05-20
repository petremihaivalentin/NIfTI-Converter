from PIL import Image
import numpy as np
import sys, getopt
import math

def read(file):
    with open(file, 'r') as f:
        data = np.loadtxt(f, dtype="i", delimiter=" ")
    return data

def main(argv):
    inputfile= ''
    outputfile= ''
    try:
        opts, args = getopt.getopt(argv, "hi:o", ["ifile=","ofile="])
    except getopt.GetoptError:
        print('processNii.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('processNii.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg

    
    data = np.asarray(read(inputfile))

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i][j] != 0:
                data[i][j] *= 255
                data[i][j] = math.floor(data[i][j])

    img = Image.fromarray(data, mode='L')
    
    file_name = inputfile[:-4] + ".png"

    img.save(file_name)
    print("printed" + file_name)

if __name__ == "__main__":
   main(sys.argv[1:])