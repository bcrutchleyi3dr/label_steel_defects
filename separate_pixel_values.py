import numpy as np
import pandas as pd
import math


from PIL import Image

import csv

with open('newfile.csv', newline='') as f:
    file_list = csv.reader(f)
    files = list(file_list)    

num_files = len(files)

print(num_files)

mymatrix_1= pd.read_csv("newfile.csv", delimiter=',', header = None)

df = pd.DataFrame(mymatrix_1)

arr = df.to_numpy()


x = arr [0]

print(x)

# #print(mymatrix[1])

# for n in range(1,num_files):
	
	
	# file_and_classifier = files[n]
	# file_and_classifier_string_conversion = str(file_and_classifier)
	# file_name_no_classifier = file_and_classifier_string_conversion[2:-4]
	# classifier = file_and_classifier_string_conversion[-3]
	
	
		 
	# im = Image.open(file_name_no_classifier)
	
	# pix = im.load()
	
	
	# x= arr[n]
	
	
	# x = x[np.logical_not(np.isnan(x))]
	# print(x)
	# # x.shape
	
	# # odd_i = [] 
	# # even_i = [] 
	# # for i in range(0, len(x)): 
	    # # if i % 2: 
	        # # even_i.append(x[i]) 
	    # # else : 
	        # # odd_i.append(x[i]) 
	  
	# # res = odd_i + even_i 
	# # print(odd_i)
	# # print(even_i)
	# # x = []
	# # y = []
	# # for i in range(0, len(odd_i)):
		# # x_not_rounded = odd_i[i]/256
		# # x_trunc = math.trunc(odd_i[i]/256)
		
		# # y_val = (x_not_rounded - x_trunc)*256
		
		# # x.append(x_trunc)
		# # y.append(y_val)
	
	
	
	
	
	# # for j in range (0, len(even_i)-1):
		# # for k in range(0, int(even_i[j])-1):
			# # x_pix = x[j]
			# # y_pix = y[j]+k
			
			# # if y_pix<256:
				# # if (classifier == '1'):
					# # pix[x[j],y[j]+k]=(255, 76, 76)
				# # elif(classifier == '2'):
					# # pix[x[j],y[j]+k]=(76, 255, 76)
				# # elif(classifier == '3'):
					# # pix[x[j],y[j]+k]=(76, 76, 255)
				# # else:
					# # pix[x[j],y[j]+k]=(255, 255, 0)
			
			
			# # im.save(file_name_no_classifier)
			
	
			

		
	


