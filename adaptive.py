def adapttrape(f,N,a,b,accuracy,pnt):    
    def trape(step):
        h = (b-a)/step
        sum = (f(a)+f(b))/2.*h
        for i in range(1,step):
            sum += f(a+i*h)*h
        return sum
    
    def Si(step):
        sum = 0.
        h = (b-a)/step
        for i in range(1,step,2):
            sum += f(a+i*h)*h
        return sum
    
    step = N
    trape_sum_old = trape(step)
    if(pnt > 0):
        print(step,trape_sum_old)
    error = 1.
    
    while (error>accuracy):
        step = step*2
        trape_sum = trape_sum_old/2. + Si(step)
        error = abs(trape_sum - trape_sum_old)/3.
        if(pnt > 0):
            print(step, trape_sum_old,error)
        trape_sum_old = trape_sum

    return trape_sum


def adaptsimp(f,N,a,b,accuracy,pnt):
    def Si2(step):
        sum = f(a) + f(b)
        h = (b-a)/step
        
        for i in range(2,step-1,2):
            sum += 2*f(a+i*h)
        return sum/3
    
    def Ti2(step):
        sum = 0.
        h = (b-a)/step
        for i in range(1,step,2):
            sum += f(a+i*h)
        return sum*2/3

    step = N
    h = (b-a)/step
    si2_sum_old = Si2(step)
    ti2_sum_old = Ti2(step)
    simp_sum_old = h*(si2_sum_old+2*ti2_sum_old)
    if(pnt > 0):
        print(step, simp_sum_old)
    error = 1.

    while (error>accuracy):
        step = step*2
        h = (b-a)/step
        si2_sum = si2_sum_old + ti2_sum_old
        ti2_sum = Ti2(step)
        simp_sum = h*(si2_sum+2*ti2_sum)
        error = abs(simp_sum - simp_sum_old)/15
        if(pnt > 0):
            print (step, simp_sum, error)
        simp_sum_old = simp_sum
        si2_sum_old = si2_sum
        ti2_sum_old = ti2_sum

    return simp_sum