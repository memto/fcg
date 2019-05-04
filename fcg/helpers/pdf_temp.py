import fpdf

class PDFFlashCard(fpdf.FPDF):
	"""docstring for PDFFlashCard"""
	__a4_l_w = 298 # milimet
	__a4_l_h = 210
	def __init__(self, orient, font, size, rows, cols, spacing):
		super(PDFFlashCard, self).__init__(orient, "mm", "A4")
		self.font = font
		self.size = size

		self.orient = orient
		self.set_margins(0,0,0)
		if self.orient == "L":
			self.width = self.__a4_l_w
			self.heigh = self.__a4_l_h
		elif self.orient == "P":
			self.width = self.__a4_l_h
			self.heigh = self.__a4_l_w

		self.rows = rows
		self.cols = cols
		self.spacing = spacing

	def init_font(self):
		self.set_font(self.font, "", self.size)

	@property
	def cell_width(self):
		self._cell_width = (self.width - self.spacing*(self.cols - 1))//self.cols
		return self._cell_width

	@property
	def cell_heigh(self):
		self._cell_heigh = (self.heigh - self.spacing*(self.rows - 1))//self.rows
		return self._cell_heigh

	def border_all(self):
		for i in range(1, self.rows+1):
			for j in range(1, self.cols+1):
				self.border(i,j)

	def border(self, row, col):
		x = (col - 1) * (self.cell_width + self.spacing)
		y = (row - 1) * (self.cell_heigh + self.spacing)
		self.rect(x, y, self.cell_width, self.cell_heigh)

	def put_image(self, row, col, path):
		x = (col - 1) * (self.cell_width + self.spacing)
		y = (row - 1) * (self.cell_heigh + self.spacing)
		self.image(path, x, y, self.cell_width, self.cell_heigh)

	def put_text(self, row, col, x, y, w, h, style="", size = -1, text=""):
		size = size if size > 4 else self.size
		self.set_font(self.font, style, size)
		cell_x = (col - 1) * (self.cell_width + self.spacing)
		cell_y = (row - 1) * (self.cell_heigh + self.spacing)
		self.set_xy(cell_x+x, cell_y+y)
		self.multi_cell(w, h, text, 0, 'C')
		self.init_font()

class PDFCarBrand(PDFFlashCard):
	"""docstring for PDFCarBrand"""
	def __init__(self, orient, font, size, rows, cols, spacing):
		super(PDFCarBrand, self).__init__(orient, font, size, rows, cols, spacing)

	def add_cards(self, image_paths, brand_infos, border_all=True):
		self.front_page(image_paths, border_all)
		self.back_page(brand_infos, border_all)

	def front_page(self, image_paths, border_all):
		if not image_paths:
			return

		self.add_page()
		if border_all:
			self.border_all()

		row = 1
		col = 1
		for img in image_paths:
			self.put_image(row, col, img)
			if col == self.cols:
				row += 1; col = 1
			else:
				col += 1

	def back_page(self, brand_infos, border_all):
		if not brand_infos:
			return

		self.add_page()
		if border_all:
			self.border_all()

		row = 1
		col = 1
		for brand_info in brand_infos:
			if brand_info:
				sub_y = 0
				data = {"row": row, "col": col,
					"x": 0,
					"y": sub_y,

					"w": self.cell_width,
					"h": 10,
					"style": "B", "size": 18, "text": brand_info['country']}
				self.put_text(**data)

				data = {"row": row, "col": col,
					"x": 0,
					"y": sub_y+10,

					"w": self.cell_width,
					"h": 6,
					"style": "", "size": 10, "text": '(by Dad with <3)'}
				self.put_text(**data)

				sub_y = self.cell_heigh//3
				data = {"row": row, "col": col,
					"x": 0,
					"y": sub_y,

					"w": self.cell_width,
					"h": 18,
					"style": "", "size": 40, "text": brand_info['name']}
				self.put_text(**data)

				data = {"row": row, "col": col,
					"x": 0,
					"y": sub_y+18,

					"w": self.cell_width,
					"h": 8,
					"style": "", "size": 14, "text": brand_info['Founded']}
				self.put_text(**data)

				sub_y = (2*self.cell_heigh//3)
				data = {"row": row, "col": col,
					"x": 0,
					"y": sub_y,

					"w": self.cell_width,
					"h": 8,
					"style": "", "size": 14, "text": brand_info['Founder']}
				self.put_text(**data)

			if col == self.cols:
				row += 1; col = 1
			else:
				col += 1


def main():
	pdf = PDFCarBrand("P", "Arial", 14, 3, 2, 2)
	pdf.init_font()

	# German BMW {'idx': 2, 'Founded': '7 March 1916', 'Founder': 'Franz Josef Popp  \nKarl Rapp', 'Headquarters': 'Munich, Bavaria, Germany', 'Slogan': '"Sheer Driving Pleasure" (Worldwide)  \n"The Ultimate Driving Machine" (United States, United Kingdom)  \n"The Ultimate Driving Experience" (Canada)  \n"Freude am Fahren" (Germany)', 'Subsidiaries': 'Rolls-Royce  \nBMW M  \nMini', 'Official Site': 'www.bmw.com', 'Overview': '**BMW** (Bavarian Motor Works) is a German automobile company founded in 1916,\nit also owns and produces Mini cars and Rolls-Royce Motor Cars. BMW is one of\nthree best-selling luxury automakers in the world, along with Audi and\nMercedes-Benz.'}


	pdf.add_cards(
		# images
		[
			"samples/carbrand.jpg",
		],
		# terms
		[
			{
				'country': 'German',
				'name': 'BMW',
				'Founded': '7 March 1916',
				'Founder': 'Franz Josef Popp  \nKarl Rapp',
			}
		])

	pdf.add_cards(
		# images
		[
			"samples/carbrand.jpg",
		],
		# terms
		[
		])

	pdf.output('output/carbrands-example.pdf', 'F')

if __name__ == '__main__':
	main()

