import numpy as np
def intro():
    matrixA = np.array([[1,0], [0,1]])
    matrixB = np.array([[0,1],[1,0]])
    matrixC = np.matmul(matrixA, matrixB)
    print("Matrix A has a 2x2 shape:\n"+ str(matrixA)+'\n')
    print("Matrix B has a 2x2 shape:\n"+ str(matrixB)+'\n') 
    question = input("What would matrix C be? \n")
    matrixC = np.matmul(matrixA, matrixB)
    print(matrixC)
        
def example1():
    print("\nProblem #1\n")
    matrixA = np.array([[3,4,5],
                        [0,1,2]])
    matrixB = np.array([[3,4],
                    [5, 8],
                    [1, 6]])
    matrixC = np.matmul(matrixA, matrixB)
    print("Matrix A has a 2x3 shape:\n"+ str(matrixA)+'\n')
    print("Matrix B has a 3x2 shape:\n"+ str(matrixB)+'\n') 
    question = input("What would the second row of Matrix C be? \n")
    matrixC = np.matmul(matrixA, matrixB)
    if question in str(matrixC[1]):
        print("Good job! The full resulting matrix is")
        print(matrixC)
    else: 
        print("Not quite. The full resulting matrix is")
        print(matrixC)

def example2():
    print("\nProblem #2\n")
    matrixA = np.array([[2, 3]])
    matrixB = np.array([[14,18],
                    [2, 1]])
    matrixC = np.matmul(matrixA, matrixB)
    print("Matrix A has a 1x3 shape:\n"+ str(matrixA)+'\n')
    print("Matrix B has a 3x2 shape:\n"+ str(matrixB)+'\n') 
    question = input("What would matrix C be? \n")
    matrixC = np.matmul(matrixA, matrixB)
    if question in str(matrixC):
        print("Good job! The full resulting matrix is")
        print(matrixC)
    else: 
        print("Not quite. The full resulting matrix is")
        print(matrixC)

def example3():
    print("\n Problem #3\n")
    matrixA = np.array([[10, 20, 30]])
    matrixB = np.array([[1,2],
                    [2, 1],
                    [1, 2]])
    matrixC = np.matmul(matrixA, matrixB)
    print("Matrix A has a 1x3 shape:\n"+ str(matrixA)+'\n')
    print("Matrix B has a 3x2 shape:\n"+ str(matrixB)+'\n') 
    question = input("What would matrix C be? \n")
    matrixC = np.matmul(matrixA, matrixB)
    if question in str(matrixC):
        print("Good job! The full resulting matrix is")
        print(matrixC)
    else: 
        print("Not quite. The full resulting matrix is")
        print(matrixC)

def example4():
    print("\n Problem #4\n")
    matrixA = np.array([[1, 2, 3], 
                        [3, 2, 1], 
                        [1, 1, 1]])
    matrixB = np.array([[1,2],
                    [1, 2],
                    [1, 2]])
    matrixC = np.matmul(matrixA, matrixB)
    print("Matrix A has a 3x3 shape:\n"+ str(matrixA)+'\n')
    print("Matrix B has a 3x2 shape:\n"+ str(matrixB)+'\n') 
    question = input("What would the final row in matrix C be? \n")
    matrixC = np.matmul(matrixA, matrixB)
    if question in str(matrixC[2]):
        print("Good job! The full resulting matrix is")
        print(matrixC)
    else: 
        print("Not quite. The full resulting matrix is")
        print(matrixC)

def example5():
    print("\nProblem #5\n")
    matrixA = np.array([[1, 2, 3], 
                        [4, 5, 6], 
                        [2, 1, 2]])
    matrixB = np.array([[1,2,3],
                    [1,2,3],
                    [1,2,3]])
    matrixC = np.matmul(matrixA, matrixB)
    print("Matrix A has a 3x3 shape:\n"+ str(matrixA)+'\n')
    print("Matrix B has a 3x3 shape:\n"+ str(matrixB)+'\n') 
    question = input("What would the final row in matrix C be? \n")
    matrixC = np.matmul(matrixA, matrixB)
    if question in str(matrixC[2]):
        print("Good job! The full resulting matrix is")
        print(matrixC)
    else: 
        print("Not quite. The full resulting matrix is")
        print(matrixC)

def main():
    intro()
    example1()
    example2()
    example3()
    example4()
    example5()
