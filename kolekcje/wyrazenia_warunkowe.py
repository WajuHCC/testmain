a = [1, 2, 3, 4]
if 1 in a:
    print("Jest")
    print("OK")
else:
    print("Ni ma")

print()

x,y=95,95
if x>100 and y>100:
    print("Jesteś poza planszą")
elif x>90 and x<=100 and y>=0 and y<10:
    print("Jesteś w PDR")
elif x>90 and x<=100 and y>90 and y<=100:
    print("Jesteś w PGR")
elif x>=0 and x<10 and y>90 and y<=100:
    print("Jesteś w LGR")
elif x>=0 and x<10 and y>=0 and y<=10:
    print("Jesteś w LDR")
elif x>=10 and x<=90 and y>=0 and y<10:
    print("Jesteś w DK")
elif x>=10 and x<=90 and y>=10 and y<90:
    print("Jesteś w GK")
elif x<=10 and