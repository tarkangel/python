def breaker():
    for counter in range(10000):   
        if counter % 2 != 0:
            continue
        print(counter) 
        if counter == 5678:
            break

if __name__ == '__main__':
    breaker()