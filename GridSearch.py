from Dictionary import Dictionary

path = 'words.text'


def main():
    dictionary = Dictionary(path)
    inp = str(raw_input('enter the 4*4 grid'))
    grid = [inp[0:4], inp[4:8], inp[8:12], inp[12:16]]
    word = ''
    result = []
    i =0
    j=0
    dir = -1
    startX= 0
    startY=0
    while startX <= 3 and startY <= 3:
        letter = grid[i][j]
        word += letter
        if add_valid_word(dictionary, result, word):
            word =''
            if startX == 3:
                startY +=1
                startX = 0
            else:
                startX += 1
                ##startY = 0
            i = startY
            j = startX
            continue
        if dictionary.is_partial_match(word):
            if j == 3:
                if i == 3:
                    break
                else:
                    i += 1
                    dir = 1
            else:
                j += 1
                dir = 0
        else:
            word = word[:-1]
            if len(word) == 0 or dir ==-1:
                if startX == 3:
                    startY += 1
                    startX = 0
                else:
                    startX += 1
                    ##startY = 0
                i = startY
                j = startX
                continue
            if dir == 0:
                j += 1
                dir = 1
            else :
                if dir == 1:
                    i += 1
                    dir = -1

    print(startX)
    print(startY)








def add_valid_word(dictionary, result, word):
    if not word in result and dictionary.is_valid_word(word):
        result.append(word)
        return True


if __name__ == '__main__':
    main()