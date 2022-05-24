import Transpose
import Render

class Even():
        def Left(tower, steps):
            Transpose.Center(tower,1)
            steps += 1
            Render.std(steps, tower)
            Transpose.Right(tower,2)
            steps += 1
            Render.std(steps, tower)
            Transpose.Right(tower,1)
            steps += 1
            Render.std(steps, tower)
            return steps
        def Center(tower, steps):
            Transpose.Left(tower,1)
            steps += 1
            Render.std(steps, tower)
            Transpose.Right(tower,2)
            steps += 1
            Render.std(steps, tower)
            Transpose.Right(tower,1)
            steps += 1
            Render.std(steps, tower)
            return steps
        def Right(tower, steps):
            Transpose.Left(tower,1)
            steps += 1
            Render.std(steps, tower)
            Transpose.Center(tower,2)
            steps += 1
            Render.std(steps, tower)
            Transpose.Center(tower, 1)
            steps += 1
            Render.std(steps, tower)
            return steps

class NotEven():
    def Left(tower, steps):
        Transpose.Right(tower,1)
        steps += 1
        Render.std(steps, tower)
        Transpose.Center(tower,2)
        steps += 1
        Render.std(steps, tower)
        Transpose.Center(tower,1)
        steps += 1
        Render.std(steps, tower)
        return steps
    def Center(tower, steps):
        Transpose.Right(tower,1)
        steps += 1
        Render.std(steps, tower)
        Transpose.Left(tower,2)
        steps += 1
        Render.std(steps, tower)
        Transpose.Left(tower,1)
        steps += 1
        Render.std(steps, tower)
        return steps
    def Right(tower, steps):
        Transpose.Center(tower,1)
        steps += 1
        Render.std(steps, tower)
        Transpose.Left(tower,2)
        steps += 1
        Render.std(steps, tower)
        Transpose.Left(tower, 1)
        steps += 1
        Render.std(steps, tower)
        return steps