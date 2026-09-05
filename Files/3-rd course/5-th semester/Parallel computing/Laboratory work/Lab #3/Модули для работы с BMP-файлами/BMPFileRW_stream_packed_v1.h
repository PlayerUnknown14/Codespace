#include <fstream>


// дл€ того чтобы компил€тор не дополн€л байтами  упаковываем т.е. все данные идут р€дом
#pragma pack(push, 1)  
typedef struct {
	unsigned short    bfType;
	unsigned long    bfSize;
	unsigned short    bfReserved1;
	unsigned short    bfReserved2;
	unsigned long    bfOffBits;
} BITMAPFILEHEADER;
#pragma pack(pop)


typedef struct {
	unsigned long       biSize;
	long        biWidth;
	long        biHeight;
	unsigned short        biPlanes;
	unsigned short       biBitCount;
	unsigned long       biCompression;
	unsigned long       biSizeImage;
	long        biXPelsPerMeter;
	long        biYPelsPerMeter;
	unsigned long       biClrUsed;
	unsigned long       biClrImportant;
} BITMAPINFOHEADER;

//
typedef struct tagRGBTRIPLE {
	unsigned char rgbtBlue;
	unsigned char     rgbtGreen;
	unsigned char     rgbtRed;
} RGBTRIPLE;



void BMPRead(RGBTRIPLE **&, BITMAPFILEHEADER&, BITMAPINFOHEADER&, const char *);
void BMPWrite(RGBTRIPLE**& rgb, int imWidth, int imHeight, const char* fout);

unsigned char get_row_data_padding(unsigned int width);
unsigned int bmp24b_file_size_calc(unsigned int width, unsigned int height);

// ќпределение величины дополнени€ на случай если ширина изображени€ не кратна 4
unsigned char get_row_data_padding(unsigned int width) {
	return (width % 4 == 0) ? 0 : (4 - (width * sizeof(RGBTRIPLE)) % 4);
}

// ¬ычисление размера BMP файла
unsigned int bmp24b_file_size_calc(unsigned int width, unsigned int height) {
	return sizeof(BITMAPFILEHEADER)+ sizeof(BITMAPINFOHEADER) +  height * (width* sizeof(RGBTRIPLE) + get_row_data_padding(width));
}


void BMPRead(RGBTRIPLE** &rgb, BITMAPFILEHEADER &header, \
	BITMAPINFOHEADER &bmiHeader, const char* fin)
{
    // ќткрываем файл BMP
	std::ifstream InFile(fin, std::ios::binary);
	// —читываем заголовок файла
	InFile.read((char*)(&header), sizeof(BITMAPFILEHEADER));
	// —читываем заголовочную часть изображени€
	InFile.read((char*)(&bmiHeader), sizeof(BITMAPINFOHEADER));
    // ¬ыдел€ем пам€ть под массив RGB хран€щий структуры RGBTRIPLE
    rgb = new RGBTRIPLE*[bmiHeader.biHeight];
	// формируем единую область данных дл€ оптимизации хранени€
	rgb[0] = new RGBTRIPLE[bmiHeader.biWidth*bmiHeader.biHeight];
    for (int i = 1; i < bmiHeader.biHeight; i++)
    {   // нестраиваем указатели начала каждой строки
        rgb[i] = &rgb[0][bmiHeader.biWidth*i];
    }
	// перемещаемс€ на начало данных изображени€
	InFile.seekg(header.bfOffBits, std::ios::beg);
	// определ€ем величину дополнени€ на случай если ширина изображени€ не кратна 4
	int padding = get_row_data_padding(bmiHeader.biWidth);
	char tmp[3] = { 0,0,0 };
	// —читываем данные изображени€ в массив структур RGB 
    for (int i = 0; i < bmiHeader.biHeight; i++)
    {
			InFile.read((char*)(&rgb[bmiHeader.biHeight-1-i][0]), bmiHeader.biWidth*sizeof(RGBTRIPLE)); // RGBTRIPLE {Blue Green bRed;}
			if (padding > 0)
				InFile.read((char*)(&tmp[0]), padding);
    }
    // «акрываем файл
	InFile.close();
}

void BMPWrite(RGBTRIPLE**& rgb, int imWidth , int imHeight, const char* fout)
{
	// ќткрываем файл дл€ записи изображени€ в формат BMP
	std::ofstream OutFile(fout, std::ios::binary);
	// —оздаем заголовочную часть дл€ файла BMP
	BITMAPFILEHEADER header = { 0 };
	header.bfType = ('M' << 8) + 'B';
	header.bfSize = bmp24b_file_size_calc(imWidth, imHeight);;
	header.bfOffBits = 54;
	// —оздаем заголовочную часть дл€ данных изображени€ 
	BITMAPINFOHEADER bmiHeader = { 0 };
	// заполн€ем необходимыми данными
	bmiHeader.biSize = 40;
	bmiHeader.biWidth = imWidth;
	bmiHeader.biHeight = imHeight;
	bmiHeader.biPlanes = 1;
	bmiHeader.biBitCount = 24;
	bmiHeader.biSizeImage = header.bfSize - sizeof(BITMAPINFOHEADER)- sizeof(BITMAPFILEHEADER);
	//// «аписываем заголовок файла
	OutFile.write((char*)(&header), sizeof(BITMAPFILEHEADER));
	//// «аписываем заголовочную часть изображени€
	OutFile.write((char*)(&bmiHeader), sizeof(BITMAPINFOHEADER));
	// определ€ем величину дополнени€ на случай если ширина изображени€ не кратна 4
	int padding = get_row_data_padding(bmiHeader.biWidth);
	char tmp[3] = { 0,0,0 };
	// «аписываем данные изображени€ из массива структур RGBTRIPLE в файл 
	for (int i = 0; i < bmiHeader.biHeight; i++)
	{
		OutFile.write((char*)&(rgb[bmiHeader.biHeight - i - 1][0]), bmiHeader.biWidth * sizeof(RGBTRIPLE));
		if (padding > 0)
			OutFile.write((char*)(&tmp[0]), padding);
	}
	// закрываем файл
	OutFile.close();
}

