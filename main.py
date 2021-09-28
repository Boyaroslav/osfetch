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
        '     `--       `--/ '],
    'Kali' : [
        ' ~~____..',
        '       ```0',
        '  ``----==-0',
        '       ;/--=00000',
        '---------===00000000',
        '              ;////000o',
        '             ;///000ooooooo/_\ ',
        '           ;///         \ ____/===',
        '            ;///',
        '               ;/////',
        '                  /////',
        '                      \***\  ',
        '                     //   //',
        '                      //    //',
        '                        //   //']
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
        if self.name=='time':
            self.printage=list(self.printage.split())[0]
            print(self.name,"=",self.printage)
        if self.name=='architecture':
            print(self.name,"=",self.printage[:-1])
time=thing("uptime","time")
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
try:
    osname.watch()
except:
    osname=thing('uname -r','OS')
    osname.watch()
processor.watch()
