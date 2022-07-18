def breaker():
    for counter in range(1000):   
        if counter % 2 != 0:
            continue
        print(counter) 
if __name__ == '__main__':
    breaker()