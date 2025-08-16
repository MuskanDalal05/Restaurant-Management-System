# database name Restaurant_Management
# table name orders

from tkinter import *
import mysql.connector
from tkinter import messagebox
import datetime

conn = mysql.connector.connect(
    user='root',
    password='12345',
    host='localhost',
    database='Restaurant_Management'
)


Paneer_tikka_price = Veg_Seekh_Kabab_price = malai_chaap_price = cheese_balls_price = paneer_Kabab_price = cheese_chilli_price = Cheesy_garlic_bread_price = Potato_Twister_price = Chana_chaat_price = Crispy_corn_price = Cream_Salad_price = Veg_Cutlet_price = Potato_Lollipop_price = Veg_Noodle_price = Spring_Roll_price = Soya_veg_cutlet_price = 0

Paneer_tikka_quantity = Veg_Seekh_Kabab_quantity = malai_chaap_quantity = cheese_balls_quantity = paneer_Kabab_quantity = cheese_chilli_quantity = Cheesy_garlic_bread_quantity = Potato_Twister_quantity = Chana_chaat_quantity = Crispy_corn_quantity = Cream_Salad_quantity = Veg_Cutlet_quantity = Potato_Lollipop_quantity = Veg_Noodle_quantity = Spring_Roll_quantity = Soya_veg_cutlet_quantity = 0

Zira_Rice_price = Veg_Schezwan_Fried_Rice_price = Dal_Makhani_price = Dal_Tadka_price = Panner_Butter_Masala_price = Palak_Panner_price = Palak_Corn_price = Malai_Kofta_price = Kadhi_Pakora_price = Chana_Masala_price = Mushroom_Do_Pyaza_price = Mixed_Fruit_Raita_price = Pineapple_Raita_price = Curd_price = Butter_Naan_price = Butter_Roti_price = Lacha_Paratha_price = 0

Zira_Rice_quantity = Veg_Schezwan_Fried_Rice_quantity = Dal_Makhani_quantity = Dal_Tadka_quantity = Panner_Butter_Masala_quantity = Palak_Panner_quantity = Palak_Corn_quantity = Malai_Kofta_quantity = Kadhi_Pakora_quantity = Chana_Masala_quantity = Mushroom_Do_Pyaza_quantity = Mixed_Fruit_Raita_quantity = Pineapple_Raita_quantity = Curd_quantity = Butter_Naan_quantity = Butter_Roti_quantity = Lacha_Paratha_quantity = 0 

Kheer_price = Badam_Halwa_price = Moong_Dal_Halwa_price = Rasmalai_price = Rasgulla_price = Pineapple_Kesari_price = Fruit_Custard_price = Rabdi_with_Jalebi_price = Gulab_Jamun_price = Choco_lava_Cake_price = Brownie_with_Ice_Cream_price = Milk_badam_price = Fruit_Cream_price = Caramel_Bread_Pudding_price = Butterscotch_Ice_Cream_price = Choco_Brownie_Ice_Cream_price = Cold_Coffee_price = 0

Kheer_quantity = Badam_Halwa_quantity = Moong_Dal_Halwa_quantity = Rasmalai_quantity = Rasgulla_quantity = Pineapple_Kesari_quantity = Fruit_Custard_quantity = Rabdi_with_Jalebi_quantity = Gulab_Jamun_quantity = Choco_lava_Cake_quantity = Brownie_with_Ice_Cream_quantity = Milk_badam_quantity = Fruit_Cream_quantity = Caramel_Bread_Pudding_quantity = Butterscotch_Ice_Cream_quantity = Choco_Brownie_Ice_Cream_quantity = Cold_Coffee_quantity = 0

Starters_total_bill = 0
Main_Course_total_bill = 0
Dessert_total_bill = 0


