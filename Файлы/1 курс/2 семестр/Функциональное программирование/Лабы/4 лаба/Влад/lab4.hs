
data SimpleType = IntType | FloatType | StringType deriving (Eq, Show)


data Field = Field String SimpleType deriving (Show)


data Structure = Structure String [Field] deriving (Show)


data Type = Simple SimpleType | Complex String deriving (Eq, Show)


data Identifier = Identifier String Type deriving (Show)


type Database = [(String, Identifier)]


structures :: [(String, Structure)]
structures =
    [ ("Person", Structure "Person" [Field "age" IntType, Field "name" StringType])
    , ("Car", Structure "Car" [Field "model" StringType, Field "year" IntType])
    ]


isStructured :: Identifier -> Bool
isStructured (Identifier _ (Complex _)) = True
isStructured _ = False


getType :: String -> Database -> Maybe Type
getType name db = lookup name db >>= Just . snd


lookupStruct :: String -> [(String, Structure)] -> Maybe [Field]
lookupStruct name structs =
    case lookup name structs of
        Just (Structure _ fields) -> Just fields
        Nothing -> Nothing


getFields :: String -> Database -> Maybe [Field]
getFields name db =
    case getType name db of
        Just (Complex structName) ->
            lookupStruct structName structures
        _ -> Nothing


getByType :: Type -> Database -> [String]
getByType targetType db =
    [name | (name, Identifier _ typ) <- db, typ == targetType]


getByTypes :: [Type] -> Database -> [String]
getByTypes types db =
    [name | (name, Identifier _ typ) <- db, typ `elem` types]


database :: Database
database =
    [ ("age", Identifier "age" (Simple IntType))
    , ("height", Identifier "height" (Simple FloatType))
    , ("name", Identifier "name" (Simple StringType))
    , ("person", Identifier "person" (Complex "Person"))
    , ("car", Identifier "car" (Complex "Car"))
    ]


main :: IO ()
main = do
    
    putStrLn "Проверка, является ли идентификатор 'person' сложным:"
    print (isStructured (Identifier "person" (Complex "Person")))  

    
    putStrLn "Получение типа идентификатора 'age':"
    print (getType "age" database)  

    
    putStrLn "Получение полей структуры 'person':"
    print (getFields "person" database)  

    
    putStrLn "Получение идентификаторов типа IntType:"
    print (getByType (Simple IntType) database)  

    
    putStrLn "Получение идентификаторов типов IntType и StringType:"
    print (getByTypes [Simple IntType, Simple StringType] database)  