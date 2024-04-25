from handler import Handler
import os

if __name__ == "__main__":
    files: list[str] = []
    for fileName in os.listdir("./instances"):
        files.append(fileName)

    handler = Handler()

    # manda o handler resolver cada um dos problemas
    for file in files:
        handler.solveProblem("./instances/", file)