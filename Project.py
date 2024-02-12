from tkinter import*
from tkinter import ttk
import csv

filepath = 'History_Bk.csv'
filepath2 = 'Daily summary.csv'

clearr=()
def process_1():

    try:
        Code_bk =  bicycle_code2.get()
        in_time_bk = time_in.get()
    except Exception as e:
        errorcall = Label(mywin,text="โปรดระบุให้ถูกต้อง",font="Tomaho 13 bold",fg="red")
        errorcall.grid(row=11,column=1,pady=10)

    information = ['รหัสจักรยาน: {}'.format(Code_bk),
                   'เวลาที่ยืม: {} นาฬิกา.'.format(in_time_bk)]

    with open(filepath,'a',encoding='utf-8')as outfile:
        writer=csv.writer(outfile)
        writer.writerow(information)   

def show_result():
    
    show_result = Tk()
    show_result.minsize(300,300)
    show_result.title('คิดเป็นเงิน')

    try:
        cal_in_time = time_in2.get()
        cal_out_time = time_back.get()
        Code = bicycle_code3.get()

    except Exception as e:
        errorcall = Label(mywin,text="โปรดระบุให้ถูกต้อง",font="Tomaho 13 bold",fg="red")
        errorcall.grid(row=11,column=1,pady=10)
        show_result.destroy()
        
    def price():

        cal_in_time = time_in2.get()
        cal_out_time = time_back.get()
        cal_in_hr = int(cal_in_time[0:2])
        cal_in_mn = int(cal_in_time[3:5])
        cal_out_hr = int(cal_out_time[0:2])
        cal_out_mn = int(cal_out_time[3:5])
        cal_out = (cal_out_hr * 60 + cal_out_mn)
        cal_in = (cal_in_hr * 60 + cal_in_mn)
        total = cal_out - cal_in
         
        if (total) % 60 == 0:
            hr = total // 60
        else:
            hr = total // 60+1

        loop = True
        while loop:
            if hr >= 3:
                total_parking = (50+(hr-3)*10)
            elif hr == 2:
                total_parking = (hr-1)*30
            else:
                total_parking = (hr*10)

            return total_parking
    try:
        information2 = ['Code:{}'.format(Code),
                        'In:{} '.format(cal_in_time),
                        'Out:{} '.format(cal_out_time),
                        '{}'.format(price())]

        with open(filepath2,'a',encoding ='utf-8') as outfile:
            writer = csv.writer(outfile,lineterminator ='\n')
            writer.writerow(information2)

    except Exception as e:
        errorcall = Label(mywin,text="โปรดระบุให้ถูกต้อง",font="Tomaho 13 bold",fg="red")
        errorcall.grid(row=11,column=1,pady=10)
        show_result.destroy()

    try:
        show_result1 = Label(show_result,text = "สรุปผล",width = 40,font="Tomaho 10 bold",bg = "#FF9966")
        show_result1.grid(row=0,column=3,pady=10)
    except Exception as e:
        print('error head')

    try:
        show_bk_code = Label(show_result,text = "รหัสจักรยาน : {}".format(Code),width = 20 ,font="Tomaho 10 bold")
        show_bk_code.grid(row=1,column=3,pady=10)
    except Exception as e:
        print('error Code')

    try:
        show_bk_in = Label(show_result,text = "เวลาที่ยืม : {} นาฬิกา".format(cal_in_time),width = 20 ,font="Tomaho 10 bold")
        show_bk_in.grid(row=2,column=3,pady=10)
    except Exception as e:
        print('error in_time')
        
    try:
        show_bk_out = Label(show_result,text = "เวลาที่คืน : {} นาฬิกา".format(cal_out_time),width = 20 ,font="Tomaho 10 bold")
        show_bk_out.grid(row=3,column=3,pady=10)
    except Exception as e:
        print('error out_time')
    
    try:
        show_bk_result = Label(show_result,text = "คิดเป็นเงิน : {} บาท".format(price()),width = 20 ,font="Tomaho 10 bold")
        show_bk_result.grid(row=5,column=3,pady=10)
    except Exception as e:
        errorcall = Label(mywin,text="โปรดระบุให้ถูกต้อง",font="Tomaho 13 bold",fg="red")
        errorcall.grid(row=11,column=1,pady=10)
        show_result.destroy()

    bt_close = Button(show_result,text='Close',width=10,bg="#FF0000",command=show_result.destroy)
    bt_close.grid(row=7,column=3,pady=10)
          
