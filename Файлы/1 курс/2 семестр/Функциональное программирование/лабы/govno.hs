putTodo :: (Int, String) -> IO ()
putTodo (n, todo) = putStrLn (show n ++ ": " ++ todo)

prompt :: [String] -> IO ()
prompt todos = do
    putStrLn ""
    putStrLn "Current TODO list:"
    mapM_ putTodo (zip [0..] todos)
    command <- getLine
    interpret command todos

interpret :: String -> [String] -> IO ()
interpret ('+':' ':todo) todos = prompt (todo:todos)
interpret ('-':' ':num ) todos =
    case delete (read num) todos of
        Nothing -> do
            putStrLn "No TODO entry matches the given number"
            prompt todos
        Just todos' -> prompt todos'
interpret  "q"           todos = return ()
interpret  command       todos = do
    putStrLn ("Invalid command: `" ++ command ++ "`")
    prompt todos

delete :: Int -> [a] -> Maybe [a]
delete 0 (_:as) = Just as
delete n (a:as) = do
    as' <- delete (n - 1) as
    return (a:as')
delete _  []    = Nothing

main = do
    putStrLn "Commands:"
    putStrLn "+ <String> - Add a TODO entry"
    putStrLn "- <Int>    - Delete the numbered entry"
    putStrLn "q          - Quit"
    prompt []

Example usage:

$ runghc todo.hs
Commands:
+ <String> - Add a TODO entry
- <Int>    - Delete the numbered entry
q          - Quit

Current TODO list:
+ Go to bed

Current TODO list:
0: Go to bed
+ Buy some milk

Current TODO list:
0: Buy some milk
1: Go to bed
+ Shampoo the hamster

Current TODO list:
0: Shampoo the hamster
1: Buy some milk
2: Go to bed
- 1

Current TODO list:
0: Shampoo the hamster
1: Go to bed
q