if (conn.is_connected):
    cursor = conn.cursor()

    window = Tk()
    width = 450
    height = 250
    system_width = window.winfo_screenwidth()
    system_height=window.winfo_screenheight()
    window.config(bg="beige")

    c_x = int(system_width/2-width/2)
    c_y = int(system_height/2-height/2)


    window.geometry(f"{width}x{height}+{c_x}+{c_y}")
    window.maxsize(width, height)
    window.minsize(width, height)
    window.title("Restaurant Management")

    # starters variable
    starters_rd_var = StringVar()
    Starters_quantity_var = IntVar(value='')
    Starters_semi_bill_var = IntVar(value='')
    Starters_total_bill_var = IntVar(value='')

    # main course variable
    main_course_rd_var = StringVar()
    Main_Course_quantity_var = IntVar(value='')
    Main_Course_semi_bill_var = IntVar(value='')
    Main_Course_total_bill_var = IntVar(value='')

    # Dessert variable
    Dessert_rd_var = StringVar()
    Dessert_quantity_var = IntVar(value='')
    Dessert_semi_bill_var = IntVar(value='')
    Dessert_total_bill_var = IntVar(value='')

    # checkout variable
    checkout_customer_name_var = StringVar()
    checkout_customer_mobile_number_var = IntVar(value='')
    checkout_starters_total_amount_var = IntVar(value='')
    checkout_main_course_total_amount_var = IntVar(value='')
    checkout_dessert_total_amount_var = IntVar(value='')
    checkout_grand_total_var = IntVar(value='')

    def Menu_win():

        def starters():

            def starters_semi_bill():
                global Paneer_tikka_price, Veg_Seekh_Kabab_price, malai_chaap_price, cheese_balls_price, paneer_Kabab_price, cheese_chilli_price, Cheesy_garlic_bread_price, Potato_Twister_price, Chana_chaat_price, Crispy_corn_price, Cream_Salad_price, Veg_Cutlet_price, Potato_Lollipop_price, Veg_Noodle_price, Spring_Roll_price, Soya_veg_cutlet_price

                global Paneer_tikka_quantity, Veg_Seekh_Kabab_quantity, malai_chaap_quantity, cheese_balls_quantity, paneer_Kabab_quantity, cheese_chilli_quantity, Cheesy_garlic_bread_quantity, Potato_Twister_quantity, Chana_chaat_quantity, Crispy_corn_quantity, Cream_Salad_quantity, Veg_Cutlet_quantity, Potato_Lollipop_quantity, Veg_Noodle_quantity, Spring_Roll_quantity, Soya_veg_cutlet_quantity

                global Starters_total_bill

                # starters radio button
                starters_rd = starters_rd_var.get()
                Starters_quantity = Starters_quantity_var.get()

                if (starters_rd == "Paneer tikka"):
                    Paneer_tikka_price = 160
                    Paneer_tikka_quantity = Starters_quantity
                    Starters_semi_bill = Paneer_tikka_quantity * Paneer_tikka_price                   
                    Starters_semi_bill_var.set(Starters_semi_bill)            

                elif (starters_rd == "Veg Seekh Kabab"):
                    Veg_Seekh_Kabab_price = 140
                    Veg_Seekh_Kabab_quantity = Starters_quantity
                    Starters_semi_bill = Veg_Seekh_Kabab_quantity * Veg_Seekh_Kabab_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "malai Chaap"):
                    malai_chaap_price = 140
                    malai_chaap_quantity = Starters_quantity
                    Starters_semi_bill = malai_chaap_quantity * malai_chaap_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "Cheese Balls"):
                    cheese_balls_price = 190
                    cheese_balls_quantity = Starters_quantity
                    Starters_semi_bill = cheese_balls_quantity * cheese_balls_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "Paneer Kabab"):
                    paneer_Kabab_price = 170
                    paneer_Kabab_quantity = Starters_quantity
                    Starters_semi_bill = paneer_Kabab_quantity * paneer_Kabab_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "Cheese chilli"):
                    cheese_chilli_price = 210
                    cheese_chilli_quantity = Starters_quantity
                    Starters_semi_bill = cheese_chilli_quantity * cheese_chilli_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "Cheesy garlic bread"):
                    Cheesy_garlic_bread_price = 220
                    Cheesy_garlic_bread_quantity = Starters_quantity
                    Starters_semi_bill = Cheesy_garlic_bread_quantity * Cheesy_garlic_bread_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "Potato Twisters"):
                    Potato_Twister_price = 175
                    Potato_Twister_quantity = Starters_quantity
                    Starters_semi_bill = Potato_Twister_quantity * Potato_Twister_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "Chana chaat"):
                    Chana_chaat_price = 130
                    Chana_chaat_quantity = Starters_quantity
                    Starters_semi_bill = Chana_chaat_quantity * Chana_chaat_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "Crispy Corn"):
                    Crispy_corn_price = 150
                    Crispy_corn_quantity = Starters_quantity
                    Starters_semi_bill = Crispy_corn_quantity * Crispy_corn_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "Cream Salad"):
                    Cream_Salad_price = 170
                    Cream_Salad_quantity = Starters_quantity
                    Starters_semi_bill = Cream_Salad_quantity * Cream_Salad_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "Veg Cutlet"):
                    Veg_Cutlet_price = 150
                    Veg_Cutlet_quantity = Starters_quantity
                    Starters_semi_bill = Veg_Cutlet_quantity * Veg_Cutlet_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "Potato Lollipop"):
                    Potato_Lollipop_price = 190
                    Potato_Lollipop_quantity = Starters_quantity
                    Starters_semi_bill = Potato_Lollipop_quantity * Potato_Lollipop_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "Veg Noodle"):
                    Veg_Noodle_price = 160
                    Veg_Noodle_quantity = Starters_quantity
                    Starters_semi_bill = Veg_Noodle_quantity * Veg_Noodle_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "Spring Roll"):
                    Spring_Roll_price = 150
                    Spring_Roll_quantity =  Starters_quantity
                    Starters_semi_bill = Spring_Roll_quantity * Spring_Roll_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                elif (starters_rd == "Soya veg cutlet"):
                    Soya_veg_cutlet_price = 180
                    Soya_veg_cutlet_quantity = Starters_quantity
                    Starters_semi_bill = Soya_veg_cutlet_quantity * Soya_veg_cutlet_price
                    Starters_semi_bill_var.set(Starters_semi_bill)

                Starters_total_bill = Paneer_tikka_quantity * Paneer_tikka_price + Veg_Seekh_Kabab_quantity * Veg_Seekh_Kabab_price + malai_chaap_quantity * malai_chaap_price + cheese_balls_quantity * cheese_balls_price + paneer_Kabab_quantity * paneer_Kabab_price + cheese_chilli_quantity * cheese_chilli_price + Cheesy_garlic_bread_quantity * Cheesy_garlic_bread_price + Potato_Twister_quantity * Potato_Twister_price + Chana_chaat_quantity * Chana_chaat_price + Crispy_corn_quantity * Crispy_corn_price + Cream_Salad_quantity * Cream_Salad_price + Veg_Cutlet_quantity * Veg_Cutlet_price + Potato_Lollipop_quantity * Potato_Lollipop_price + Veg_Noodle_quantity * Veg_Noodle_price + Spring_Roll_quantity * Spring_Roll_price + Soya_veg_cutlet_quantity * Soya_veg_cutlet_price

            
            def starters_total_bill():
                
                global Starters_total_bill

                Starters_total_bill_var.set(Starters_total_bill)

            width = 1050
            height = 530
            Starters_Window = Toplevel()
            system_width = Starters_Window.winfo_screenwidth()
            system_height=Starters_Window.winfo_screenheight()

            c_x = int(system_width/2-width/2)
            c_y = int(system_height/2-height/2)


            Starters_Window.geometry(f"{width}x{height}+{c_x}+{c_y}")
            Starters_Window.maxsize(width, height)
            Starters_Window.minsize(width, height)
            Starters_Window.title("Restaurant Management Starters")
            Starters_Window.config(bg="#fdf5e2")

            def back_button():
                Starters_quantity_var.set(value='')
                Starters_semi_bill_var.set(value='')
                Starters_total_bill_var.set(value='')
                starters_rd_var.set(value='')
                Starters_Window.destroy()

            def on_closing():
                Starters_quantity_var.set(value='')
                Starters_semi_bill_var.set(value='')
                Starters_total_bill_var.set(value='')
                starters_rd_var.set(value='')
                Starters_Window.destroy()

            Starters_Window.wm_protocol("WM_DELETE_WINDOW", on_closing)

            # Starters label frame
            Starters_label_frame = Frame(Starters_Window,bg="#fdf5e2")
            Starters_label_frame.place(x=30, y=40)

            # Starters price frame
            Starters_price_frame = Frame(Starters_Window,bg="#fdf5e2")
            Starters_price_frame.place(x=230, y=40)

            # Starters main label
            Starter_main_label = Label(Starters_Window, text="Starters", font=("Helvetica", 12, "bold"),bg="#fdf5e2")
            Starter_main_label.pack()

            # Paneer tikka label
            Paneer_tikka_label = Label(Starters_label_frame, text="Paneer tikka", font=10 ,bg="#fdf5e2")
            Paneer_tikka_label.grid(row=0, column=0)

            # Veg Seekh Kabab label
            Veg_Seekh_Kabab_label = Label(Starters_label_frame, text="Veg Seekh Kabab", font=10 ,bg="#fdf5e2")
            Veg_Seekh_Kabab_label.grid(row=1, column=0)

            # malai chaap label
            malai_chaap_label = Label(Starters_label_frame, text="malai Chaap", font=10 ,bg="#fdf5e2")
            malai_chaap_label.grid(row=2, column=0)

            # cheese balls label
            cheese_balls_label = Label(Starters_label_frame, text="Cheese Balls", font=10 ,bg="#fdf5e2")
            cheese_balls_label.grid(row=3, column=0)

            # paneer Kabab label
            paneer_Kabab_label = Label(Starters_label_frame, text="Paneer Kabab", font=10 ,bg="#fdf5e2")
            paneer_Kabab_label.grid(row=4, column=0)

            # cheese chilli label
            cheese_chilli_label = Label(Starters_label_frame, text="Cheese chilli", font=10 ,bg="#fdf5e2")
            cheese_chilli_label.grid(row=5, column=0)

            # Cheesy garlic bread label
            Cheesy_garlic_bread_label = Label(Starters_label_frame, text="Cheesy garlic bread", font=10 ,bg="#fdf5e2")
            Cheesy_garlic_bread_label.grid(row=6, column=0)

            # Potato Twisters label
            Potato_Twisters_Label = Label(Starters_label_frame, text="Potato Twisters", font=10 ,bg="#fdf5e2")
            Potato_Twisters_Label.grid(row=7, column=0)

            # Chana chaat label
            Chana_chaat_label = Label(Starters_label_frame, text="Chana chaat", font=10 ,bg="#fdf5e2")
            Chana_chaat_label.grid(row=8, column=0)

            # crispy corn label
            Crispy_corn_Label = Label(Starters_label_frame, text="Crispy Corn", font=10, bg="#fdf5e2")
            Crispy_corn_Label.grid(row=9, column=0)

            # Cream salad Label
            Cream_salad_Label = Label(Starters_label_frame, text="Cream Salad", font=10, bg="#fdf5e2")
            Cream_salad_Label.grid(row=10, column=0)

            # veg Cutlet Label
            veg_Cutlet_Label = Label(Starters_label_frame, text="Veg Cutlet", font=10, bg="#fdf5e2")
            veg_Cutlet_Label.grid(row=11, column=0)

            # Potato lollipop Label
            Potato_lollipop_Label = Label(Starters_label_frame, text="Potato Lollipop", font=10, bg="#fdf5e2")
            Potato_lollipop_Label.grid(row=12, column=0)

            # Veg noodle Label
            Veg_noodle_Label = Label(Starters_label_frame, text="Veg Noodle", font=10, bg="#fdf5e2")
            Veg_noodle_Label.grid(row=13, column=0)

            # Spring Roll Label
            Spring_Roll_Label = Label(Starters_label_frame, text="Spring Roll", font=10, bg="#fdf5e2")
            Spring_Roll_Label.grid(row=14, column=0)

            # Soya veg cutlet Label
            Soya_veg_cutlet_Label = Label(Starters_label_frame, text="Soya veg cutlet", font=10, bg="#fdf5e2")
            Soya_veg_cutlet_Label.grid(row=15, column=0)

            # Paneer tikka price label
            Paneer_tikka_price_label = Label(Starters_price_frame, text="Rs 160", font=10, bg="#fdf5e2")
            Paneer_tikka_price_label.grid(row=0, column=0)

            # Veg Seekh Kabab price label
            Veg_Seekh_Kabab_price_label = Label(Starters_price_frame, text="Rs 140", font=10, bg="#fdf5e2")
            Veg_Seekh_Kabab_price_label.grid(row=1, column=0)

            # malai chaap price label
            malai_chaap_price_label = Label(Starters_price_frame, text="Rs 140", font=10, bg="#fdf5e2")
            malai_chaap_price_label.grid(row=2, column=0)

            # cheese balls price label
            cheese_balls_price_label = Label(Starters_price_frame, text="Rs 190", font=10, bg="#fdf5e2")
            cheese_balls_price_label.grid(row=3, column=0)

            # paneer Kabab price label
            paneer_Kabab_price_label = Label(Starters_price_frame, text="Rs 170", font=10, bg="#fdf5e2")
            paneer_Kabab_price_label.grid(row=4, column=0)

            # cheese chilli price label
            cheese_chilli_price_label = Label(Starters_price_frame, text="Rs 210", font=10, bg="#fdf5e2")
            cheese_chilli_price_label.grid(row=5, column=0)

            # Cheesy garlic bread price label
            Cheesy_garlic_bread_price_label = Label(Starters_price_frame, text="Rs 220", font=10, bg="#fdf5e2")
            Cheesy_garlic_bread_price_label.grid(row=6, column=0)

            # Potato Twisters price label
            Potato_Twisters_price_label = Label(Starters_price_frame, text="Rs 175", font=10, bg="#fdf5e2")
            Potato_Twisters_price_label.grid(row=7, column=0)

            # Chana chaat price label
            Chana_chaat_price_label = Label(Starters_price_frame, text="Rs 130", font=10, bg="#fdf5e2")
            Chana_chaat_price_label.grid(row=8, column=0)

            # crispy corn price label
            crispy_corn_price_label = Label(Starters_price_frame, text="Rs 150", font=10, bg="#fdf5e2")
            crispy_corn_price_label.grid(row=9, column=0)

            # Cream salad price Label
            Cream_salad_price_Label = Label(Starters_price_frame, text="Rs 170", font=10, bg="#fdf5e2")
            Cream_salad_price_Label.grid(row=10, column=0)

            # veg Cutlet price Label
            veg_Cutlet_price_Label = Label(Starters_price_frame, text="Rs 150", font=10, bg="#fdf5e2")
            veg_Cutlet_price_Label.grid(row=11, column=0)

            # Potato lollipop price Label
            Potato_lollipop_price_Label = Label(Starters_price_frame, text="Rs 190", font=10, bg="#fdf5e2")
            Potato_lollipop_price_Label.grid(row=12, column=0)

            # Veg noodle price Label
            Veg_noodle_price_Label = Label(Starters_price_frame, text="Rs 160", font=10,bg="#fdf5e2")
            Veg_noodle_price_Label.grid(row=13, column=0)

            # Spring Roll price Label
            Spring_Roll_price_Label = Label(Starters_price_frame, text="Rs 150", font=10,bg="#fdf5e2")
            Spring_Roll_price_Label.grid(row=14, column=0)

            # Soya veg cutlet price Label
            Soya_veg_cutlet_price_Label = Label(Starters_price_frame, text="Rs 180", font=10,bg="#fdf5e2")
            Soya_veg_cutlet_price_Label.grid(row=15, column=0)

            # Add Starters Label
            Add_Starters_Label = Label(Starters_Window, text="Add Starters", font=12,bg="#fdf5e2")
            Add_Starters_Label.place(x=430, y=45)

            # Starters Window radio button
            Starters_Window_radiobox1 = Radiobutton(Starters_Window, text="Paneer tikka", variable=starters_rd_var, value="Paneer tikka",bg="#fdf5e2")
            Starters_Window_radiobox1.place(x=360, y=80)
            Starters_Window_radiobox2 = Radiobutton(Starters_Window, text="Veg Seekh Kabab", variable=starters_rd_var, value="Veg Seekh Kabab",bg="#fdf5e2")
            Starters_Window_radiobox2.place(x=470, y=80)
            Starters_Window_radiobox3 = Radiobutton(Starters_Window, text="malai Chaap", variable=starters_rd_var, value="malai Chaap",bg="#fdf5e2")
            Starters_Window_radiobox3.place(x=360, y=110)
            Starters_Window_radiobox4 = Radiobutton(Starters_Window, text="Cheese Balls", variable=starters_rd_var, value="Cheese Balls",bg="#fdf5e2")
            Starters_Window_radiobox4.place(x=470, y=110)
            Starters_Window_radiobox5 = Radiobutton(Starters_Window, text="Paneer Kabab", variable=starters_rd_var, value="Paneer Kabab",bg="#fdf5e2")
            Starters_Window_radiobox5.place(x=360, y=140)
            Starters_Window_radiobox6 = Radiobutton(Starters_Window, text="Cheese chilli", variable=starters_rd_var, value="Cheese chilli",bg="#fdf5e2")
            Starters_Window_radiobox6.place(x=470, y=140)
            Starters_Window_radiobox7 = Radiobutton(Starters_Window, text="Cream Salad", variable=starters_rd_var, value="Cream Salad",bg="#fdf5e2")
            Starters_Window_radiobox7.place(x=360, y=170)
            Starters_Window_radiobox8 = Radiobutton(Starters_Window, text="Potato Twisters", variable=starters_rd_var, value="Potato Twisters",bg="#fdf5e2")
            Starters_Window_radiobox8.place(x=470, y=170)
            Starters_Window_radiobox9 = Radiobutton(Starters_Window, text="Chana chaat", variable=starters_rd_var, value="Chana chaat",bg="#fdf5e2")
            Starters_Window_radiobox9.place(x=360, y=200)
            Starters_Window_radiobox10 = Radiobutton(Starters_Window, text="Crispy Corn", variable=starters_rd_var, value="Crispy Corn",bg="#fdf5e2")
            Starters_Window_radiobox10.place(x=470, y=200)
            Starters_Window_radiobox11 = Radiobutton(Starters_Window, text="Cheesy garlic bread", variable=starters_rd_var, value="Cheesy garlic bread",bg="#fdf5e2")
            Starters_Window_radiobox11.place(x=360, y=230)
            Starters_Window_radiobox12 = Radiobutton(Starters_Window, text="Veg Cutlet", variable=starters_rd_var, value="Veg Cutlet",bg="#fdf5e2")
            Starters_Window_radiobox12.place(x=360, y=260)
            Starters_Window_radiobox13 = Radiobutton(Starters_Window, text="Potato Lollipop", variable=starters_rd_var, value="Potato Lollipop",bg="#fdf5e2")
            Starters_Window_radiobox13.place(x=470, y=260)
            Starters_Window_radiobox14 = Radiobutton(Starters_Window, text="Veg Noodle", variable=starters_rd_var, value="Veg Noodle",bg="#fdf5e2")
            Starters_Window_radiobox14.place(x=360, y=290)
            Starters_Window_radiobox15 = Radiobutton(Starters_Window, text="Spring Roll", variable=starters_rd_var, value="Spring Roll",bg="#fdf5e2")
            Starters_Window_radiobox15.place(x=470, y=290)
            Starters_Window_radiobox16 = Radiobutton(Starters_Window, text="Soya veg cutlet", variable=starters_rd_var, value="Soya veg cutlet",bg="#fdf5e2")
            Starters_Window_radiobox16.place(x=360, y=320)

            # Starters place your order label
            Starters_place_your_order_label = Label(Starters_Window, text="Place Your Order", font=12,bg="#fdf5e2")
            Starters_place_your_order_label.place(x=800, y=40)

            # Starters quantity label
            Starters_quantity_label = Label(Starters_Window, text="Quantity", font=8,bg="#fdf5e2")
            Starters_quantity_label.place(x=820, y=80)

            # Starters quantity input
            Starters_quantity_input = Entry(Starters_Window, width=25, textvariable=Starters_quantity_var)
            Starters_quantity_input.place(x=780, y=120)

            # Starters semi bill label
            Starters_semi_bill_label = Label(Starters_Window, text="Semi Bill", font=8,bg="#fdf5e2")
            Starters_semi_bill_label.place(x=820, y=160)

            # Starters semi bill input
            Starters_semi_bill_input = Entry(Starters_Window, width=25, textvariable=Starters_semi_bill_var)
            Starters_semi_bill_input.place(x=780, y=200)

            # Starters semi bill button
            Starters_semi_bill_button = Button(Starters_Window, text="Semi Bill", command=starters_semi_bill)
            Starters_semi_bill_button.place(x=830, y=240)

            # Starters total bill label
            Starters_total_bill_label = Label(Starters_Window, text="Total Bill", font=8,bg="#fdf5e2")
            Starters_total_bill_label.place(x=820, y=290)

            # Starters total bill input
            Starters_total_bill_input = Entry(Starters_Window, width=25, textvariable=Starters_total_bill_var)
            Starters_total_bill_input.place(x=780, y=330)

            # Starters total bill button
            Starters_total_bill_button = Button(Starters_Window, text="Total Bill",command =starters_total_bill)
            Starters_total_bill_button.place(x=830, y=360)

            # Starters back button
            Starters_Back_button =Button(Starters_Window, text="Back",command=back_button,padx=24)
            Starters_Back_button.place(x=420, y=470)

        def Main_Course():
            
            def main_Course_semi_bill():

                global Zira_Rice_price, Veg_Schezwan_Fried_Rice_price, Dal_Makhani_price,Dal_Tadka_price, Panner_Butter_Masala_price, Palak_Panner_price, Palak_Corn_price, Malai_Kofta_price, Kadhi_Pakora_price, Chana_Masala_price, Mushroom_Do_Pyaza_price, Mixed_Fruit_Raita_price, Pineapple_Raita_price, Curd_price, Butter_Naan_price, Butter_Roti_price, Lacha_Paratha_price

                global Zira_Rice_quantity, Veg_Schezwan_Fried_Rice_quantity, Dal_Makhani_quantity,Dal_Tadka_quantity, Panner_Butter_Masala_quantity, Palak_Panner_quantity, Palak_Corn_quantity, Malai_Kofta_quantity, Kadhi_Pakora_quantity, Chana_Masala_quantity, Mushroom_Do_Pyaza_quantity, Mixed_Fruit_Raita_quantity, Pineapple_Raita_quantity, Curd_quantity, Butter_Naan_quantity, Butter_Roti_quantity, Lacha_Paratha_quantity 

                global Main_Course_total_bill

                # main course radio button
                main_course_rd = main_course_rd_var.get()
                Main_Course_quantity = Main_Course_quantity_var.get()

                if(main_course_rd=="Zira Rice"):
                    Zira_Rice_price = 180
                    Zira_Rice_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Zira_Rice_quantity * Zira_Rice_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Veg Schezwan Fried Rice"):
                    Veg_Schezwan_Fried_Rice_price = 210
                    Veg_Schezwan_Fried_Rice_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Veg_Schezwan_Fried_Rice_quantity * Veg_Schezwan_Fried_Rice_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Dal Makhani"):
                    Dal_Makhani_price = 220
                    Dal_Makhani_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Dal_Makhani_quantity * Dal_Makhani_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Dal Tadka"):
                    Dal_Tadka_price = 190
                    Dal_Tadka_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Dal_Tadka_quantity * Dal_Tadka_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Palak Panner"):
                    Palak_Panner_price = 210
                    Palak_Panner_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Palak_Panner_quantity * Palak_Panner_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Panner Butter Masala"):
                    Panner_Butter_Masala_price = 240
                    Panner_Butter_Masala_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Panner_Butter_Masala_quantity * Panner_Butter_Masala_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)
            
                elif(main_course_rd=="Palak Corn"):
                    Palak_Corn_price = 180
                    Palak_Corn_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Palak_Corn_quantity * Palak_Corn_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Malai Kofta"):
                    Malai_Kofta_price = 200
                    Malai_Kofta_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Malai_Kofta_quantity * Malai_Kofta_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Kadhi Pakora"):
                    Kadhi_Pakora_price = 230
                    Kadhi_Pakora_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Kadhi_Pakora_quantity * Kadhi_Pakora_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Chana Masala"):
                    Chana_Masala_price = 175
                    Chana_Masala_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Chana_Masala_quantity * Chana_Masala_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Pineapple Raita"):
                    Pineapple_Raita_price = 185
                    Pineapple_Raita_quantity = Main_Course_quantity
                    Main_Course_semi_bill =  Pineapple_Raita_quantity * Pineapple_Raita_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Mushroom Do Pyaza"):
                    Mushroom_Do_Pyaza_price = 210
                    Mushroom_Do_Pyaza_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Mushroom_Do_Pyaza_quantity * Mushroom_Do_Pyaza_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Curd"):
                    Curd_price = 50
                    Curd_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Curd_quantity * Curd_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)
                    
                elif(main_course_rd=="Mixed Fruit Raita"):
                    Mixed_Fruit_Raita_price = 170
                    Mixed_Fruit_Raita_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Mixed_Fruit_Raita_quantity * Mixed_Fruit_Raita_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Butter Naan"):
                    Butter_Naan_price = 45
                    Butter_Naan_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Butter_Naan_quantity * Butter_Naan_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Butter Roti"):
                    Butter_Roti_price = 30
                    Butter_Roti_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Butter_Roti_quantity * Butter_Roti_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                elif(main_course_rd=="Lacha Paratha"):
                    Lacha_Paratha_price = 55
                    Lacha_Paratha_quantity = Main_Course_quantity
                    Main_Course_semi_bill = Lacha_Paratha_quantity * Lacha_Paratha_price
                    Main_Course_semi_bill_var.set(Main_Course_semi_bill)

                Main_Course_total_bill = Zira_Rice_quantity * Zira_Rice_price + Veg_Schezwan_Fried_Rice_quantity * Veg_Schezwan_Fried_Rice_price + Dal_Makhani_quantity * Dal_Makhani_price + Dal_Tadka_quantity * Dal_Tadka_price + Palak_Panner_quantity * Palak_Panner_price + Panner_Butter_Masala_quantity * Panner_Butter_Masala_price + Palak_Corn_quantity * Palak_Corn_price + Malai_Kofta_quantity * Malai_Kofta_price + Kadhi_Pakora_quantity * Kadhi_Pakora_price + Chana_Masala_quantity * Chana_Masala_price + Pineapple_Raita_quantity * Pineapple_Raita_price + Mushroom_Do_Pyaza_quantity * Mushroom_Do_Pyaza_price + Curd_quantity * Curd_price + Mixed_Fruit_Raita_quantity * Mixed_Fruit_Raita_price + Butter_Naan_quantity * Butter_Naan_price + Butter_Roti_quantity * Butter_Roti_price + Lacha_Paratha_quantity * Lacha_Paratha_price

            def main_Course_total_bill():

                global Main_Course_total_bill

                Main_Course_total_bill_var.set(Main_Course_total_bill)


            width = 1050
            height = 530
            Main_Course_Window = Toplevel()
            system_width = Main_Course_Window.winfo_screenwidth()
            system_height=Main_Course_Window.winfo_screenheight()

            c_x = int(system_width/2-width/2)
            c_y = int(system_height/2-height/2)


            Main_Course_Window.geometry(f"{width}x{height}+{c_x}+{c_y}")
            Main_Course_Window.maxsize(width, height)
            Main_Course_Window.minsize(width, height)
            Main_Course_Window.title("Restaurant Management Main Course")
            Main_Course_Window.config(bg="#fdf5e2")

            def back_button():
                main_course_rd_var.set(value='')
                Main_Course_quantity_var.set(value='')
                Main_Course_semi_bill_var.set(value='')
                Main_Course_total_bill_var.set(value='')
                Main_Course_Window.destroy()

            def on_closing():
                main_course_rd_var.set(value='')
                Main_Course_quantity_var.set(value='')
                Main_Course_semi_bill_var.set(value='')
                Main_Course_total_bill_var.set(value='')
                Main_Course_Window.destroy()

            Main_Course_Window.wm_protocol("WM_DELETE_WINDOW", on_closing)

            # Main Course label frame
            Main_Course_label_frame = Frame(Main_Course_Window,bg="#fdf5e2")
            Main_Course_label_frame.place(x=30, y=40)

            # Main Course price frame
            Main_Course_price_frame = Frame(Main_Course_Window,bg="#fdf5e2")
            Main_Course_price_frame.place(x=230, y=40)

            # Main Course main label
            Main_Course_main_label = Label(Main_Course_Window, text="Main Course", font=("Helvetica", 12, "bold"),bg="#fdf5e2")
            Main_Course_main_label.pack()

            #Zira Rice label
            Zira_Rice_label = Label(Main_Course_label_frame,text="Zira Rice", font=10,bg="#fdf5e2")
            Zira_Rice_label.grid(row=0, column=0)

            #Veg Schezwan Fried Rice label
            Veg_Schezwan_Fried_Rice_label = Label(Main_Course_label_frame,text="Veg Schezwan Fried Rice", font=10,bg="#fdf5e2")
            Veg_Schezwan_Fried_Rice_label.grid(row=1, column=0)

            #Dal Makhani label
            Dal_Makhani_label = Label(Main_Course_label_frame,text="Dal Makhani", font=10,bg="#fdf5e2")
            Dal_Makhani_label.grid(row=2, column=0)

            #Dal Tadka label
            Dal_Tadka_label = Label(Main_Course_label_frame,text="Dal Tadka", font=10,bg="#fdf5e2")
            Dal_Tadka_label.grid(row=3, column=0)

            #Panner Butter Masala label
            Panner_Butter_Masala_label = Label(Main_Course_label_frame,text="Panner Butter Masala", font=10,bg="#fdf5e2")
            Panner_Butter_Masala_label.grid(row=4, column=0)

            #Palak Panner label
            Palak_Panner_label = Label(Main_Course_label_frame,text="Palak Panner", font=10,bg="#fdf5e2")
            Palak_Panner_label.grid(row=5, column=0)

            #Palak Corn label
            Palak_Corn_label = Label(Main_Course_label_frame,text="Palak Corn", font=10,bg="#fdf5e2")
            Palak_Corn_label.grid(row=6, column=0)

            #Malai Kofta label
            Malai_Kofta_label = Label(Main_Course_label_frame,text="Malai Kofta", font=10,bg="#fdf5e2")
            Malai_Kofta_label.grid(row=7, column=0)

            #Kadhi Pakora label
            Kadhi_Pakora_label = Label(Main_Course_label_frame,text="Kadhi Pakora", font=10,bg="#fdf5e2")
            Kadhi_Pakora_label.grid(row=8, column=0)

            #Chana Masala label
            Chana_Masala_label = Label(Main_Course_label_frame,text="Chana Masala", font=10,bg="#fdf5e2")
            Chana_Masala_label.grid(row=9, column=0)

            #Mushroom Do Pyaza label
            Mushroom_Do_Pyaza_label = Label(Main_Course_label_frame,text="Mushroom Do Pyaza", font=10,bg="#fdf5e2")
            Mushroom_Do_Pyaza_label.grid(row=10, column=0)

            #Mixed Fruit Raita label
            Mixed_Fruit_Raita_label = Label(Main_Course_label_frame,text="Mixed Fruit Raita",font=10,bg="#fdf5e2")
            Mixed_Fruit_Raita_label.grid(row=11, column=0)

            #Pineapple Raita label
            Pineapple_Raita_label = Label(Main_Course_label_frame,text="Pineapple Raita",font=10,bg="#fdf5e2")
            Pineapple_Raita_label.grid(row=12, column=0)

            #Curd label
            Curd_label = Label(Main_Course_label_frame,text="Curd",font=10,bg="#fdf5e2")
            Curd_label.grid(row=13, column=0)

            #Butter Naan label
            Butter_Naan_label = Label(Main_Course_label_frame,text="Butter Naan",font=10,bg="#fdf5e2")
            Butter_Naan_label.grid(row=14, column=0)

            #Butter Roti label
            Butter_Roti_label = Label(Main_Course_label_frame,text="Butter Roti",font=10,bg="#fdf5e2")
            Butter_Roti_label.grid(row=15, column=0)

            #Lacha Paratha label
            Lacha_Paratha_label = Label(Main_Course_label_frame,text="Lacha Paratha",font=10,bg="#fdf5e2")
            Lacha_Paratha_label.grid(row=16, column=0)

            #Zira Rice Price label
            Zira_Rice_Price_label = Label(Main_Course_price_frame,text="Rs 180",font=10,bg="#fdf5e2")
            Zira_Rice_Price_label.grid(row=0, column=0)

            #Veg Schezwan Fried Rice Price label
            Veg_Schezwan_Fried_Rice_Price_label = Label(Main_Course_price_frame,text="Rs 210",font=10,bg="#fdf5e2")
            Veg_Schezwan_Fried_Rice_Price_label.grid(row=1, column=0)

            #Dal Makhani Price label
            Dal_Makhani_Price_label = Label(Main_Course_price_frame,text="Rs 220",font=10,bg="#fdf5e2")
            Dal_Makhani_Price_label.grid(row=2, column=0)

            #Dal Tadka Price label
            Dal_Tadka_Price_label = Label(Main_Course_price_frame,text="Rs 190",font=10,bg="#fdf5e2")
            Dal_Tadka_Price_label.grid(row=3, column=0)

            #Panner Butter Masala Price label
            Panner_Butter_Masala_Price_label = Label(Main_Course_price_frame,text="Rs 240",font=10,bg="#fdf5e2")
            Panner_Butter_Masala_Price_label.grid(row=4, column=0)

            #Palak Panner Price label
            Palak_Panner_Price_label = Label(Main_Course_price_frame,text="Rs 210",font=10,bg="#fdf5e2")
            Palak_Panner_Price_label.grid(row=5, column=0)

            #Palak Corn Price label
            Palak_Corn_Price_label = Label(Main_Course_price_frame,text="Rs 180",font=10,bg="#fdf5e2")
            Palak_Corn_Price_label.grid(row=6, column=0)

            #Malai Kofta Price label
            Malai_Kofta_Price_label = Label(Main_Course_price_frame,text="Rs 200",font=10,bg="#fdf5e2")
            Malai_Kofta_Price_label.grid(row=7, column=0)

            #Kadhi Pakora Price label
            Kadhi_Pakora_Price_label = Label(Main_Course_price_frame,text="Rs 230",font=10,bg="#fdf5e2")
            Kadhi_Pakora_Price_label.grid(row=8, column=0)

            #Chana Masala Price label
            Chana_Masala_Price_label = Label(Main_Course_price_frame,text="Rs 175",font=10,bg="#fdf5e2")
            Chana_Masala_Price_label.grid(row=9, column=0)

            #Mushroom Do Pyaza Price label
            Mushroom_Do_Pyaza_Price_label = Label(Main_Course_price_frame,text="Rs 210",font=10,bg="#fdf5e2")
            Mushroom_Do_Pyaza_Price_label.grid(row=10, column=0)

            #Mixed Fruit Raita Price label
            Mixed_Fruit_Raita_Price_label = Label(Main_Course_price_frame,text="Rs 170",font=10,bg="#fdf5e2")
            Mixed_Fruit_Raita_Price_label.grid(row=11, column=0)

            #Pineapple Raita Price label
            Pineapple_Raita_Price_label = Label(Main_Course_price_frame,text="Rs 185",font=10,bg="#fdf5e2")
            Pineapple_Raita_Price_label.grid(row=12, column=0)

            #Curd Price label
            Curd_Price_label = Label(Main_Course_price_frame,text="Rs 50",font=10,bg="#fdf5e2")
            Curd_Price_label.grid(row=13, column=0)

            #Butter Naan Price label
            Butter_Naan_Price_label = Label(Main_Course_price_frame,text="Rs 45",font=10,bg="#fdf5e2")
            Butter_Naan_Price_label.grid(row=14, column=0)

            #Butter Roti Price label
            Butter_Roti_Price_label = Label(Main_Course_price_frame,text="Rs 30",font=10,bg="#fdf5e2")
            Butter_Roti_Price_label.grid(row=15, column=0)

            #Lacha Paratha Price label
            Lacha_Paratha_Price_label = Label(Main_Course_price_frame,text="Rs 55",font=10,bg="#fdf5e2")
            Lacha_Paratha_Price_label.grid(row=16, column=0)

            # Add Main Course label
            Add_Main_Course_label = Label(Main_Course_Window, text="Add Main Course", font=12,bg="#fdf5e2")
            Add_Main_Course_label.place(x=410, y=45)

            # Main Course Window radio button
            Main_Course_Window_radiobox1 = Radiobutton(Main_Course_Window,text="Zira Rice",variable=main_course_rd_var, value="Zira Rice",bg="#fdf5e2")
            Main_Course_Window_radiobox1.place(x=360, y=80)
            Main_Course_Window_radiobox2 = Radiobutton(Main_Course_Window,text="Veg Schezwan Fried Rice",variable=main_course_rd_var, value="Veg Schezwan Fried Rice",bg="#fdf5e2")
            Main_Course_Window_radiobox2.place(x=470, y=80)
            Main_Course_Window_radiobox3 = Radiobutton(Main_Course_Window,text="Dal Makhani",variable=main_course_rd_var, value="Dal Makhani",bg="#fdf5e2")
            Main_Course_Window_radiobox3.place(x=360, y=110)
            Main_Course_Window_radiobox4 = Radiobutton(Main_Course_Window,text="Dal Tadka",variable=main_course_rd_var, value="Dal Tadka",bg="#fdf5e2")
            Main_Course_Window_radiobox4.place(x=470, y=110)
            Main_Course_Window_radiobox5= Radiobutton(Main_Course_Window,text="Palak Panner",variable=main_course_rd_var, value="Palak Panner",bg="#fdf5e2")
            Main_Course_Window_radiobox5.place(x=360, y=140)
            Main_Course_Window_radiobox6 = Radiobutton(Main_Course_Window,text="Panner Butter Masala",variable=main_course_rd_var, value="Panner Butter Masala",bg="#fdf5e2")
            Main_Course_Window_radiobox6.place(x=470, y=140)
            Main_Course_Window_radiobox7 = Radiobutton(Main_Course_Window,text="Palak Corn",variable=main_course_rd_var, value="Palak Corn",bg="#fdf5e2")
            Main_Course_Window_radiobox7.place(x=360, y=170)
            Main_Course_Window_radiobox8 = Radiobutton(Main_Course_Window,text="Malai Kofta",variable=main_course_rd_var, value="Malai Kofta",bg="#fdf5e2")
            Main_Course_Window_radiobox8.place(x=470,y=170)
            Main_Course_Window_radiobox9 = Radiobutton(Main_Course_Window,text="Kadhi Pakora",variable=main_course_rd_var, value="Kadhi Pakora",bg="#fdf5e2")
            Main_Course_Window_radiobox9.place(x=360, y=200)
            Main_Course_Window_radiobox10 = Radiobutton(Main_Course_Window,text="Chana Masala",variable=main_course_rd_var, value="Chana Masala",bg="#fdf5e2")
            Main_Course_Window_radiobox10.place(x=470,y=200)
            Main_Course_Window_radiobox11 = Radiobutton(Main_Course_Window,text="Pineapple Raita",variable=main_course_rd_var, value="Pineapple Raita",bg="#fdf5e2")
            Main_Course_Window_radiobox11.place(x=360,y=230)
            Main_Course_Window_radiobox12 = Radiobutton(Main_Course_Window,text="Mushroom Do Pyaza",variable=main_course_rd_var, value="Mushroom Do Pyaza",bg="#fdf5e2")
            Main_Course_Window_radiobox12.place(x=470, y=230)
            Main_Course_Window_radiobox13 = Radiobutton(Main_Course_Window,text="Curd",variable=main_course_rd_var, value="Curd",bg="#fdf5e2")
            Main_Course_Window_radiobox13.place(x=360, y=260)
            Main_Course_Window_radiobox14 = Radiobutton(Main_Course_Window,text="Mixed Fruit Raita",variable=main_course_rd_var, value="Mixed Fruit Raita",bg="#fdf5e2")
            Main_Course_Window_radiobox14.place(x=470,y=260)
            Main_Course_Window_radiobox15 = Radiobutton(Main_Course_Window,text="Butter Naan",variable=main_course_rd_var, value="Butter Naan",bg="#fdf5e2")
            Main_Course_Window_radiobox15.place(x=360,y=290)
            Main_Course_Window_radiobox16 = Radiobutton(Main_Course_Window,text="Butter Roti",variable=main_course_rd_var, value="Butter Roti",bg="#fdf5e2")
            Main_Course_Window_radiobox16.place(x=470, y=290)
            Main_Course_Window_radiobox17 = Radiobutton(Main_Course_Window,text="Lacha Paratha",variable=main_course_rd_var, value="Lacha Paratha",bg="#fdf5e2")
            Main_Course_Window_radiobox17.place(x=360,y=320)

            # Main Course place your order label
            Main_Course_place_your_order_label = Label(Main_Course_Window, text="Place Your Order", font=12,bg="#fdf5e2")
            Main_Course_place_your_order_label.place(x=800, y=40)

            # Main Course quantity label
            Main_Course_quantity_label = Label(Main_Course_Window, text="Quantity", font=8,bg="#fdf5e2")
            Main_Course_quantity_label.place(x=820, y=80)

            # Main Course quantity input
            Main_Course_quantity_input = Entry(Main_Course_Window, width=25, textvariable=Main_Course_quantity_var)
            Main_Course_quantity_input.place(x=780, y=120)

            # Main Course semi bill label
            Main_Course_semi_bill_label = Label(Main_Course_Window, text="Semi Bill", font=8,bg="#fdf5e2")
            Main_Course_semi_bill_label.place(x=820, y=160)

            # Main Course semi bill input
            Main_Course_semi_bill_input = Entry(Main_Course_Window, width=25, textvariable=Main_Course_semi_bill_var)
            Main_Course_semi_bill_input.place(x=780, y=200)

            # Main Course semi bill button
            Main_Course_semi_bill_button = Button(Main_Course_Window,text="Semi Bill",command=main_Course_semi_bill)
            Main_Course_semi_bill_button.place(x=830, y=240)

            # Main Course total bill label
            Main_Course_total_bill_label = Label(Main_Course_Window, text="Total Bill", font=8,bg="#fdf5e2")
            Main_Course_total_bill_label.place(x=820, y=280)

            # Main Course total bill input
            Main_Course_total_bill_input = Entry(Main_Course_Window, width=25, textvariable=Main_Course_total_bill_var)
            Main_Course_total_bill_input.place(x=780, y=320)

            Main_Course_total_bill_button = Button(Main_Course_Window, text="Total Bill",command = main_Course_total_bill)
            Main_Course_total_bill_button.place(x=830, y=360)

            # Main Course back button
            Main_Course_Back_button = Button(Main_Course_Window, text="Back",command=back_button,padx=24)
            Main_Course_Back_button.place(x=420, y=470)
        
        def dessert():

            def Dessert_semi_bill():
                
                global Kheer_price, Badam_Halwa_price, Moong_Dal_Halwa_price, Rasmalai_price, Rasgulla_price, Pineapple_Kesari_price, Fruit_Custard_price, Rabdi_with_Jalebi_price, Gulab_Jamun_price, Choco_lava_Cake_price, Brownie_with_Ice_Cream_price, Milk_badam_price, Fruit_Cream_price, Caramel_Bread_Pudding_price, Butterscotch_Ice_Cream_price, Choco_Brownie_Ice_Cream_price, Cold_Coffee_price

                global Kheer_quantity, Badam_Halwa_quantity, Moong_Dal_Halwa_quantity, Rasmalai_quantity, Rasgulla_quantity, Pineapple_Kesari_quantity, Fruit_Custard_quantity, Rabdi_with_Jalebi_quantity, Gulab_Jamun_quantity, Choco_lava_Cake_quantity, Brownie_with_Ice_Cream_quantity, Milk_badam_quantity, Fruit_Cream_quantity, Caramel_Bread_Pudding_quantity, Butterscotch_Ice_Cream_quantity, Choco_Brownie_Ice_Cream_quantity, Cold_Coffee_quantity

                global Dessert_total_bill

                #Dessert radio button
                Dessert_rd = Dessert_rd_var.get()
                Dessert_quantity = Dessert_quantity_var.get()


                if(Dessert_rd=="Kheer"):
                    Kheer_price = 90
                    Kheer_quantity = Dessert_quantity
                    Dessert_semi_bill = Kheer_quantity * Kheer_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)

                elif(Dessert_rd=="Badam Halwa"):
                    Badam_Halwa_price = 150
                    Badam_Halwa_quantity = Dessert_quantity
                    Dessert_semi_bill = Badam_Halwa_quantity * Badam_Halwa_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)

                elif(Dessert_rd=="Moong Dal Halwa"):
                    Moong_Dal_Halwa_price = 120
                    Moong_Dal_Halwa_quantity = Dessert_quantity
                    Dessert_semi_bill = Moong_Dal_Halwa_quantity * Moong_Dal_Halwa_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)

                elif(Dessert_rd=="Rasmalai"):
                    Rasmalai_price = 130
                    Rasmalai_quantity = Dessert_quantity
                    Dessert_semi_bill = Rasmalai_quantity * Rasmalai_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)

                elif(Dessert_rd=="Rasgulla"):
                    Rasgulla_price = 80
                    Rasgulla_quantity = Dessert_quantity
                    Dessert_semi_bill = Rasgulla_quantity * Rasgulla_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)

                elif(Dessert_rd=="Pineapple Kesari"):
                    Pineapple_Kesari_price = 110
                    Pineapple_Kesari_quantity = Dessert_quantity
                    Dessert_semi_bill = Pineapple_Kesari_quantity * Pineapple_Kesari_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)

                elif(Dessert_rd=="Fruit Custard"):
                    Fruit_Custard_price = 100
                    Fruit_Custard_quantity = Dessert_quantity
                    Dessert_semi_bill = Fruit_Custard_quantity * Fruit_Custard_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)

                elif(Dessert_rd=="Rabdi with Jalebi"):
                    Rabdi_with_Jalebi_price = 90
                    Rabdi_with_Jalebi_quantity = Dessert_quantity
                    Dessert_semi_bill = Rabdi_with_Jalebi_quantity * Rabdi_with_Jalebi_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)

                elif(Dessert_rd=="Gulab Jamun"):
                    Gulab_Jamun_price = 80
                    Gulab_Jamun_quantity = Dessert_quantity
                    Dessert_semi_bill = Gulab_Jamun_quantity * Gulab_Jamun_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)

                elif(Dessert_rd=="Choco lava Cake"):
                    Choco_lava_Cake_price = 75
                    Choco_lava_Cake_quantity = Dessert_quantity
                    Dessert_semi_bill = Choco_lava_Cake_quantity * Choco_lava_Cake_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)

                elif(Dessert_rd=="Brownie with Ice Cream"):
                    Brownie_with_Ice_Cream_price = 180
                    Brownie_with_Ice_Cream_quantity = Dessert_quantity
                    Dessert_semi_bill = Brownie_with_Ice_Cream_quantity * Brownie_with_Ice_Cream_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)

                elif(Dessert_rd=="Milk badam"):
                    Milk_badam_price = 60
                    Milk_badam_quantity = Dessert_quantity
                    Dessert_semi_bill = Milk_badam_quantity * Milk_badam_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)
                    
                elif(Dessert_rd=="Fruit Cream"):
                    Fruit_Cream_price =140
                    Fruit_Cream_quantity = Dessert_quantity
                    Dessert_semi_bill = Fruit_Cream_quantity * Fruit_Cream_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)
                    
                elif(Dessert_rd=="Caramel Bread Pudding"):
                    Caramel_Bread_Pudding_price = 170
                    Caramel_Bread_Pudding_quantity = Dessert_quantity
                    Dessert_semi_bill = Caramel_Bread_Pudding_quantity * Caramel_Bread_Pudding_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)
                    
                elif(Dessert_rd=="Butterscotch Ice Cream"):
                    Butterscotch_Ice_Cream_price = 80
                    Butterscotch_Ice_Cream_quantity = Dessert_quantity
                    Dessert_semi_bill = Butterscotch_Ice_Cream_quantity * Butterscotch_Ice_Cream_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)

                elif(Dessert_rd=="Choco Brownie Ice Cream"):
                    Choco_Brownie_Ice_Cream_price = 120
                    Choco_Brownie_Ice_Cream_quantity = Dessert_quantity
                    Dessert_semi_bill = Choco_Brownie_Ice_Cream_quantity * Choco_Brownie_Ice_Cream_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)
            
                elif(Dessert_rd=="Cold Coffee"):
                    Cold_Coffee_price = 90
                    Cold_Coffee_quantity = Dessert_quantity
                    Dessert_semi_bill = Cold_Coffee_quantity * Cold_Coffee_price
                    Dessert_semi_bill_var.set(Dessert_semi_bill)

                Dessert_total_bill = Kheer_quantity * Kheer_price + Badam_Halwa_quantity * Badam_Halwa_price + Moong_Dal_Halwa_quantity * Moong_Dal_Halwa_price + Rasmalai_quantity * Rasmalai_price + Rasgulla_quantity * Rasgulla_price + Pineapple_Kesari_quantity * Pineapple_Kesari_price + Fruit_Custard_quantity * Fruit_Custard_price + Rabdi_with_Jalebi_quantity * Rabdi_with_Jalebi_price + Gulab_Jamun_quantity * Gulab_Jamun_price + Choco_lava_Cake_quantity * Choco_lava_Cake_price + Brownie_with_Ice_Cream_quantity * Brownie_with_Ice_Cream_price + Milk_badam_quantity * Milk_badam_price + Fruit_Cream_quantity * Fruit_Cream_price + Caramel_Bread_Pudding_quantity * Caramel_Bread_Pudding_price + Butterscotch_Ice_Cream_quantity * Butterscotch_Ice_Cream_price + Choco_Brownie_Ice_Cream_quantity * Choco_Brownie_Ice_Cream_price + Cold_Coffee_quantity * Cold_Coffee_price

            
            def dessert_total_bill():
                global Dessert_total_bill

                Dessert_total_bill_var.set(Dessert_total_bill)

            def back_button():
                Dessert_rd_var.set(value='')
                Dessert_quantity_var.set(value='')
                Dessert_semi_bill_var.set(value='')
                Dessert_total_bill_var.set(value='')
                Dessert_Window.destroy()

            def on_closing():
                Dessert_rd_var.set(value='')
                Dessert_quantity_var.set(value='')
                Dessert_semi_bill_var.set(value='')
                Dessert_total_bill_var.set(value='')
                Dessert_Window.destroy()
            
            width = 1050
            height = 530
            Dessert_Window = Toplevel()
            Dessert_Window.title("Restaurant Management Dessert")
            system_width = Dessert_Window.winfo_screenwidth()
            system_height=Dessert_Window.winfo_screenheight()
            Dessert_Window.config( bg="#fdf5e2")

            c_x = int(system_width/2-width/2)
            c_y = int(system_height/2-height/2)


            Dessert_Window.geometry(f"{width}x{height}+{c_x}+{c_y}")
            Dessert_Window.maxsize(width, height)
            Dessert_Window.minsize(width, height)

            Dessert_Window.wm_protocol("WM_DELETE_WINDOW", on_closing)

            # Dessert label frame
            Dessert_label_frame = Frame(Dessert_Window, bg="#fdf5e2")
            Dessert_label_frame.place(x=30, y=40)

            # Dessert price frame
            Dessert_price_frame = Frame(Dessert_Window, bg="#fdf5e2")
            Dessert_price_frame.place(x=230, y=40)

            # Dessert main label
            Dessert_main_label = Label(Dessert_Window, text="Desserts", font=("Helvetica", 12, "bold"), bg="#fdf5e2")
            Dessert_main_label.pack()

            # Kheer label
            Kheer_label = Label(Dessert_label_frame,text="Kheer",font=10, bg="#fdf5e2")
            Kheer_label.grid(row=0,column=0)

            # Badam Halwa label
            Badam_Halwa_label = Label(Dessert_label_frame,text="Badam Halwa",font=10, bg="#fdf5e2")
            Badam_Halwa_label.grid(row=1,column=0)

            # Moong Dal Halwa label
            Moong_Dal_Halwa_label = Label(Dessert_label_frame,text="Moong Dal Halwa",font=10, bg="#fdf5e2")
            Moong_Dal_Halwa_label.grid(row=2,column=0)

            # Rasmalai label
            Rasmalai_label = Label(Dessert_label_frame,text="Rasmalai",font=10, bg="#fdf5e2")
            Rasmalai_label.grid(row=3,column=0)

            # Rasgulla label
            Rasgulla_label = Label(Dessert_label_frame,text="Rasgulla",font=10, bg="#fdf5e2")
            Rasgulla_label.grid(row=4,column=0)

            # Pineapple Kesari label
            Pineapple_Kesari_label = Label(Dessert_label_frame,text="Pineapple Kesari",font=10, bg="#fdf5e2")
            Pineapple_Kesari_label.grid(row=5,column=0)

            # Fruit Custard label
            Fruit_Custard_label = Label(Dessert_label_frame,text="Fruit Custard",font=10, bg="#fdf5e2")
            Fruit_Custard_label.grid(row=6,column=0)
            
            # Rabdi with Jalebi label
            Rabdi_with_Jalebi_label = Label(Dessert_label_frame,text="Rabdi with Jalebi",font=10, bg="#fdf5e2")
            Rabdi_with_Jalebi_label.grid(row=7,column=0)

            # Gulab Jamun label
            Gulab_Jamun_label = Label(Dessert_label_frame,text="Gulab Jamun",font=10, bg="#fdf5e2")
            Gulab_Jamun_label.grid(row=8,column=0)

            # Choco lava Cake label
            Choco_lava_Cake_label = Label(Dessert_label_frame,text="Choco lava Cake",font=10, bg="#fdf5e2")
            Choco_lava_Cake_label.grid(row=9,column=0)

            # Brownie with Ice Cream label
            Brownie_with_Ice_Cream_label = Label(Dessert_label_frame,text="Brownie with Ice Cream",font=10, bg="#fdf5e2")
            Brownie_with_Ice_Cream_label.grid(row=10,column=0)

            # Milk badam label
            Milk_badam_label = Label(Dessert_label_frame,text="Milk badam",font=10, bg="#fdf5e2")
            Milk_badam_label.grid(row=11,column=0)

            # Fruit Cream label
            Fruit_Cream_label = Label(Dessert_label_frame,text="Fruit Cream",font=10, bg="#fdf5e2")
            Fruit_Cream_label.grid(row=12,column=0)

            # Caramel Bread Pudding label
            Caramel_Bread_Pudding_label = Label(Dessert_label_frame,text="Caramel Bread Pudding",font=10, bg="#fdf5e2")
            Caramel_Bread_Pudding_label.grid(row=13,column=0)

            # Butterscotch Ice Cream label
            Butterscotch_Ice_Cream_label = Label(Dessert_label_frame,text="Butterscotch Ice Cream",font=10, bg="#fdf5e2")
            Butterscotch_Ice_Cream_label.grid(row=14,column=0)

            # Choco Brownie Ice Cream label
            Choco_Brownie_Ice_Cream_label = Label(Dessert_label_frame,text="Choco Brownie Ice Cream",font=10, bg="#fdf5e2")
            Choco_Brownie_Ice_Cream_label.grid(row=15,column=0)

            # Cold Coffee label
            Cold_Coffee_label = Label(Dessert_label_frame,text="Cold Coffee",font=10, bg="#fdf5e2")
            Cold_Coffee_label.grid(row=16,column=0)


            # Kheer price label 
            Kheer_price_label = Label(Dessert_price_frame,text="Rs 90",font=10, bg="#fdf5e2")
            Kheer_price_label.grid(row=0,column=0)

            # Badam Halwa price label
            Badam_Halwa_price_label = Label(Dessert_price_frame,text="Rs 150",font=10, bg="#fdf5e2")
            Badam_Halwa_price_label.grid(row=1,column=0)

            # Moong Dal Halwa price label
            Moong_Dal_Halwa_price_label = Label(Dessert_price_frame,text="Rs 120",font=10, bg="#fdf5e2")
            Moong_Dal_Halwa_price_label.grid(row=2,column=0)

            # Rasmalai price label
            Rasmalai_price_label = Label(Dessert_price_frame,text="Rs 130",font=10, bg="#fdf5e2")
            Rasmalai_price_label.grid(row=3,column=0)

            # Rasgulla price label
            Rasgulla_price_label = Label(Dessert_price_frame,text="Rs 80",font=10, bg="#fdf5e2")
            Rasgulla_price_label.grid(row=4,column=0)

            # Pineapple Kesari price label
            Pineapple_Kesari_label = Label(Dessert_price_frame,text="Rs 110",font=10, bg="#fdf5e2")
            Pineapple_Kesari_label.grid(row=5,column=0)

            # Fruit Custard price label
            Fruit_Custard_label = Label(Dessert_price_frame,text="Rs 100",font=10, bg="#fdf5e2")
            Fruit_Custard_label.grid(row=6,column=0)
            
            # Rabdi with Jalebi price label
            Rabdi_with_Jalebi_label = Label(Dessert_price_frame,text="Rs 90",font=10, bg="#fdf5e2")
            Rabdi_with_Jalebi_label.grid(row=7,column=0)

            # Gulab Jamun price label
            Gulab_Jamun_label = Label(Dessert_price_frame,text="Rs 80",font=10, bg="#fdf5e2")
            Gulab_Jamun_label.grid(row=8,column=0)

            # Choco lava Cake price label
            Choco_lava_Cake_price_label = Label(Dessert_price_frame,text="Rs 75",font=10, bg="#fdf5e2")
            Choco_lava_Cake_price_label.grid(row=9,column=0)

            # Brownie with Ice Cream price label
            Brownie_with_Ice_Cream_price_label = Label(Dessert_price_frame,text="Rs 180",font=10, bg="#fdf5e2")
            Brownie_with_Ice_Cream_price_label.grid(row=10,column=0)

            # Milk badam price label
            Milk_badam_price_label = Label(Dessert_price_frame,text="Rs 60",font=10, bg="#fdf5e2")
            Milk_badam_price_label.grid(row=11,column=0)

            # Fruit Cream price label
            Fruit_Cream_price_label = Label(Dessert_price_frame,text="Rs 140",font=10, bg="#fdf5e2")
            Fruit_Cream_price_label.grid(row=12,column=0)

            # Caramel Bread Pudding price label
            Caramel_Bread_Pudding_price_label = Label(Dessert_price_frame,text="Rs 170",font=10, bg="#fdf5e2")
            Caramel_Bread_Pudding_price_label.grid(row=13,column=0)

            # Butterscotch Ice Cream price label
            Butterscotch_Ice_Cream_price_label = Label(Dessert_price_frame,text="Rs 80",font=10, bg="#fdf5e2")
            Butterscotch_Ice_Cream_price_label.grid(row=14,column=0)

            # Choco Brownie Ice Cream price label
            Choco_Brownie_Ice_Cream_price_label = Label(Dessert_price_frame,text="Rs 120",font=10, bg="#fdf5e2")
            Choco_Brownie_Ice_Cream_price_label.grid(row=15,column=0)

            # Cold Coffee price label
            Cold_Coffee_price_label = Label(Dessert_price_frame,text="Rs 90",font=10, bg="#fdf5e2")
            Cold_Coffee_price_label.grid(row=16,column=0)

            # Add Desserts label
            Add_Main_Course_label = Label(Dessert_Window, text="Add Desserts", font=12, bg="#fdf5e2")
            Add_Main_Course_label.place(x=430, y=45)

            # Desserts Window radio button
            Dessert_Window_radiobox1 = Radiobutton(Dessert_Window,text="Kheer",variable=Dessert_rd_var, value="Kheer", bg="#fdf5e2")
            Dessert_Window_radiobox1.place(x=360, y=80)
            Dessert_Window_radiobox2 = Radiobutton(Dessert_Window,text="Badam Halwa",variable=Dessert_rd_var, value="Badam Halwa", bg="#fdf5e2")
            Dessert_Window_radiobox2.place(x=470, y=80)
            Dessert_Window_radiobox3 = Radiobutton(Dessert_Window,text="Rasmalai",variable=Dessert_rd_var, value="Rasmalai", bg="#fdf5e2")
            Dessert_Window_radiobox3.place(x=360, y=110)
            Dessert_Window_radiobox4 = Radiobutton(Dessert_Window,text="Moong Dal Halwa",variable=Dessert_rd_var, value="Moong Dal Halwa", bg="#fdf5e2")
            Dessert_Window_radiobox4.place(x=470, y=110)
            Dessert_Window_radiobox5 = Radiobutton(Dessert_Window,text="Rasgulla",variable=Dessert_rd_var, value="Rasgulla", bg="#fdf5e2")
            Dessert_Window_radiobox5.place(x=360, y=140)
            Dessert_Window_radiobox6 = Radiobutton(Dessert_Window,text="Pineapple Kesari",variable=Dessert_rd_var, value="Pineapple Kesari", bg="#fdf5e2")
            Dessert_Window_radiobox6.place(x=470, y=140)
            Dessert_Window_radiobox7 = Radiobutton(Dessert_Window,text="Fruit Custard",variable=Dessert_rd_var, value="Fruit Custard", bg="#fdf5e2")
            Dessert_Window_radiobox7.place(x=360, y=170)
            Dessert_Window_radiobox8 = Radiobutton(Dessert_Window,text="Rabdi with Jalebi",variable=Dessert_rd_var, value="Rabdi with Jalebi", bg="#fdf5e2")
            Dessert_Window_radiobox8.place(x=470, y=170)
            Dessert_Window_radiobox9 = Radiobutton(Dessert_Window,text="Gulab Jamun",variable=Dessert_rd_var, value="Gulab Jamun", bg="#fdf5e2")
            Dessert_Window_radiobox9.place(x=360, y=200)
            Dessert_Window_radiobox10 = Radiobutton(Dessert_Window,text="Choco lava Cake",variable=Dessert_rd_var, value="Choco lava Cake", bg="#fdf5e2")
            Dessert_Window_radiobox10.place(x=470, y=200)
            Dessert_Window_radiobox11 = Radiobutton(Dessert_Window,text="Milk badam",variable=Dessert_rd_var, value="Milk badam", bg="#fdf5e2")
            Dessert_Window_radiobox11.place(x=360, y=230)
            Dessert_Window_radiobox12 = Radiobutton(Dessert_Window,text="Brownie with Ice Cream",variable=Dessert_rd_var, value="Brownie with Ice Cream", bg="#fdf5e2")
            Dessert_Window_radiobox12.place(x=470, y=230)
            Dessert_Window_radiobox13 = Radiobutton(Dessert_Window,text="Fruit Cream",variable=Dessert_rd_var, value="Fruit Cream", bg="#fdf5e2")
            Dessert_Window_radiobox13.place(x=360, y=260)
            Dessert_Window_radiobox14 = Radiobutton(Dessert_Window,text="Caramel Bread Pudding",variable=Dessert_rd_var, value="Caramel Bread Pudding", bg="#fdf5e2")
            Dessert_Window_radiobox14.place(x=470, y=260)
            Dessert_Window_radiobox15 = Radiobutton(Dessert_Window,text="Cold Coffee",variable=Dessert_rd_var, value="Cold Coffee", bg="#fdf5e2")
            Dessert_Window_radiobox15.place(x=360, y=290)
            Dessert_Window_radiobox16 = Radiobutton(Dessert_Window,text="Butterscotch Ice Cream",variable=Dessert_rd_var, value="Butterscotch Ice Cream", bg="#fdf5e2")
            Dessert_Window_radiobox16.place(x=470, y=290)
            Dessert_Window_radiobox17 = Radiobutton(Dessert_Window,text="Choco Brownie Ice Cream",variable=Dessert_rd_var, value="Choco Brownie Ice Cream", bg="#fdf5e2")
            Dessert_Window_radiobox17.place(x=360, y=320)

            # Dessert place your order label
            Dessert_place_your_order_label = Label(Dessert_Window, text="Place Your Order", font=12, bg="#fdf5e2")
            Dessert_place_your_order_label.place(x=800, y=40)

            # Dessert quantity label
            Dessert_quantity_label = Label(Dessert_Window, text="Quantity", font=8, bg="#fdf5e2")
            Dessert_quantity_label.place(x=820, y=80)

            # Dessert quantity input
            Dessert_quantity_input = Entry(Dessert_Window, width=25, textvariable=Dessert_quantity_var)
            Dessert_quantity_input.place(x=780, y=120)

            # Dessert semi bill label
            Dessert_semi_bill_label = Label(Dessert_Window, text="Semi Bill", font=8, bg="#fdf5e2")
            Dessert_semi_bill_label.place(x=820, y=160)

            # Dessert semi bill input
            Dessert_semi_bill_input = Entry(Dessert_Window, width=25, textvariable=Dessert_semi_bill_var)
            Dessert_semi_bill_input.place(x=780, y=200)
        
            # Dessert semi bill button
            Dessert_semi_bill_button = Button(Dessert_Window,text="Semi Bill",command=Dessert_semi_bill)
            Dessert_semi_bill_button.place(x=830, y=240)

            # Dessert total bill label
            Dessert_total_bill_label = Label(Dessert_Window, text="Total Bill", font=8, bg="#fdf5e2")
            Dessert_total_bill_label.place(x=820, y=280)

            # Dessert total bill input
            Dessert_total_bill_input = Entry(Dessert_Window, width=25, textvariable=Dessert_total_bill_var)
            Dessert_total_bill_input.place(x=780, y=320)

            Dessert_total_bill_button = Button(Dessert_Window, text="Total Bill",command = dessert_total_bill)
            Dessert_total_bill_button.place(x=830, y=360)

            # Dessert back button
            Dessert_Back_button = Button(Dessert_Window, text="Back",command=back_button,padx=24)
            Dessert_Back_button.place(x=420, y=470)
            
        def checkout():

            def checkout_function():

                global Paneer_tikka_price, Veg_Seekh_Kabab_price, malai_chaap_price, cheese_balls_price, paneer_Kabab_price, cheese_chilli_price, Cheesy_garlic_bread_price, Potato_Twister_price, Chana_chaat_price, Crispy_corn_price, Cream_Salad_price, Veg_Cutlet_price, Potato_Lollipop_price, Veg_Noodle_price, Spring_Roll_price, Soya_veg_cutlet_price

                global Paneer_tikka_quantity, Veg_Seekh_Kabab_quantity, malai_chaap_quantity, cheese_balls_quantity, paneer_Kabab_quantity, cheese_chilli_quantity, Cheesy_garlic_bread_quantity, Potato_Twister_quantity, Chana_chaat_quantity, Crispy_corn_quantity, Cream_Salad_quantity, Veg_Cutlet_quantity, Potato_Lollipop_quantity, Veg_Noodle_quantity, Spring_Roll_quantity, Soya_veg_cutlet_quantity

                global Zira_Rice_price, Veg_Schezwan_Fried_Rice_price, Dal_Makhani_price,Dal_Tadka_price, Panner_Butter_Masala_price, Palak_Panner_price, Palak_Corn_price, Malai_Kofta_price, Kadhi_Pakora_price, Chana_Masala_price, Mushroom_Do_Pyaza_price, Mixed_Fruit_Raita_price, Pineapple_Raita_price, Curd_price, Butter_Naan_price, Butter_Roti_price, Lacha_Paratha_price

                global Zira_Rice_quantity, Veg_Schezwan_Fried_Rice_quantity, Dal_Makhani_quantity,Dal_Tadka_quantity, Panner_Butter_Masala_quantity, Palak_Panner_quantity, Palak_Corn_quantity, Malai_Kofta_quantity, Kadhi_Pakora_quantity, Chana_Masala_quantity, Mushroom_Do_Pyaza_quantity, Mixed_Fruit_Raita_quantity, Pineapple_Raita_quantity, Curd_quantity, Butter_Naan_quantity, Butter_Roti_quantity, Lacha_Paratha_quantity 


                global Kheer_price, Badam_Halwa_price, Moong_Dal_Halwa_price, Rasmalai_price, Rasgulla_price, Pineapple_Kesari_price, Fruit_Custard_price, Rabdi_with_Jalebi_price, Gulab_Jamun_price, Choco_lava_Cake_price, Brownie_with_Ice_Cream_price, Milk_badam_price, Fruit_Cream_price, Caramel_Bread_Pudding_price, Butterscotch_Ice_Cream_price, Choco_Brownie_Ice_Cream_price, Cold_Coffee_price

                global Kheer_quantity, Badam_Halwa_quantity, Moong_Dal_Halwa_quantity, Rasmalai_quantity, Rasgulla_quantity, Pineapple_Kesari_quantity, Fruit_Custard_quantity, Rabdi_with_Jalebi_quantity, Gulab_Jamun_quantity, Choco_lava_Cake_quantity, Brownie_with_Ice_Cream_quantity, Milk_badam_quantity, Fruit_Cream_quantity, Caramel_Bread_Pudding_quantity, Butterscotch_Ice_Cream_quantity, Choco_Brownie_Ice_Cream_quantity, Cold_Coffee_quantity

                global Starters_total_bill
                global Main_Course_total_bill
                global Dessert_total_bill

                checkout_customer_name = checkout_customer_name_var.get()
                checkout_customer_mobile_number = checkout_customer_mobile_number_var.get()
                checkout_starters_total_amount = checkout_starters_total_amount_var.get()
                checkout_main_course_total_amount = checkout_main_course_total_amount_var.get()
                checkout_dessert_total_amount = checkout_dessert_total_amount_var.get()
                checkout_grand_total = checkout_grand_total_var.get()

                now = datetime.datetime.now()
                current_datetime = now.strftime("%Y-%m-%d %H:%M:%S") 

                sql =f"insert into orders values('{checkout_customer_name}',{checkout_customer_mobile_number},'{current_datetime}',{checkout_grand_total},{checkout_starters_total_amount},{checkout_main_course_total_amount},{checkout_dessert_total_amount},{Paneer_tikka_price},{Paneer_tikka_quantity},{Veg_Seekh_Kabab_price},{Veg_Seekh_Kabab_quantity},{malai_chaap_price},{malai_chaap_quantity},{cheese_balls_price},{cheese_balls_quantity},{paneer_Kabab_price},{paneer_Kabab_quantity},{cheese_chilli_price},{cheese_chilli_quantity},{Cheesy_garlic_bread_price},{Cheesy_garlic_bread_quantity},{Potato_Twister_price},{Potato_Twister_quantity},{Chana_chaat_price},{Chana_chaat_quantity},{Crispy_corn_price},{Crispy_corn_quantity},{Cream_Salad_price},{Cream_Salad_quantity},{Veg_Cutlet_price},{Veg_Cutlet_quantity},{Potato_Lollipop_price},{Potato_Lollipop_quantity},{Veg_Noodle_price},{Veg_Noodle_quantity},{Spring_Roll_price},{Spring_Roll_quantity},{Soya_veg_cutlet_price},{Soya_veg_cutlet_quantity},{Zira_Rice_price},{Zira_Rice_quantity},{Veg_Schezwan_Fried_Rice_price},{Veg_Schezwan_Fried_Rice_quantity},{Dal_Makhani_price},{Dal_Makhani_quantity},{Dal_Tadka_price},{Dal_Tadka_quantity},{Panner_Butter_Masala_price},{Panner_Butter_Masala_quantity},{Palak_Panner_price},{Palak_Panner_quantity},{Palak_Corn_price},{Palak_Corn_quantity},{Malai_Kofta_price},{Malai_Kofta_quantity},{Kadhi_Pakora_price},{Kadhi_Pakora_quantity},{Chana_Masala_price},{Chana_Masala_quantity},{Mushroom_Do_Pyaza_price},{Mushroom_Do_Pyaza_quantity},{Mixed_Fruit_Raita_price},{Mixed_Fruit_Raita_quantity},{Pineapple_Raita_price},{Pineapple_Raita_quantity},{Curd_price},{Curd_quantity},{Butter_Naan_price},{Butter_Naan_quantity},{Butter_Roti_price},{Butter_Roti_quantity},{Lacha_Paratha_price},{Lacha_Paratha_quantity},{Kheer_price},{Kheer_quantity},{Badam_Halwa_price},{Badam_Halwa_quantity},{Moong_Dal_Halwa_price},{Moong_Dal_Halwa_quantity},{Rasmalai_price},{Rasmalai_quantity},{Rasgulla_price},{Rasgulla_quantity},{Pineapple_Kesari_price},{Pineapple_Kesari_quantity},{Fruit_Custard_price},{Fruit_Custard_quantity},{Rabdi_with_Jalebi_price},{Rabdi_with_Jalebi_quantity},{Gulab_Jamun_price},{Gulab_Jamun_quantity},{Choco_lava_Cake_price},{Choco_lava_Cake_quantity},{Brownie_with_Ice_Cream_price},{Brownie_with_Ice_Cream_quantity},{Milk_badam_price},{Milk_badam_quantity},{Fruit_Cream_price},{Fruit_Cream_quantity},{Caramel_Bread_Pudding_price},{Caramel_Bread_Pudding_quantity},{Butterscotch_Ice_Cream_price},{Butterscotch_Ice_Cream_quantity},{Choco_Brownie_Ice_Cream_price},{Choco_Brownie_Ice_Cream_quantity},{Cold_Coffee_price},{Cold_Coffee_quantity})"

                cursor.execute(sql)
                conn.commit()
                messagebox.showinfo("","Thank you for your order! We hope you enjoyed your meal!",parent=checkout_Window)

                Paneer_tikka_price = Veg_Seekh_Kabab_price = malai_chaap_price = cheese_balls_price = paneer_Kabab_price = cheese_chilli_price = Cheesy_garlic_bread_price = Potato_Twister_price = Chana_chaat_price = Crispy_corn_price = Cream_Salad_price = Veg_Cutlet_price = Potato_Lollipop_price = Veg_Noodle_price = Spring_Roll_price = Soya_veg_cutlet_price = 0

                Paneer_tikka_quantity = Veg_Seekh_Kabab_quantity = malai_chaap_quantity = cheese_balls_quantity = paneer_Kabab_quantity = cheese_chilli_quantity = Cheesy_garlic_bread_quantity = Potato_Twister_quantity = Chana_chaat_quantity = Crispy_corn_quantity = Cream_Salad_quantity = Veg_Cutlet_quantity = Potato_Lollipop_quantity = Veg_Noodle_quantity = Spring_Roll_quantity = Soya_veg_cutlet_quantity = 0

                Zira_Rice_price = Veg_Schezwan_Fried_Rice_price = Dal_Makhani_price = Dal_Tadka_price = Panner_Butter_Masala_price = Palak_Panner_price = Palak_Corn_price = Malai_Kofta_price = Kadhi_Pakora_price = Chana_Masala_price = Mushroom_Do_Pyaza_price = Mixed_Fruit_Raita_price = Pineapple_Raita_price = Curd_price = Butter_Naan_price = Butter_Roti_price = Lacha_Paratha_price = 0

                Zira_Rice_quantity = Veg_Schezwan_Fried_Rice_quantity = Dal_Makhani_quantity = Dal_Tadka_quantity = Panner_Butter_Masala_quantity = Palak_Panner_quantity = Palak_Corn_quantity = Malai_Kofta_quantity = Kadhi_Pakora_quantity = Chana_Masala_quantity = Mushroom_Do_Pyaza_quantity = Mixed_Fruit_Raita_quantity = Pineapple_Raita_quantity = Curd_quantity = Butter_Naan_quantity = Butter_Roti_quantity = Lacha_Paratha_quantity = 0 

                Kheer_price = Badam_Halwa_price = Moong_Dal_Halwa_price = Rasmalai_price = Rasgulla_price = Pineapple_Kesari_price = Fruit_Custard_price = Rabdi_with_Jalebi_price = Gulab_Jamun_price = Choco_lava_Cake_price = Brownie_with_Ice_Cream_price = Milk_badam_price = Fruit_Cream_price = Caramel_Bread_Pudding_price = Butterscotch_Ice_Cream_price = Choco_Brownie_Ice_Cream_price = Cold_Coffee_price = 0

                Kheer_quantity = Badam_Halwa_quantity = Moong_Dal_Halwa_quantity = Rasmalai_quantity = Rasgulla_quantity = Pineapple_Kesari_quantity = Fruit_Custard_quantity = Rabdi_with_Jalebi_quantity = Gulab_Jamun_quantity = Choco_lava_Cake_quantity = Brownie_with_Ice_Cream_quantity = Milk_badam_quantity = Fruit_Cream_quantity = Caramel_Bread_Pudding_quantity = Butterscotch_Ice_Cream_quantity = Choco_Brownie_Ice_Cream_quantity = Cold_Coffee_quantity = 0
                        
                Starters_total_bill = 0
                Main_Course_total_bill = 0
                Dessert_total_bill = 0

                checkout_customer_name_var.set(value='')
                checkout_customer_mobile_number_var.set(value='')
                checkout_starters_total_amount_var.set(value='')
                checkout_main_course_total_amount_var.set(value='')
                checkout_dessert_total_amount_var.set(value='')
                checkout_grand_total_var.set(value='')
                        

            def back_button():
                checkout_Window.destroy()

            global Starters_total_bill
            global Main_Course_total_bill
            global Dessert_total_bill
            grand_total_bill = Starters_total_bill + Main_Course_total_bill + Dessert_total_bill

            checkout_starters_total_amount_var.set(Starters_total_bill)
            checkout_main_course_total_amount_var.set(Main_Course_total_bill)
            checkout_dessert_total_amount_var.set(Dessert_total_bill)
            checkout_grand_total_var.set(grand_total_bill)


            width = 600
            height = 420
            checkout_Window = Toplevel()
            system_width = checkout_Window.winfo_screenwidth()
            system_height = checkout_Window.winfo_screenheight()

            c_x = int(system_width/2-width/2)
            c_y = int(system_height/2-height/2)
            checkout_Window.geometry(f"{width}x{height}+{c_x}+{c_y}")
            checkout_Window.maxsize(width, height)
            checkout_Window.minsize(width, height)
            checkout_Window.title("Restaurant Management Checkout")
            checkout_Window.config(bg="#fdf5e2")

            checkout_main_label = Label(checkout_Window, text="Checkout", font=("Helvetica", 12, "bold"), bg="#fdf5e2")
            checkout_main_label.pack()

            checkout_label_frame= Frame(checkout_Window, bg="#fdf5e2")
            checkout_label_frame.place(x=100,y=60)

            checkout_input_frame= Frame(checkout_Window, bg="#fdf5e2")
            checkout_input_frame.place(x=280,y=60)
            
            # checkout customer name label
            checkout_customer_name_label = Label(checkout_label_frame, text="Customer Name",pady=5, bg="#fdf5e2")
            checkout_customer_name_label.grid(row=0,column=0)

            # checkout customer name input
            checkout_customer_name_input = Entry(checkout_input_frame, width=25,textvariable=checkout_customer_name_var)
            checkout_customer_name_input.grid(row=0,column=0,pady=5)
            
            # checkout customer mobile number label
            checkout_customer_mobile_number_label = Label(checkout_label_frame, text="Customer Mobile No.",pady=5, bg="#fdf5e2")
            checkout_customer_mobile_number_label.grid(row=1,column=0)
            
            # checkout customer mobile number input
            checkout_customer_mobile_number_input = Entry(checkout_input_frame, width=25,textvariable=checkout_customer_mobile_number_var)
            checkout_customer_mobile_number_input.grid(row=1,column=0,pady=5)

            # checkout Starters total amount label
            checkout_Starters_total_amount_label = Label(checkout_label_frame, text="Starters Total Amount",pady=5, bg="#fdf5e2")
            checkout_Starters_total_amount_label.grid(row=2,column=0)
            
            # checkout Starters total amount input
            checkout_Starters_total_amount_input = Entry(checkout_input_frame, width=25,textvariable=checkout_starters_total_amount_var)
            checkout_Starters_total_amount_input.grid(row=2,column=0,pady=5)

            # checkout Main Course total amount label
            checkout_Main_Course_total_amount_label = Label(checkout_label_frame, text="Main Course Total Amount",pady=5, bg="#fdf5e2")
            checkout_Main_Course_total_amount_label.grid(row=3,column=0)

            # checkout Main Course total amount input
            checkout_Main_Course_total_amount_input = Entry(checkout_input_frame, width=25,textvariable=checkout_main_course_total_amount_var)
            checkout_Main_Course_total_amount_input.grid(row=3,column=0,pady=5)

            # checkout Dessert total amount label 
            checkout_Dessert_total_amount_label = Label(checkout_label_frame, text="Dessert Total Amount",pady=5, bg="#fdf5e2")
            checkout_Dessert_total_amount_label.grid(row=4,column=0)

            # checkout Dessert total amount input
            checkout_Dessert_total_amount_input = Entry(checkout_input_frame, width=25,textvariable=checkout_dessert_total_amount_var)
            checkout_Dessert_total_amount_input.grid(row=4,column=0,pady=5)

            # checkout Grand Total label
            checkout_Grand_Total_label = Label(checkout_label_frame, text="Grand Total",pady=5, bg="#fdf5e2")
            checkout_Grand_Total_label.grid(row=5,column=0)

            # checkout Grand input Total input
            checkout_Grand_Total_input = Entry(checkout_input_frame, width=25,textvariable=checkout_grand_total_var)
            checkout_Grand_Total_input.grid(row=5,column=0,pady=5)

            checkout_btn = Button(checkout_Window, text="Checkout",command= checkout_function)
            checkout_btn.place(x=200,y=300)

            #checkout back button
            checkout_Back_button = Button(checkout_Window, text="Back",command=back_button,padx=24)
            checkout_Back_button.place(x=320, y=300)

        
        def back_button():
            Menu_Window.destroy()

        width = 400
        height = 350
        Menu_Window = Toplevel()
        system_width = Menu_Window.winfo_screenwidth()
        system_height=Menu_Window.winfo_screenheight()

        c_x = int(system_width/2-width/2)
        c_y = int(system_height/2-height/2)


        Menu_Window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        Menu_Window.maxsize(width, height)
        Menu_Window.minsize(width, height)
        Menu_Window.title("Restaurant Management Menu")
        Menu_Window.config(bg="#fdf5e2")

        # Menu label
        Menu_label = Label(Menu_Window, text="Menu",font=("Helvetica", 12, "bold"),bg="#fdf5e2")
        Menu_label.pack()

        # starters button
        starters_button = Button(Menu_Window, text="Starter", command=starters, padx=50)
        starters_button.place(x=120, y=50)

        # Main Course button
        Main_Course_button = Button(Menu_Window, text="Main Course", command=Main_Course, padx=35)
        Main_Course_button.place(x=120, y=100)

        # Dessert button
        dessert_button = Button(Menu_Window, text="Dessert",command=dessert, padx=50)
        dessert_button.place(x=120, y=150)

        # checkout button
        checkout_button = Button(Menu_Window, text="Checkout", command=checkout, padx=50)
        checkout_button.place(x=120, y=240)

        # back button
        Back_button = Button(Menu_Window, text="Back",command=back_button,padx=24)
        Back_button.place(x=160, y=290)

    
    # main label
    main_label = Label(window, text="Welcome to Restaurant",font=("Helvetica", 20, "bold"),bg="#fdf5e2")
    main_label.place(x=70, y=50)

    # Main Menu win button
    button = Button(window, text="Proceed to Menu", command=Menu_win)
    button.place(x=170, y=140)

window.mainloop()
