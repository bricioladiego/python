def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Diego", "lastname": "Domínguez"}

    super_list = [
        {"firstname": "Seiya", "lastname": "Pegaso"},
        {"firstname": "Mariana", "lastname": "Reyes"},
        {"firstname": "Vanessa", "lastname": "González"},
        {"firstname": "Saori", "lastname": "Kido"},
        {"firstname": "Aioros", "lastname": "Sagitario"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "integer_nums": [-10, -2, 0, 1, 10],
        "floating_nums": [0.21, 9.53, 20.61],
    }

    for key, value in super_dict.items():
        print(key, ">", value)

    for values in super_list:
        print(values)



if __name__ == '__main__':
    run()