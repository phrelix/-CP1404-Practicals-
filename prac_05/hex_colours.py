hexColors = {'black' : '#000000', 'ghostwhite' : '#f8f8ff', 'gray' : '	#bebebe', 'red' : '#ff0000',
             'sienna' : '#a0522d', 'tan' : '#d2b48c', 'violet' : '#ee82ee', 'white' : '#ffffff',
             'blue' : '#0000ff', 'darkgreen' : '#006400'}
choice = input("Please enter a color, black, ghostwhite, gray, red, sienna, tan, violet, white, blue, darkgreen")
choice.islower()
if choice in hexColors:
    print (hexColors[choice])
