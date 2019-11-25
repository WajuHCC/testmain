import sys
input_file = sys.argv[1]
output_file = sys.argv[2]

def czysc(input_file, output_file):
    lista=[]
    with open("dane/" + input_file) as f:
        for email in f:
            if email.count("@") == 1 and email not in lista:
                lista.append(email.lower())
        lista.sort()
    with open("wyniki/" + output_file, 'w') as g:
        for email in lista:
            g.write(email + "\n")

czysc(input_file, output_file)



