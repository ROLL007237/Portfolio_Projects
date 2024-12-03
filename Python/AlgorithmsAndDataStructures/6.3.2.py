from sortedcontainers import SortedDict

records = [['21413', 321], ['1231', 312], ['12412', 133], ['1231', 4213]]
sortedrecords = SortedDict()

for i in records:
    if not (i[0] in sortedrecords.keys()):
        sortedrecords[i[0]] = i[1]


class StockPrice:
    def __init__(self, records: SortedDict):
        for i in records:
            if not (i[0] in sortedrecords.keys()):
                sortedrecords[i[0]] = i[1]
        self.timestamps = sortedrecords.keys()
        self.prices = sortedrecords.values()
        self.srecords = sortedrecords
        self.records = records

    def update(self,timestamp: int, price: int) -> None:
        self.srecords[timestamp] = price

    def current(self) -> int:
        self.srecords
    #def maximum(self) -> int:

    # def minimum(self) -> int:


s = StockPrice(sortedrecords)

