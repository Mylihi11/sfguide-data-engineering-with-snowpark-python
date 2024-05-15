import sys

income = 1000

def main(income: float) -> float:
    if float(income) <= 2000:
        tax = float(income) * 0.2
    elif float(income) <= 5000:
        tax = 2000 * 0.2 + (float(income) - 2000) * 0.3
    elif float(income) <= 10000:
        tax = 2000 * 0.2 + 3000 * 0.3 + (float(income) - 5000) * 0.4
    else:
        tax = 2000 * 0.2 + 3000 * 0.3 + 5000 * 0.4 + (float(income) - 10000) * 0.5
    return tax


#print(main(*sys.argv[1:]))



#if __name__ == '__main__':
 #   if len(sys.argv) > 1:
  #      print(main(*sys.argv[1:]))  # type: ignore
   # else:
    #    print(main())  # type: ignore

