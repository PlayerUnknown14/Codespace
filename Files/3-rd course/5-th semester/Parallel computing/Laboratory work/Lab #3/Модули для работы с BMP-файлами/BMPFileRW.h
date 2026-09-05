#include <Windows.h>
#include <fstream>

void BMPRead(RGBTRIPLE**&, BITMAPFILEHEADER&, BITMAPINFOHEADER&, const char*);
void BMPWrite(RGBTRIPLE**& rgb, int imWidth, int imHeight, const char* fout);

unsigned char get_row_data_padding(unsigned int width);
unsigned int bmp24b_file_size_calc(unsigned int width, unsigned int height);

// Определение величины дополнения на случай если ширина изображения не кратна 4
unsigned char get_row_data_padding(unsigned int width) {
	return (width % 4 == 0) ? 0 : (4 - (width * sizeof(RGBTRIPLE)) % 4);
}

// Вычисление размера BMP файла
unsigned int bmp24b_file_size_calc(unsigned int width, unsigned int height) {
	return sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER) + height * (width * sizeof(RGBTRIPLE) + get_row_data_padding(width));
}


void BMPRead(RGBTRIPLE**& rgb, BITMAPFILEHEADER& header, \
	BITMAPINFOHEADER& bmiHeader, const char* fin)
{
	// Открываем файл BMP
	std::ifstream InFile(fin, std::ios::binary);
	// Считываем заголовок файла
	InFile.read((char*)(&header), sizeof(BITMAPFILEHEADER));
	// Считываем заголовочную часть изображения
	InFile.read((char*)(&bmiHeader), sizeof(BITMAPINFOHEADER));
	// Выделяем память под массив RGB хранящий структуры RGBTRIPLE
	rgb = new RGBTRIPLE * [bmiHeader.biHeight];
	// формируем единую область данных для оптимизации хранения
	rgb[0] = new RGBTRIPLE[bmiHeader.biWidth * bmiHeader.biHeight];
	for (int i = 1; i < bmiHeader.biHeight; i++)
	{   // нестраиваем указатели начала каждой строки
		rgb[i] = &rgb[0][bmiHeader.biWidth * i];
	}
	// перемещаемся на начало данных изображения
	InFile.seekg(header.bfOffBits, std::ios::beg);
	// определяем величину дополнения на случай если ширина изображения не кратна 4
	int padding = get_row_data_padding(bmiHeader.biWidth);
	char tmp[3] = { 0,0,0 };
	// Считываем данные изображения в массив структур RGB 
	for (int i = 0; i < bmiHeader.biHeight; i++)
	{
		InFile.read((char*)(&rgb[bmiHeader.biHeight - 1 - i][0]), bmiHeader.biWidth * sizeof(RGBTRIPLE)); // RGBTRIPLE {Blue Green bRed;}
		if (padding > 0)
			InFile.read((char*)(&tmp[0]), padding);
	}
	// Закрываем файл
	InFile.close();
}

void BMPWrite(RGBTRIPLE**& rgb, int imWidth, int imHeight, const char* fout)
{
	// Открываем файл для записи изображения в формат BMP
	std::ofstream OutFile(fout, std::ios::binary);
	// Создаем заголовочную часть для файла BMP
	BITMAPFILEHEADER header = { 0 };
	header.bfType = ('M' << 8) + 'B';
	header.bfSize = bmp24b_file_size_calc(imWidth, imHeight);;
	header.bfOffBits = 54;
	// Создаем заголовочную часть для данных изображения 
	BITMAPINFOHEADER bmiHeader = { 0 };
	// заполняем необходимыми данными
	bmiHeader.biSize = 40;
	bmiHeader.biWidth = imWidth;
	bmiHeader.biHeight = imHeight;
	bmiHeader.biPlanes = 1;
	bmiHeader.biBitCount = 24;
	bmiHeader.biSizeImage = header.bfSize - sizeof(BITMAPINFOHEADER) - sizeof(BITMAPFILEHEADER);
	//// Записываем заголовок файла
	OutFile.write((char*)(&header), sizeof(BITMAPFILEHEADER));
	//// Записываем заголовочную часть изображения
	OutFile.write((char*)(&bmiHeader), sizeof(BITMAPINFOHEADER));
	// определяем величину дополнения на случай если ширина изображения не кратна 4
	int padding = get_row_data_padding(bmiHeader.biWidth);
	char tmp[3] = { 0,0,0 };
	// Записываем данные изображения из массива структур RGBTRIPLE в файл 
	for (int i = 0; i < bmiHeader.biHeight; i++)
	{
		OutFile.write((char*)&(rgb[bmiHeader.biHeight - i - 1][0]), bmiHeader.biWidth * sizeof(RGBTRIPLE));
		if (padding > 0)
			OutFile.write((char*)(&tmp[0]), padding);
	}
	// закрываем файл
	OutFile.close();
}

