#!/usr/bin/python        


from project_euler_lib import discrete

def main():
    """Find the sum of even Fibonaccis under 4M."""
    result = sum([i for i in discrete.fib(4000000) if i % 2 == 0])
    
    # This is how you start the interactive debugger.
    # import code; code.interact(local=locals())
    print 'Result:', result


if __name__ == "__main__":
    main()
    