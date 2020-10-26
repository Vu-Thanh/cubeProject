class Solve:
    solutionexists = False
    halfsolutionexists = False
    minobst = []
    visited1 = []
    visited2 = []

    def checkColors(self):



    def DFSUtil2(self, puzzle, i):
        if len(self.visited2) == len(puzzle):
            return
        else:

            if not self.visited1:
                self.visited1.append(puzzle[i].op1)

                self.DFSUtil(puzzle, i + 1)


    def DFSUtil1(self,puzzle, i):
        if len(self.visited1) == len(puzzle):
            return 1
        else:

            self.visited1.append(puzzle[i].op1)
            result1 = self.checkColors()
            result2 = self.DFSUtil1(puzzle, i+1)

            if result1 == 0:
                self.visited1.pop()
                self.visited1.append(puzzle[i].op2)
                result1 = self.checkColors()

            if result1 == 0:
                self.visited1.pop()
                self.visited1.append(puzzle[i].op3)
                result1 = self.checkColors()

            if result1 == 1:
                result2 = self.DFSUtil1(puzzle, i+1)


    def DFS(self, puzzle):
        index = 0
        self.DFSUtil1(puzzle, index)
        self.DFSUtil2(puzzle, index)

    def minObstacle(self, puzzle):
        self.DEF(puzzle)