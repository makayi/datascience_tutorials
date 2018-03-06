from numpy import  *


def compute_error_for_given_point(b,m,points):
    totalError=0
    for i in range(0,len(points)):
        x=points[i,0]
        y=[i,1]
        totalError+=(y-(m*x+b))**2
        return totalError/float(len(points))

def step_gradient(b_current,m_current,points,learning_rate):





def gradient_descent_runner(points,starting_b,starting_m,learning_rate,num_iterations):
    b=starting_b
    m=starting_m
    for i in range(num_iterations):
        b,m=step_gradient(b,m,array(points),learning_rate)
    return [b,m]

def run():
    points=genfromtxt('data.csv',default=',')

    #hyperparametres
    learning_rate=0.0001

    #y=mx+b slope formulae


    initial_b=0
    initial_m=0
    num_iterations=1000
    [b,m]=gradient_descent_runner(points,initial_b,initial_m,learning_rate,num_iterations)
    print(b)
    print(m)

run()