def summary():  
    try:
        users=['Users']
        total=['Total']
        with open(filepath2,'r',encoding ='utf-8') as infile:
            read = csv.reader(infile)
            list_ = list(read)
            sum_price=0
        for loop in list_:
            sum_price += eval(loop[3])
            len_users=0
        for loop in list_:
            len_users += len([0])

        users.append(len_users)
        total.append(sum_price)
        with open(filepath2,'a',encoding ='utf-8')as outfile:
            writer = csv.writer(outfile,lineterminator ='\n')
            writer.writerow(users)
            writer.writerow(total)
            
    except Exception as e:
        errorcall = Label(mywin,text="โปรดระบุให้ถูกต้อง",font="Tomaho 13 bold",fg="red")
        errorcall.grid(row=11,column=1,pady=10)


def Clear():
    with open(filepath,"w",encoding='utf-8')as clfile:
        clear_f = csv.writer(clfile)
        clear_f.writerow(clearr)

        
def history():
    callhistory = Tk()
    callhistory.minsize(500,300)
    callhistory.title('history')

    with open(filepath,"r",encoding='utf-8')as calluser:
        usercall = csv.reader(calluser)
        alldata = list(usercall)

    for i in alldata:
        park_history = Label(callhistory,text=i,font='Tahoma 15 bold')
        park_history.grid()

   

mywin = Tk()
mywin.title("โปรแกรมคำนวณค่ายืมรถจักรยาน ณ สวนสาธารณะ")
mywin.minsize(450,480)

try:
    bicycle_code = StringVar()
    bicycle_code2 = StringVar(value="เลือกจักรยาน")
    bicycle_code3 = StringVar(value="เลือกจักรยาน")
    time_in = DoubleVar()
    time_in2 = StringVar()
    time_back = StringVar()
except Exception as e:
        errorcall = Label(mywin,text="โปรดระบุให้ถูกต้อง",font="Tomaho 13 bold",fg="red")
        errorcall.grid(row=11,column=1,pady=10)
        show_result.destroy()
        

head = Label(mywin,text="จักรยาน at park",font="Tahoma 10 bold",
             bg = "#FF9966")
head.grid(row=0,column=1,pady=20)

head_2 = Label(mywin,text="ยืมจักรยาน",font="Tahoma 10 bold",
             bg = "#FF9966")
head_2.grid(row=1,column=0)

Ab = Label(mywin,text = "รหัสจักรยาน",width = 20 ,font="Tomaho 10 bold")
Ab.grid(row=2,column=0,pady=10)

inp = ttk.Combobox(textvariable=bicycle_code2)
inp["values"] = ("A00","A01","A02","A03","A04","A05","A06","A07","A08","A09")
inp.grid(row=2,column=2)

Ac = Label(mywin,text = "เวลาที่ยืม : (xx.xx)",width = 20 ,font="Tomaho 10 bold")
Ac.grid(row=3,column=0)

itimein = Entry(mywin,textvariable=time_in,width=20)
itimein.grid(row=3,column=2,sticky=W)
itimein.focus()

btOK = Button(mywin,text="OK",width=10,bg="#66FF66",
          command=process_1)
btOK.grid(row=4,column=1,pady=10)

bt = Button(mywin,text='ประวัติการยืม',width=10,bg="#00AB84",
      command=history)
bt.grid(row=4,column=2,pady=10)

clear_his = Button(mywin,text ='Clear History',width =10,command=Clear,bg="#00AB84")
clear_his.grid(row=5,column=2,pady=10)

head_3 = Label(mywin,text="คืนจักรยาน",font="Tahoma 10 bold",
             bg = "#FF9966")
head_3.grid(row=6,column=0)

Ad = Label(mywin,text = "รหัสจักรยาน",width = 20 ,font="Tomaho 10 bold")
Ad.grid(row=7,column=0,pady=10)

inp_1 = ttk.Combobox(textvariable=bicycle_code3)
inp_1["values"] = ("A00","A01","A02","A03","A04","A05","A06","A07","A08","A09")
inp_1.grid(row=7,column=2)


Ae = Label(mywin,text = "เวลาที่ยืม : (xx.xx)",width = 20 ,font="Tomaho 10 bold")
Ae.grid(row=8,column=0)

timein = Entry(mywin,textvariable=time_in2,width=20)
timein.grid(row=8,column=2,sticky=W)
timein.focus()

Af = Label(mywin,text = "เวลาที่คืน : (xx.xx)",width = 20 ,font="Tomaho 10 bold")
Af.grid(row=9,column=0,pady=10)

timeback = Entry(mywin,textvariable=time_back,width=20)
timeback.grid(row=9,column=2,sticky=W)
timeback.focus()

btOK = Button(mywin,text="OK",width=10,bg="#66FF66",command=show_result)
btOK.grid(row=10,column=1,pady=10)

bt_finish = Button(mywin,text='สรุปยอดรายวัน',width=10,bg="#FFDEAD",command=summary)
bt_finish.grid(row=11,column=0,pady=10)


bt = Button(mywin,text='Close',width=10,bg="#FF0000",command=mywin.destroy)
bt.grid(row=10,column=2,pady=10)

mywin.mainloop()
