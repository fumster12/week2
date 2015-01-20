# solution_4.py
# by Funmi Dosunmu 1/20/15
# Syracuse sequence

def seq(x):
    x = eval(input("What is the starting number?: "))
    seq = [x]
    if x % 2 == 0: 
        x = (x / 2)
    else:
        x = (3 * x + 1) 
    return seq

              
seq()

