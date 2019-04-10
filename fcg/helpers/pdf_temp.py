import fpdf

class PDFFlashCard(fpdf.FPDF):
	"""docstring for PDFFlashCard"""
	__a4_l_w = 299 # milimet
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
		self.multi_cell(w, h, text)
		self.init_font()

class PDFCarBrand(PDFFlashCard):
	"""docstring for PDFCarBrand"""
	def __init__(self, orient, font, size, rows, cols, spacing):
		super(PDFCarBrand, self).__init__(orient, font, size, rows, cols, spacing)

	def add_cards(self, image_paths, terms_dict, border_all=True):
		self.front_page(image_paths, border_all)
		self.back_page(terms_dict, border_all)

	def front_page(self, image_paths, border_all):
		self.add_page()
		if border_all:
			self.border_all()

		row = 1
		col = 1
		for img in image_paths:
			self.put_image(row, col, img)
			if col == self.cols:
				row += 1
				col = 1
			else:
				col += 1

	def back_page(self, terms_dict, border_all):
		pass


def main():
	pdf = PDFCarBrand("P", "Arial", 14, 3, 2, 2)
	pdf.init_font()

	pdf.add_cards(
		# images
		[
			"samples/carbrand.jpg",
		],
		# terms
		[
		])

	pdf.add_cards(
		# images
		[
			"samples/carbrand.jpg",
		],
		# terms
		[
		])

	pdf.output('output/carbrand.pdf', 'F')

if __name__ == '__main__':
	main()

