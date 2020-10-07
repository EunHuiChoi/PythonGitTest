is_angry = True
stomach = list()

while is_angry:
    stomach.append('chocolate')

    if len(stomach) == 10:
        print('Happy!')
        break
    else:
        print('Try one more')
        continue