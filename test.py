
from turtle import color
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from matplotlib.pyplot import text
import numpy as np
from scipy.stats import norm

red=(0.839, 0.0588, 0.0588, 1)

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols=1
        self.top_grid=GridLayout()
        self.top_grid.cols=2
        self.add_widget(Label(text="BLACK SCHOLES ALGORITHM", font_size=28, bold=True))

        
        self.top_grid.add_widget(Label(text="RATE OF INTEREST", italic=True, bold=True))
        self.r=TextInput(multiline=False)
        self.top_grid.add_widget(self.r)

        self.top_grid.add_widget(Label(text="SPOT PRICE",italic=True, bold=True))
        self.S=TextInput(multiline=False)
        self.top_grid.add_widget(self.S)

        self.top_grid.add_widget(Label(text="STRIKE PRICE",italic=True, bold=True))
        self.K=TextInput(multiline=False)
        self.top_grid.add_widget(self.K)

        self.top_grid.add_widget(Label(text="EXPIRATION TIME",italic=True, bold=True))
        self.T=TextInput(multiline=False)
        self.top_grid.add_widget(self.T)

        self.top_grid.add_widget(Label(text="VOLATILITY",italic=True, bold=True))
        self.sigma=TextInput(multiline=False)
        self.top_grid.add_widget(self.sigma)

        self.top_grid.add_widget(Label(text="CALL OR PUT [enter c/p]",italic=True, bold=True))
        self.option=TextInput(multiline=False)
        self.top_grid.add_widget(self.option)

        self.add_widget(self.top_grid)

        self.calculate=Button(text="CALCULATE", font_size=32, background_color=red, bold=True)
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
         
        
        
        self.add_widget(Label(text='Price of the option is \n ' +str(black_scholes(r,S,K,T,sigma,option))+ '\n<sinwin out>'))
        
        

class GayPay(App):
    def build(self):
        return MyGridLayout()
if __name__=='__main__':
    GayPay().run()
