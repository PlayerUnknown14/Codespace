-- Определение простых типов
data SimpleType = IntType | FloatType | StringType deriving (Eq, Show)

-- Определение полей структуры
data Field = Field String SimpleType deriving (Show)

-- Определение сложных типов (структур)
data Structure = Structure String [Field] deriving (Show)

-- Определение типа идентификатора (простой или сложный)
data Type = Simple SimpleType | Complex String deriving (Eq, Show)

-- Определение идентификатора
data Identifier = Identifier String Type deriving (Show)

-- База данных: список пар (имя_идентификатора, идентификатор)
type Database = [(String, Identifier)]

-- Список структур
structures :: [(String, Structure)]
structures =
    [ ("Person", Structure "Person" [Field "age" IntType, Field "name" StringType])
    , ("Car", Structure "Car" [Field "model" StringType, Field "year" IntType])
    ]

-- Функция для проверки, является ли идентификатор сложным типом
isStructured :: Identifier -> Bool
isStructured (Identifier _ (Complex _)) = True
isStructured _ = False

-- Функция для получения типа идентификатора по имени из базы данных
getType :: String -> Database -> Maybe Type
getType name db = lookup name db >>= Just . snd

-- Вспомогательная функция для получения полей структуры по её имени
lookupStruct :: String -> [(String, Structure)] -> Maybe [Field]
lookupStruct name structs =
    case lookup name structs of
        Just (Structure _ fields) -> Just fields
        Nothing -> Nothing

-- Функция для получения полей идентификатора, если он имеет тип структуры
getFields :: String -> Database -> Maybe [Field]
getFields name db =
    case getType name db of
        Just (Complex structName) ->
            lookupStruct structName structures
        _ -> Nothing

-- Функция для получения списка имен идентификаторов указанного типа
getByType :: Type -> Database -> [String]
getByType targetType db =
    [name | (name, Identifier _ typ) <- db, typ == targetType]

-- Функция для получения списка имен идентификаторов, принадлежащих указанным типам
getByTypes :: [Type] -> Database -> [String]
getByTypes types db =
    [name | (name, Identifier _ typ) <- db, typ `elem` types]

-- Пример базы данных
database :: Database
database =
    [ ("age", Identifier "age" (Simple IntType))
    , ("height", Identifier "height" (Simple FloatType))
    , ("name", Identifier "name" (Simple StringType))
    , ("person", Identifier "person" (Complex "Person"))
    , ("car", Identifier "car" (Complex "Car"))
    ]

-- Основная программа
main :: IO ()
main = do
    -- Проверка, является ли идентификатор сложным
    putStrLn "Проверка, является ли идентификатор 'person' сложным:"
    print (isStructured (Identifier "person" (Complex "Person")))  -- True

    -- Получение типа идентификатора 'age'
    putStrLn "Получение типа идентификатора 'age':"
    print (getType "age" database)  -- Just (Simple IntType)

    -- Получение полей структуры 'person'
    putStrLn "Получение полей структуры 'person':"
    print (getFields "person" database)  -- Just [Field "age" IntType, Field "name" StringType]

    -- Получение идентификаторов типа IntType
    putStrLn "Получение идентификаторов типа IntType:"
    print (getByType (Simple IntType) database)  -- ["age"]

    -- Получение идентификаторов типов IntType и StringType
    putStrLn "Получение идентификаторов типов IntType и StringType:"
    print (getByTypes [Simple IntType, Simple StringType] database)  -- ["age", "name"]