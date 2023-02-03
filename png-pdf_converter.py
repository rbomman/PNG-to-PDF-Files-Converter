# Python 3 code to rename multiple
# files in a directory or folder
 
# importing os module
from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader
import os, glob
import random
 
# Function to rename multiple files
def main():
   
    #rename Base PNGs Folder to whatever folder you want to use for the images you wish to convert
    folder = r'C:\Base PNGs Folder'
    for count, filename in enumerate(os.listdir(folder)):
    dst = f"{str(count)}.png"
        
    # foldername/filename, if .py file is outside folder
    src = f"{folder}/{filename}"  
    dst = f"{folder}/{dst}"
         
    # rename() function will rename all the files
    os.rename(src, dst)
        
    num_images = len(os.listdir(folder))
    rand_num = random.randint
    list_input_images = [None] * num_images 
    list_output_images = [None] * num_images 
    for in_img in range(num_images): 
        in_img 
        #make sure to rename folder here too
        list_input_images[in_img] =  Image.open(fr'C:\Base PNGs Folder\{in_img}.png')
        list_output_images[in_img] = list_input_images[in_img].convert('RGB')
        #rename Temp Folder to a folder that will be used merely for the transistional state of the image to PDF conversion
        list_output_images[in_img].save(fr'C:\Temp folder for unmerged PDFs\Python converted file{in_img}.pdf')

    # Call the PdfFileMerger
    mergedObject = PdfFileMerger()

    # Loop through all of them and append their pages
    for fileNumber in range(num_images):
        #make sure to rename this folrer as well
        mergedObject.append(PdfFileReader(fr'C:\Temp folder for unmerged PDFs\Python converted file{str(fileNumber)}'+ '.pdf', 'rb'))

    # Write all the files into a file which is named as shown below
    #rename the Folder Merged PDFs to be the Folder where you would like your merged PDFs to go
    mergedObject.write(r"C:\Merged PDFs\mergedfileoutput.pdf")
    
    #deleting the files in the folders for ease of use the next time the program is run, make sure to rename this folders appropriately as well
    directory_to_delete = r'C:\Temp folder for unmerged PDFs'
    directory_to_delete2 = r'C:\Base PNGs Folder'
    for file in os.scandir(directory_to_delete):
        os.remove(file.path) 
    for file in os.scandir(directory_to_delete2):
        os.remove(file.path) 


 
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()
