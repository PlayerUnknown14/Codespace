# Unit testsclass TestCarDatabase(unittest.TestCase):
    def setUp(self):
        self.test_file = 'C:/Users/Глеб/Desktop/новая/test_data_source.txt'        with open("C:/Users/Глеб/Desktop/новая/test_data_source.txt", 'w', encoding='utf-16') as f:
            f.write("1/Manufacturer1/Model1/Red/Manual/FWD\n")            f.write("2/Manufacturer2/Model2/Blue/Automatic/RWD\n")
    def tearDown(self):
        os.remove("C:/Users/Глеб/Desktop/новая/test_data_source.txt")
    def test_add_car(self):        with open("C:/Users/Глеб/Desktop/новая/test_data_source.txt", 'r', encoding='utf-16') as f:
            original_count = len(f.readlines())
        add_car("Manufacturer3", "Model3", "Green", "Manual", "AWD")
        with open("C:/Users/Глеб/Desktop/новая/test_data_source.txt", 'r', encoding='utf-16') as f:            new_count = len(f.readlines())
        self.assertEqual(new_count, original_count + 1)
    def test_delete_car(self):
        with open("C:/Users/Глеб/Desktop/новая/test_data_source.txt", 'r', encoding='utf-16') as f:            original_count = len(f.readlines())
        delete_car(1)
        with open("C:/Users/Глеб/Desktop/новая/test_data_source.txt", 'r', encoding='utf-16') as f:
            new_count = len(f.readlines())
        self.assertEqual(new_count, original_count - 1)
    def test_add_car_content(self):        add_car("Manufacturer3", "Model3", "Green", "Manual", "AWD")
        with open("C:/Users/Глеб/Desktop/новая/test_data_source.txt", 'r', encoding='utf-16') as f:            last_line = f.readlines()[-1].strip().split("/")
            self.assertEqual(last_line[1], "Manufacturer3")            self.assertEqual(last_line[2], "Model3")
            self.assertEqual(last_line[3], "Green")            self.assertEqual(last_line[4], "Manual")
            self.assertEqual(last_line[5], "AWD")
    def test_delete_car_content(self):        delete_car(1)
        with open("C:/Users/Глеб/Desktop/новая/test_data_source.txt", 'r', encoding='utf-16') as f:            lines = f.readlines()
            self.assertNotIn("1/Manufacturer1/Model1/Red/Manual/FWD\n", lines)
if __name__ == '__main__':    unittest.main()