
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from matplotlib.pyplot import text
import numpy as np
from scipy.stats import norm

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols=2
        self.add_widget(Label(text="rate"))
        self.r=TextInput(multiline=False)
        self.add_widget(self.r)

        self.add_widget(Label(text="spot"))
        self.S=TextInput(multiline=False)
        self.add_widget(self.S)

        self.add_widget(Label(text="strike"))
        self.K=TextInput(multiline=False)
        self.add_widget(self.K)

        self.add_widget(Label(text="expiration"))
        self.T=TextInput(multiline=False)
        self.add_widget(self.T)

        self.add_widget(Label(text="volatility"))
        self.sigma=TextInput(multiline=False)
        self.add_widget(self.sigma)

        self.add_widget(Label(text="call or put"))
        self.option=TextInput(multiline=False)
        self.add_widget(self.option)

        self.calculate=Button(text="Calculate", font_size=32)
        self.calculate.bind(on_press=self.press)
        self.add_widget(self.calculate)
        
        
    def press(self, instance):
        r=float(self.r.text)
        S=float(self.S.text)
        K=float(self.K.text)
        T=float(self.T.text)
        sigma=float(self.sigma.text)
        option=self.option.text  
        def black_scholes(r, S, K, T, sigma, option):
            d1= (np.log(S/K)+ (r+sigma**2/2)*T)/(sigma*np.sqrt(T))
            d2=d1-sigma*np.sqrt(T)
            try:
                if option =='c':
                    price=S*norm.cdf(d1, 0, 1)- K*np.exp(-r*T)*norm.cdf(d2,0,1)
                elif option=='p':
                    price=K*np.exp(-r*T)*norm.cdf(-d2, 0, 1)-S*norm.cdf(-d1, 0, 1)
                return price
            except:
                print('enter all of the parameters accurately')
         
        
        
        self.add_widget(Label(text='Price of the option is ' +str(black_scholes(r,S,K,T,sigma,option))))
        
        

class GayPay(App):
    def build(self):
        return MyGridLayout()
if __name__=='__main__':
    GayPay().run()
