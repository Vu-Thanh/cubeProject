from Cube import Cube
import math


class Generate:

    @staticmethod
    def generate():
        puzzleArray1 = []
        puzzleArray2 = []
        puzzleArray3 = []
        puzzleArray4 = []

        n = 1  # n from formula

        for i in range(30):
            cubepuz1 = Cube()
            cubepuz2 = Cube()
            cubepuz3 = Cube()
            cubepuz4 = Cube()

            for j in range(6):
                # puzzle 1
                color1 = 1 + ((math.floor(n * math.pi)) % 30)

                # puzzle 2
                color2 = 1 + ((math.floor(n * math.e)) % 30)

                # puzzle 3
                color3 = 1 + ((math.floor(n * math.sqrt(3))) % 30)

                # puzzle 4
                color4 = 1 + ((math.floor(n * math.sqrt(5))) % 30)

                if j == 0 or j == 1:
                    cubepuz1.op1.append(color1)
                    cubepuz2.op1.append(color2)
                    cubepuz3.op1.append(color3)
                    cubepuz4.op1.append(color4)
                elif j == 2 or j == 3:
                    cubepuz1.op2.append(color1)
                    cubepuz2.op2.append(color2)
                    cubepuz3.op2.append(color3)
                    cubepuz4.op2.append(color4)
                elif j == 4 or j == 5:
                    cubepuz1.op3.append(color1)
                    cubepuz2.op3.append(color2)
                    cubepuz3.op3.append(color3)
                    cubepuz4.op3.append(color4)

                n += 1

            puzzleArray1.append(cubepuz1)
            puzzleArray2.append(cubepuz2)
            puzzleArray3.append(cubepuz3)
            puzzleArray4.append(cubepuz4)

        return puzzleArray1, puzzleArray2, puzzleArray3, puzzleArray4
