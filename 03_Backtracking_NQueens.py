def n_queens(n):
    def solve(row, positions):
        if row == n:
            print(positions)
            return True
        for col in range(n):
            if all(positions[i] != col and abs(positions[i] - col) != row - i for i in range(row)):
                positions[row] = col
                if solve(row + 1, positions):
                    return True
        return False

    solve(0, [-1] * n)

# Input the number of queens (n)
n = int(input("Enter the number of queens: "))
n_queens(n)