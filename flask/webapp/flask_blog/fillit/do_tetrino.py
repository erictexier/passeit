import tempfile
import random
import math
import time
import datetime

try:
    import tetrino
except Exception as e:
    class TetrinoDump:
        @staticmethod 
        def resolve(cmd):
            return "TETRINO NOT    ACCESSIBLE UNDER CONSTRUCTION ..:)..."
    tetrino = TetrinoDump()


tshape = [0xf000,
        0xe200,
        0xe400,
        0xe800,
        0xcc00,
        0xc600,
        0xc440,
        0xc880,
        0x8E00,
        0x8c80,
        0x8c40,
        0x88c0,
        0x8888,
        0x6c00,
        0x4E00,
        0x4C80,
        0x44C0,
        0x4C40,
        0x2E00]

charline = ["....", "...#", "..#.", "..##",
            ".#..", ".#.#", ".##.", ".###",
            "#...", "#..#", "#.#.", "#.##",
            "##..", "##.#", "###.","####"]

class Tetrino(object):
    def __init__(self):
        self.data = []
        self.result = []

    def do_play(self):
        ''' run tetrino module and save in temp area
        '''
        if len(self.data) < 1:
            return
        afile = tempfile.mkstemp(prefix = 'fillit-',suffix=datetime.datetime.utcnow().strftime("-%Y-%m-%d-%H-%M"))[1]
        tet = list()
        n = 65;
        with open(afile,"w") as f:
            for i in self.data:
                letters = list()
                for s in i:
                    f.write(s)
                    letters.append(s.replace("#","%c" % n))
                    f.write('\n')
                n += 1
                tet.append(letters)
                f.write('\n')
        self.data = tet
        start = time.time()
        result = tetrino.resolve(afile)
        self.delta = time.time() - start
        rep = len(result)
        self.sqa = int(math.sqrt(rep))
        self.stat = 0
        for x in result:
            if x == '.':
                self.stat += 1
        if rep > 0:
            self.stat = 100 - (self.stat * 100 / rep)
        self.result = list(map(lambda i: result[i:i+self.sqa], range(0,rep,self.sqa)))
        with open(afile,"a+") as out:
            out.write("grid:\n")
            out.write('{}\nsec:{}-{}%'.format('\n'.join(self.result), self.delta, self.stat))

    def show_in_line(self, col = 4):
        cdata = self.data[:]
        all = []
        line = []
        for i,d in enumerate(self.data):
            if i % col == 0:
                aline = []
                for j in range(col):
                    try:
                        x = cdata.pop(0)
                        aline.append(x)
                    except:
                        pass
                all.append(aline)

        all_line = ['Input:']
        for x in all:
            for i in range(4):
                aline = list()
                for xx in x:
                    aline.append(xx[i])
                all_line.append("   ".join(aline))
            all_line.append("-")
        all_line = all_line[:-1]
        return all_line

    def build_random(self, nb_tetrino):
        self.data = []
        for i in range(nb_tetrino):
            self.data.append(Tetrino.as_char(tshape[random.randint(0,18)]))

    @staticmethod
    def as_char(shape):
        res = list()
        l1 = charline[(shape & 0xf000) >> 12]
        l2 = charline[(shape & 0x0f00) >> 8]
        l3 = charline[(shape & 0x00f0) >> 4]
        l4 = charline[shape & 0x000f]
        return [l1,l2,l3,l4]

if __name__ == '__main__':
    t = Tetrino()
    t.build_random(14)
    t.do_play()
    t.print_result()