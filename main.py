import os

asciis={
    'ManjaroLinux' : ['00000000 000','000 0000 000','000 0000 000','000 0000 000','000 0000 000','000 0000 000'],
    'Ubuntu' : [
        '       000',
        '   ----0000',
        ' --      --',
        '-00        --',
        '0000        --',
        ' 000       --',
        '  --     000',
        '    ----0000',
        '        000,'],
    'Linux' : [
        '         _nnnn_',
        '        dGGGGMMb',
        '       @p~qp~~qMb',
        '       M|@||@) M|',
        '       @,----.JM|',
        '      JS^\__/  qKL',
        '     dZP        qKRb',
        '    dZP          qKKb',
        '   fZP            SMMb',
        '   HZM            MMMM',
        '   FqM            MMMM',
        ' __| ".        |\dS"qML',
        ' |    `.       | `/ Zq',
        '_)      \.___.,|     .',
        '\____   )MMMMMP|   ./',
        '     `--       `--/ ']
}

class thing:
    def __init__(self,x,name):
        self.x=x
        self.name=name
        self.printage=os.popen(self.x).read()
    def watch(self):
        if self.name=='os':
            self.printage=list(self.printage.split())[-1]
            print(self.name,"=",self.printage)
        else:
            print(self.name,"=",self.printage[:-1])
time=thing("uptime -s","time")
osname=thing('lsb_release -i','os')
processor=thing('uname -m','architecture')



try:
    x=asciis[list(osname.printage.split())[-1]]
except:
    x=asciis['Linux']

for i in x:
        print(i)


for j in range(2):print()
time.watch()
osname.watch()
processor.watch()
