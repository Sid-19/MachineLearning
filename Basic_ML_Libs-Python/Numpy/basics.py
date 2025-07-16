import numpy as np

a = np.array([1,2,3])

print(np.__version__)
print(a)
print(a.ndim) #number of dimension
print(a.size) #total number of elements
print(a.itemsize) #size in bytes of each element

a[0]=10
print(a)
b= a* np.array([2,0,2]) #multiply two arrays
print(b)


#you can also pass list to array

l=[1,2,3]
n = np.array(l)

# N is an array not a list cannot append to array

l = l + [4]
n = n + np.array(4)
print(l,n)

#Dot product
c = np.dot(a,b)
print(c)
#ALso Dot product New convention
c = a @ b
print(c)


#Multidimensional

a = np.array([[1,2,3,4],[5,4,5,6]])
print(a.shape)

# Create a 1D array from a list
array_1d = np.array([1, 2, 3])

# Create a 2x2 array of zeros
zeros_array = np.zeros((2, 2))

# Create a 3x3 array of ones
ones_array = np.ones((3, 3))

# Create a 4x4 identity matrix
identity_matrix = np.eye(4)

# Create an array with 5 equally spaced values between 0 and 10
linspace_array = np.linspace(0, 10, 5)

# Display the arrays
print("1D Array:", array_1d)
print("Zeros Array:\n", zeros_array)
print("Ones Array:\n", ones_array)
print("Identity Matrix:\n", identity_matrix)
print("Linspace Array:", linspace_array)


'''
2. Array Operations
np.add(a, b): Element-wise addition of arrays a and b.
np.subtract(a, b): Element-wise subtraction of arrays a and b.
np.multiply(a, b): Element-wise multiplication of arrays a and b.
np.divide(a, b): Element-wise division of arrays a and b.
np.dot(a, b): Dot product of arrays a and b.

3. Statistical Functions
np.mean(a): Compute the mean of array a.
np.median(a): Compute the median of array a.
np.std(a): Compute the standard deviation of array a.
np.sum(a): Compute the sum of array a.

4. Array Manipulation
np.reshape(a, new_shape): Reshape array a to new_shape.
np.flatten(a): Flatten array a to a 1D array.
np.concatenate((a, b), axis=0): Concatenate arrays a and b along axis 0.
np.split(a, indices_or_sections): Split array a into multiple sub-arrays.

5. Indexing and Slicing
a[0]: Access the first element of array a.
a[1:4]: Slice the array a from index 1 to 4.
a[:, 1]: Access all rows of the second column.
a[1, :]: Access the second row of array a.

6. Boolean Indexing
a[a > 5]: Access elements of array a that are greater than 5.
7. Mathematical Functions
np.sqrt(a): Compute the square root of array a.
np.exp(a): Compute the exponential of array a.
np.log(a): Compute the natural logarithm of array a.

8. Linear Algebra
np.linalg.inv(a): Compute the inverse of matrix a.
np.linalg.eig(a): Compute the eigenvalues and eigenvectors of matrix a.
np.linalg.svd(a): Compute the singular value decomposition of matrix a.
'''


# Create two arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
sum_array = np.add(a, b)
product_array = np.multiply(a, b)

# Statistical operations
mean_a = np.mean(a) 
std_b = np.std(b)

# Reshape and manipulate arrays
reshaped_a = np.reshape(a, (3, 1))
flattened_b = b.flatten()

# Linear algebra operations
matrix = np.array([[1, 2], [3, 4]])
inv_matrix = np.linalg.inv(matrix)

print("Sum Array:", sum_array)
print("Product Array:", product_array)
print("Mean of a:", mean_a)
print("Standard Deviation of b:", std_b)
print("Reshaped a:\n", reshaped_a)
print("Flattened b:", flattened_b)
print("Inverse of Matrix:\n", inv_matrix)