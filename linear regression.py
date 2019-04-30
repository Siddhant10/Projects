from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

        

def coefficient(xs,ys):
    n=np.size(xs)
    
    print("LENGTH OF X",n)
    
    
    m_x=mean(xs)
    m_y=mean(ys)
    print("MEAN OF X",m_x)
    print("MEAN OF Y",m_y)
    
    dev_y=((mean(xs)*mean(ys)) - mean(xs*ys))
    dev_x=((mean(xs)*mean(xs)) - mean(xs*xs))
   

    m=dev_y/dev_x
    b=mean(ys) - m*mean(xs)
    print("Slope",m)
    print("Intercept",b)
    
    return(m,b)

    




def MSE(x,y):
    
    print("Mean Square Error",np.square(np.subtract(x, y)).mean())
      
    n=np.size(x)
    
    
    
    
    m_x=mean(x)
    m_y=mean(y)
    
    dev_y=((mean(x)*mean(y)) - mean(x*y))
    dev_x=((mean(x)*mean(x)) - mean(x*x))
    
    m=dev_y/dev_x
    b=mean(y) - m*mean(x)
    
    rmse = 0
    for i in range(n):
        y_target = b + m * x[i]
        rmse += (y[i] - y_target) ** 2
    rmse = np.sqrt(rmse/n)
    print("RMSE",rmse)


    # Calculating R2 Score
    ss_tot = 0
    ss_res = 0
    for i in range(n):
        y_target = b + m * x[i]
        ss_tot += (y[i] - m_y) ** 2
        ss_res += (y[i] - y_target) ** 2
    r2 = 1 - (ss_res/ss_tot)
    print("R2 Score")
    print(r2)

def regression_line(x,y,e):
    y_target=e[0]+e[1]*x
    plt.plot(x, y_target, color='#58b970', label='Regression Line')
    plt.scatter(x,y, color='#ef5423', label='Scatter Plot')

    plt.xlabel('Independent variable')
    plt.ylabel('Depeendent variable')
    plt.legend()
    plt.show()
    
  





          

def main():

        xs = np.array([0,1,2,3,4,5,6,7,8,9])
        ys = np.array([1,2,3,6,5,8,4,7,2,8])
   

        e = coefficient(xs, ys)
        print("Estimated coefficients:\nb_0 = {} \
            \nb_1 = {}".format(e[0], e[1]))

	# plotting regression line
        MSE(xs,ys)
        
        
       
        regression_line(xs, ys, e)

 
    

if __name__ == "__main__":
        main()
