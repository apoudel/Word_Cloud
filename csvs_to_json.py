# csvs_to_json.py

from count_words import txt_to_csv

def make_SOTU_CSVs():
    for year in range(2001,2017):
        filename = "SOTU-textfiles/" + str(year) + ".txt"
        txt_to_csv(filename, year)

# def aggregate_CSVs():
#     for year in range(2001,2017):
#         filename = "SOTU-csv/" + str(year) + ".csv"
#         print(filename)

if __name__ == '__main__':
    make_SOTU_CSVs()
