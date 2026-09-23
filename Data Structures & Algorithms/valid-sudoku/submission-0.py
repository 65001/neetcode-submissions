class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        columns = []
        squares = []
        for i in range(0, 10):
            rows.append(set())
            columns.append(set())
            squares.append(set())

        for i in range(9):
            for j in range(9):
                squareIndex = (i // 3) * 3 + (j // 3)
                rowIndex = i
                columnIndex = j
                number = board[i][j]
                if number == ".":
                    continue
                if number in rows[i] or number in columns[j] or number in squares[squareIndex]:
                    return False
                rows[i].add(number)
                columns[j].add(number)
                squares[squareIndex].add(number)

        return True


        