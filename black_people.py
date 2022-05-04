import numpy as np
from scipy.stats import norm
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button

Builder.load_file('Myape.kv')

r=float(input("rate of interest on the option"))
S=float(input('spot price'))
K=float(input('strike price'))
T=float(input('expiration of the option'))
sigma=float(input('enter volatility'))
op_type=input('call or put [c/p]')


#5 input variables used in the equation

#6th variable is a choice for a put or a call option


def black_gurls(r, S, K, T, sigma, op_type):
    d1= (np.log(S/K)+ (r+sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2=d1-sigma*np.sqrt(T)
    try:
        if op_type=='c':
            price=S*norm.cdf(d1, 0, 1)- K*np.exp(-r*T)*norm.cdf(d2,0,1)
        elif op_type=='p':
            price=K*np.exp(-r*T)*norm.cdf(-d2, 0, 1)-S*norm.cdf(-d1, 0, 1)
        return price
    except:
        print('enter all of the parameters accurately')

print('Price of the option is', round(black_gurls(r,S,K,T,sigma,op_type), 3) )


class Myape(App):
    def build(self):
        return Builder.load_file('Myape.kv')
if __name__=='__main__':
    Myape().run()