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
	// ќткрываем файл
	FILE* pFile;
	fopen_s(&pFile, fin, "rb");
	// —читываем заголовок файла
	fread_s(&header, sizeof(BITMAPFILEHEADER), sizeof(BITMAPFILEHEADER), 1, pFile);
	// —читываем заголовочную часть изображени€
	fread_s(&bmiHeader, sizeof(BITMAPINFOHEADER), sizeof(BITMAPINFOHEADER), 1, pFile);
    // ¬ыдел€ем пам€ть под массив RGB хран€щий структуры RGBTRIPLE
    rgb = new RGBTRIPLE*[bmiHeader.biHeight];
	// формируем единую область данных дл€ оптимизации хранени€
	rgb[0] = new RGBTRIPLE[bmiHeader.biWidth*bmiHeader.biHeight];
    for (int i = 1; i < bmiHeader.biHeight; i++)
    {   // нестраиваем указатели начала каждой строки
        rgb[i] = &rgb[0][bmiHeader.biWidth*i];
    }
	// перемещаемс€ на начало данных изображени€
	fseek(pFile, header.bfOffBits, SEEK_SET);
	// определ€ем величину дополнени€ на случай если ширина изображени€ не кратна 4
	int padding = get_row_data_padding(bmiHeader.biWidth);
	char tmp[3] = { 0,0,0 };
	// —читываем данные изображени€ в массив структур RGB 
    for (int i = 0; i < bmiHeader.biHeight; i++)
    {
		fread_s(&rgb[bmiHeader.biHeight - 1 - i][0], (bmiHeader.biWidth * sizeof(RGBTRIPLE)), sizeof(RGBTRIPLE), bmiHeader.biWidth, pFile);
		if (padding > 0)
			fread_s(&tmp[0], sizeof(tmp), sizeof(unsigned char), padding, pFile);
    }
    // «акрываем файл
	fclose(pFile);
}

void BMPWrite(RGBTRIPLE**& rgb, int imWidth , int imHeight, const char* fout)
{
	// ќткрываем файл дл€ записи изображени€ в формат BMP
	FILE* oFile;
	fopen_s(&oFile, fout, "wb");
	// —оздаем заголовочную часть дл€ файла BMP
	BITMAPFILEHEADER header = { 0 }; // инициализируем нул€ми
	header.bfType = ('M' << 8) + 'B';
	header.bfSize = bmp24b_file_size_calc(imWidth, imHeight);;
	header.bfOffBits = 54;
	// —оздаем заголовочную часть дл€ данных изображени€ 
	BITMAPINFOHEADER bmiHeader = { 0 }; // инициализируем нул€ми
	// заполн€ем необходимыми данными
	bmiHeader.biSize = 40;
	bmiHeader.biWidth = imWidth;
	bmiHeader.biHeight = imHeight;
	bmiHeader.biPlanes = 1;
	bmiHeader.biBitCount = 24;
	bmiHeader.biSizeImage = header.bfSize - sizeof(BITMAPINFOHEADER)- sizeof(BITMAPFILEHEADER);
	//// «аписываем заголовок файла
	fwrite(&header, sizeof(unsigned char), sizeof(BITMAPFILEHEADER), oFile);
	//// «аписываем заголовочную часть изображени€
	fwrite(&bmiHeader, sizeof(unsigned char), sizeof(BITMAPINFOHEADER), oFile);
	// определ€ем величину дополнени€ на случай если ширина изображени€ не кратна 4
	int padding = get_row_data_padding(bmiHeader.biWidth);
	char tmp[3] = { 0,0,0 };
	// «аписываем данные изображени€ из массива структур RGBTRIPLE в файл 
	for (int i = 0; i < bmiHeader.biHeight; i++)
	{
		fwrite(&(rgb[bmiHeader.biHeight - i - 1][0]), sizeof(unsigned char), bmiHeader.biWidth * sizeof(RGBTRIPLE), oFile);
		// записываем дополнение если есть
		if (padding > 0)
			fwrite(&tmp[0], sizeof(unsigned char), padding, oFile);
	}
	// закрываем файл
	fclose(oFile);
}

