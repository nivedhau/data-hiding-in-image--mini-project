import matplotlib.image as image
img1=image.imread('Image.png')

img2=image.imread('Encoded.png')

# get a flatten 1D copy of 2D Numpy array
f_array1 = img1.flatten()
# get a flatten 1D copy of 2D Numpy array
f_array2 = img2.flatten()

y = f_array1
y_bar = f_array2
summation = 0  #variable to store the summation of differences
n = len(y)#finding total number of items in list
m=len(y_bar)
for i in range (0,n):  #looping through each element of the list
  difference = y[i] - y_bar[i]  #finding the difference between observed and predicted value
  squared_difference = difference**2  #taking square of the differene 
  summation = summation + squared_difference  #taking a sum of all the differences
print(summation)
MSE = summation/m*n  #dividing summation by total values to obtain average
print("The Mean Square Error is: " , MSE)