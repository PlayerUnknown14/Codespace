tr_height :: Double -> Double -> Double
tr_height a b = sqrt(a ^ 2 - (b / 2) ^ 2)

main :: IO ()
main = do
    let a = 5.0
    let b = 8.0
    putStrLn ("Боковая сторона треугольника " ++ show a)
    putStrLn ("Основание треугольника " ++ show b)
    let height = tr_height a b
    putStrLn ("Отсюда следует высота равнобедренного треугольника " ++ show height)
