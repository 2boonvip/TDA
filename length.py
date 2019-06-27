import sys
import numpy as np

def main(argv):
    
    if (len(argv)) == 0:
        argv.append[""]
        print(len(argv))
    
        
    for i, v in enumerate(argv):
        print("argv[{0}]: {1}".format(i, v))
        
    if len(argv) == 1:
        argv.append(" ")
        
    for string in argv:
        if len(string) > 1000:
            print(len(string))
            print("入力文字数が1000文字を超えているのでプログラムを終了します")
            sys.exit(1)
            
    row = [argv[0][i] for i in range(len(argv[0]))]
    column = [argv[1][i] for i in range(len(argv[1]))]
    row.insert(0,"")
    column.insert(0,"")
    
    levenstein = np.zeros((len(row),len(column)))
    
    for i in range(len(row)):
        levenstein[i][0] = i
    for i in range(len(column)):
        levenstein[0][i] = i
        
    for i in range(1,len(argv[0])+1):
        for j in range(1,len(argv[1])+1):
            up = levenstein[i-1][j] + 1
            left = levenstein[i][j-1] + 1
            if argv[0][i-1] == argv[1][j-1]:
                up_left = levenstein[i-1][j-1]
            else:
                up_left = levenstein[i-1][j-1] + 1
            
            levenstein[i][j] = min(up,left,up_left)
            
    print(int(levenstein[-1][-1]))
    
        
    

if __name__ == '__main__':
    args = sys.argv
    
    main(sys.argv[1:])
