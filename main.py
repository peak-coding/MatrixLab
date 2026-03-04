import numpy as np

def get_matrix():
    print("Enter the number of rows:")
    rows = int(input())
    print("Enter the number of columns:")
    cols = int(input())

    print("Enter the matrix row by row (space separated values):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    return np.array(matrix)

def compute_eigen(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        print("Eigenvalues can only be computed for square matrices.")
        return None, None

    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

def main():
    matrix = get_matrix()
    print("\nMatrix entered:")
    print(matrix)

    eigenvalues, eigenvectors = compute_eigen(matrix)

    if eigenvalues is not None:
        print("\nEigenvalues:")
        print(eigenvalues)

        print("\nEigenvectors:")
        print(eigenvectors)

if __name__ == "__main__":
    main()