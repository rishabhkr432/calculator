from tkinter import *

def btnClick(numbers):
    global operator
    operator += str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator = ''
    text_input.set('')


def btnEquals():
    global operator
    sumup = str(eval(operator))    ## The eval() allows us to execute arbitrary strings as Python code. It accepts a source string and returns an object.
    text_input.set(sumup)
    operator=''

cal = Tk()
cal.title("Calculator")
operator = ''
text_input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg='grey', justify='right').grid(columnspan=4)

addition=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='+', command=lambda :btnClick('+')).grid(row=1, column=3)

btn9=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='9', command=lambda :btnClick(9)).grid(row=1, column=2)

btn8=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='8', command=lambda :btnClick(8)).grid(row=1, column=1)

btn7=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='7', command=lambda :btnClick(7)).grid(row=1, column=0)

#######################################-----Second row-----##########################################


subtraction=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='-', command=lambda :btnClick('-')).grid(row=2, column=3)

btn6=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='6', command=lambda :btnClick(6)).grid(row=2, column=2)

btn5=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='5', command=lambda :btnClick(5)).grid(row=2, column=1)

btn4=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='4', command=lambda :btnClick(4)).grid(row=2, column=0)
#######################################-----Third row--------##################################################

multiply=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='*', command=lambda :btnClick('*')).grid(row=3, column=3)

btn3=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='3', command=lambda :btnClick(3)).grid(row=3, column=2)

btn2=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='2', command=lambda :btnClick(2)).grid(row=3, column=1)

btn1=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='1', command=lambda :btnClick(1)).grid(row=3, column=0)

#######################################-----forth row--------##################################################

divide=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='/', command=lambda :btnClick('/')).grid(row=4, column=3)

btnequal=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='=', command=lambda :btnEquals()).grid(row=4, column=2)

btnclear=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='C', command=lambda :btnClear()).grid(row=4, column=1)

btn0=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'),
            text='0', command=lambda :btnClick(0)).grid(row=4, column=0)



cal.mainloop()