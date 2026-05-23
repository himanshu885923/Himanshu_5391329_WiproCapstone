import openpyxl


class ExcelReader:

    def __init__(self, path):

        self.path = path

        self.workbook = openpyxl.load_workbook(path)

        self.sheet = self.workbook.active

    def get_row_values(self):

        row = []

        for cell in self.sheet[2]:
            row.append(cell.value)

        return row