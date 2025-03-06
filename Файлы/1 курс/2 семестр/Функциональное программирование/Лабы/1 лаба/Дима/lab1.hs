data Point = Point Double Double deriving (Show)

isParal :: Point -> Point -> Point -> Point -> Bool
isParal (Point x1 y1) (Point x2 y2) (Point x3 y3) (Point x4 y4) =
    (x1 + x3) / 2 == (x2 + x4) / 2 && (y1 + y3) / 2 == (y2 + y4) / 2

main :: IO ()
main = do
    let a = Point 1 1
        b = Point 2 1   
        c = Point 3 3
        d = Point 2 3
    if isParal a b c d
        then putStrLn "Четырехугольник ABCD - параллелограмм."
        else putStrLn "Четырехугольник ABCD - не параллелограмм."
