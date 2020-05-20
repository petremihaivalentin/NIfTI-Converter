import os
import numpy as np
from numpy import savetxt
from nibabel.testing import data_path 
import nibabel as nib
import sys, getopt

def main(argv):
    inputfile= ''
    outputfile= ''
    try:
        opts, args = getopt.getopt(argv, "hi:o", ["ifile=","ofile="])
    except getopt.GetoptError:
        print('nii2out.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('nii2out.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg

    
    image = nib.load(inputfile)
    image_array = image.get_data()

    data_hu = np.ones((512,512))


    for i in range(0, image_array.shape[0]):
        for j in range(0, image_array.shape[1]):
                data_hu[i][j] = np.mean(image_array[i][j])*image.dataobj.slope + image.dataobj.inter
    
    file_name = inputfile[:-4] + ".out"

    savetxt(file_name, data_hu, delimiter=' ')
    print("printed" + file_name)

if __name__ == "__main__":
   main(sys.argv[1:])