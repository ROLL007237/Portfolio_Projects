class MySet:
    def __init__(self,myset=None):
        for i,v in enumerate(myset):
            if myset.count(v) > 1:
                myset.remove(v)
        self.myset = myset
    def add(self, x):

        if not bool(self.myset):
            self.myset.append(x)

        if not (x in self.myset):
            if self.myset[0] > x:
                l = [x]
                self.myset = l+self.myset

            if self.myset[-1] < x:
                self.myset.append(x)
            else:
                for index in range(len(self.myset) - 1):
                    if self.myset[index] < x < self.myset[index + 1]:
                        fh = self.myset[:index + 1]
                        sh = self.myset[index + 1:]
                        fh.append(x)
                        self.myset=fh+sh
                        break

    def remove(self, x):
        if x in self.myset:
            self.myset.remove(x)

    def contains(self, x):
        if x in self.myset:
            return True
        else:
            return False

print(MySet([1,1,1,2,2,2,2,2]).myset)