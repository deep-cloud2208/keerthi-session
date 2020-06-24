def func(*args, **kwargs):
    # print(args)
    # print(kwargs)
    legb_var = "Enclosed"


    def enclosed_func():
        legb_var = "Local"
        print(legb_var)
        print(locals())

    enclosed_func()

model_year = 2019
product_name = "Seltos"
product_make = "KIA"
product_sales = 90000


# legb_var = "Global"

engine_spec = {
    "CC" : 1400,
    "Engine" : "4 Stroke"
}
manufacturing_addr1 = "India"

func(model_year,product_make,product_name, product_sales,engine_spec, manufacturing_addr1, manufacturing_addr2="Chennai", man_state="TN")

# print(globals())
