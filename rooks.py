# Filename: rooks.py
#
# Description: Implementation of the nrooks problem to be
# solved using the Glucose3 SAT solver.

import sys
from pysat.solvers import Glucose3

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 rooks.py n')
        return

    n = int(sys.argv[1])
    # Create a variable for each square on the board.
    val = 1
    output = {}
    gridVariables = dict()
    for r in range(n):
        for c in range(n):
            gridVariables[(r,c)] = val
            output[val] = (r,c)
            val += 1
    for d in gridVariables:
        print(d)
    phi = Glucose3()
  
    # Adding clauses below
    for r in range(n):
        phi.add_clause([1*gridVariables[r,c] for c in range(n)])

    for r in range(n):
        v = n
        for c in range(n):
            for i in range(1,v):
                # Checking columns
                phi.add_clause([-1*gridVariables[r,c], -1*gridVariables[r,c+i]])

                # Checking rows
                phi.add_clause([-1*gridVariables[c,r], -1*gridVariables[c+i,r]])
            v = v -1
    

    phi.solve()
    m = phi.get_model()
    print (m)
    print("Solution:")
    for r in range(n):
        for c in range(n):
            if(gridVariables[(r,c)] in m):
                print("R",end="")
            else:
                print(".",end="")
        print()
    print()

    count = 0
    for s in phi.enum_models():
        count +=1
    print("Total number of models: %d" %(count))


if __name__ == "__main__":
    main()

