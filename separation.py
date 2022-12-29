import csv
class Separation:
    def __init__(self):
        self.file_name = input("Введите название файла: ")
        self.years = set()

    def sepCsv(self):
        with open(self.file_name, encoding='utf-8') as file:
            reader_csv = csv.reader(file)
            self.name = next(reader_csv)
            for row in reader_csv:
                fits = True
                if len(row) < len(self.name):
                    continue
                for check in row:
                    if len(check) == 0:
                        fits = False
                        break
                if fits:
                    year = row[-1][:4]
                    N_file = open(f'./csv_by_years/{year}.csv', 'a', encoding='utf-8')
                    with N_file:
                        writer = csv.writer(N_file, lineterminator="\r")
                        if year not in self.years:
                            self.years.add(year)
                            writer.writerow(self.name)
                            writer.writerow(row)
                        else:
                            writer.writerow(row)
                            print(year)


sep = Separation()
sep.sepCsv()