import tkinter as tk
import tkinter.messagebox
import bs4,time,requests
#from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from tkinter import *
class Page(tk.Frame):
    pass

class Page1(Page):
   '''def save(self):
       n=name.get()
       print(n)'''
   def __init__(self, *args, **kwargs):
       pass
       
       
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #label = tk.Label(self, text="This is page 2")
       frame1=tk.Frame(self,bg="lightblue",width=1200,height=700)
       frame1.pack()
       #bslabel=tk.Label(frame1, text="BSNL Bill Payment - ",font=("BOLD", 15),bg="lightblue")#,padx=200,pady=200)
       #bslabel.pack()
       #bslabel.place(x=50,y=60)
       def bsnlcall():
           browser=webdriver.Chrome('C:\DRIVERS\CHROMEDRIVER\chromedriver.exe')
           browser.get('https://portal2.bsnl.in/myportal/cfa.do')
           landline=browser.find_element_by_link_text('Landline')
           landline.click()
           #time.sleep(2)
           eleid=browser.find_element_by_id('phoneno')
           eleid.send_keys('4024022633')
           eleid=browser.find_element_by_id('emailid')
           eleid.send_keys('lakshma3@gmail.com')
           eleid=browser.find_element_by_id('contactno')
           eleid.send_keys('9393626333')
           print("CAPTCHA found. User action required")
           print("Enter CAPTCHA and press 'Submit'")
           time.sleep(10)
           print(browser.current_url)
           res=requests.get(browser.current_url)
           time.sleep(10)
           #print("Writing page source to a file...")
           src=browser.page_source
           billfile=open('billFile.html','w')
           billfile.write(src)
           billfile.close()
           #time.sleep(10)
           #print("Completed Write")
           billfile=open('billFile.html')
           billSoup=bs4.BeautifulSoup(billfile)
           amount=billSoup.select('h4')
           #print("Your bill for current month is: ",amount[0].getText())
           #choice=input("Do you want to pay now ? Enter Yes/No  ")
           answer2=tkinter.messagebox.askquestion("Your bill for current month is: "+amount[0].getText() +"\nDo you want to pay now ?")
           if(answer2=='yes'):
                eleid=browser.find_element_by_id('paynow-btn')
                eleid.click()
                time.sleep(20)
                browser.quit()
           else:
                browser.quit()
       photo=tk.PhotoImage(file="bsnl-logo3.png")
       #photo = photo.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
       #self.pw.pic = ImageTk.PhotoImage(photo)
       #scale_w = new_width/old_width
       #scale_h = new_height/old_height
       #photo.zoom(.01, .01)
       bsbutton=tk.Button(frame1,image=photo,command=bsnlcall,)#height=50,width=50,text="Click Here",font=("BOLD", 10))
       bsbutton.image=photo
       bsbutton.pack()#**button_opt)
       bsbutton.place(x=50,y=60)
       #elabel=tk.Label(frame1,text="Electricity Bill Payment - ",font=("BOLD", 15),bg="lightblue")
       #elabel.pack()
       #elabel.place(x=50,y=180)
       def electpay():
           def autofill():
            select=Select(browser.find_element_by_name('circle'))
            select.select_by_visible_text('RANGAREDDY')
            select=Select(browser.find_element_by_name('ero'))
            select.select_by_visible_text('SAROORNAGAR')
            eleid=browser.find_element_by_name('sno')
            eleid.send_keys('1574 15192')
            eleid=browser.find_element_by_name('makePayment')
            eleid.click()

           def pay():
            sub=browser.find_element_by_name("button2")
            sub.click()
            time.sleep(1)
            element=browser.find_element_by_id('cnumber')
            element.send_keys('4373-7820-1028-0000')
            select=Select(browser.find_element_by_name('expmon'))
            select.select_by_visible_text('05 (May)')
            select=Select(browser.find_element_by_name('expyr'))
            select.select_by_visible_text('2020')
            element=browser.find_element_by_id('cvv2')
            element.send_keys('684')
            element=browser.find_element_by_id('cname2')
            element.send_keys('LAKSHMA REDDY B')
           browser=webdriver.Chrome('C:\DRIVERS\CHROMEDRIVER\chromedriver.exe')
           browser.get('https://www.billdesk.com/APCPDCL/apcpdcl.htm')
           autofill()
           time.sleep(4)
           bill=browser.find_element_by_name("txtTxnAmount")
           amt=bill.get_attribute("value")
           #print('Your electricity bill for current month is ',amt)
           due=browser.find_element_by_name("due_date")
           date=due.get_attribute("value")
           #print('You should pay by: ',date)
           #ch=input("\nDo you want to proceed to payment? Y/N ")
           answer=tkinter.messagebox.askquestion("Details","Your electricity bill for current month is"+amt+"\nYou should pay by:"+date+"\nDo you want to proceed to payment?")
           if answer=='yes':
               pay()
               #print('Do you want to confirm payment of Rs.',amt,'? Y/N')
               answer=tkinter.messagebox.askquestion("Want to make payment?","Do you want to confirm payment of Rs."+amt+"?")
               #ch=input()
               if answer=='Y':
                   element=browser.find_element_by_id('proceedForm')
                   element.click()
               else:
                   time.sleep(2)
                   browser.quit()
                   #element=browser.find_element_by_link_text('Cancel')
                   #element.click()
    
           else:
                browser.quit()


       photo2=tk.PhotoImage(file="elec-logo.png")
       ebutton=tk.Button(frame1,image=photo2,command=electpay)#text="Click here",font=("ITALIC", 10)
       ebutton.image=photo2
       ebutton.pack()
       ebutton.place(x=250,y=60)
       
       #label.pack(side="top", fill="both", expand=True)
           

class Page3(Page):
  pass

class MainView(tk.Frame):
  pass

if __name__ == "__main__":
    root = tk.Tk()#.config(bg="lightblue")
    #root["bg"] = "lightblue"
    
    main = MainView(root)
    
    main.pack(side="top", fill="both", expand=True)
    #main.option_add("*background", "lightblue")
    root.title("Automating Bill Payments")
    #root.configure(background='lightblue')
    root.wm_geometry("400x400")
    root.mainloop()
