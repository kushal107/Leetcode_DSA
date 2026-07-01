def func(i):
    if i > 10:
        return
    
    print(i)
    func(i+1)
    return

func(1)