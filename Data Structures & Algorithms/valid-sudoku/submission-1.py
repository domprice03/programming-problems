class Solution:

    VALID_SET = set(str(x) for x in range(1, 10))

    def validate(self, nums: List[str]) -> bool:
        seen = set()
        for num in nums:
            if num == ".":
                continue
            if num not in self.VALID_SET:
                return False
            if num in seen:
                return False
            seen.add(num)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [[] for i in range(len(board))]
        blocks = [[] for i in range(len(board))]
        for i, row in enumerate(board):
            if not self.validate(row):
                return False
            for j, element in enumerate(row):
                columns[j].append(element)
                blocks[(j//3)*3 + (i//3)].append(element)
        for col in columns:
            if not self.validate(col):
                return False
        for blk in blocks:
            if not self.validate(blk):
                return False
        return True