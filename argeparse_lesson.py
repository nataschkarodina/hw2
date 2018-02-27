import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-k", type=float,
                    help="coordinate x1")
parser.add_argument("-l", type=float,
                    help="coordinate y1")
parser.add_argument("-n", type=float,
                    help="coordinate x2")
parser.add_argument("-m", type=float,
                    help="coordinate y2")
parser.add_argument("-t", type=float,
                    help="coordinate x3")
parser.add_argument("-f", type=float,
                    help="coordinate y3")
args = parser.parse_args()
a =((args.m-args.l)**2+(args.n-args.k)**2)**0.5
b =((args.f-args.l)**2+(args.t-args.k)**2)**0.5
c =((args.f-args.m)**2+(args.t-args.n)**2)**0.5
p =(a+b+c)/2
answer =(p*(p-a)*(p-b)*(p-c))**0.5
print ('The square is', answer)
#answer = (((((y2-y1)**2+(x2-x1)**2)**0.5)+(((y3-y1)**2+(x3-x1)**2)**0.5)+(((y3-y2)**2+(x3-x2)**2)**0.5))/2)*(((((y2-y1)**2+(x2-x1)**2)**0.5)+(((y3-y1)**2+(x3-x1)**2)**0.5)+(((y3-y2)**2+(x3-x2)**2)**0.5))/2)-(((y2-y1)**2+(x2-x1)**2)**0.5)*(((((y2-y1)**2+(x2-x1)**2)**0.5)+(((y3-y1)**2+(x3-x1)**2)**0.5)+(((y3-y2)**2+(x3-x2)**2)**0.5))/2)-(((y3-y1)**2+(x3-x1)**2)**0.5)*((((y2-y1)**2+(x2-x1)**2)**0.5+(((y3-y1)**2+(x3-x1)**2)**0.5)+(((y3-y2)**2+(x3-x2)**2)**0.5)/2)-(((y3-y2)**2+(x3-x2)**2)**0.5))**0.5

