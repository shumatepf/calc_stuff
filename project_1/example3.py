from decimal import *

data_dict = {
    0.00875: 1.57e7,
    0.0125: 5.78e6,
    0.0175: 2.58e6,
    0.0250: 1.15e6,
    0.0350: 6.01e5,
    0.0500: 2.87e5,
    0.0700: 1.39e5,
    0.0900: 8.90e4,
    0.112: 7.02e4,
    0.137: 4.03e4,
    0.175: 2.57e4,
    0.250: 9.61e3,
    0.350: 2.15e3,
    0.440: 9.33e2,
    0.550: 2.66e2,
    0.660: 1.08e2,
    0.770: 5.17e1,
    0.880: 2.80e1,
    1.05: 1.36e1,
    1.27: 5.82,
    1.48: 2.88,
    1.82: 1.25,
    2.22: 4.80e-1,
    2.75: 2.17e-1,
    3.30: 1.18e-1,
    4.12: 6.27e-2,
    5.22: 3.03e-2
}

key_list = sorted(data_dict.keys())

getcontext().prec = 10

def reimann_sum(list, k):
    """
    Script for getting reimann sum from a dict given a list of the keys
    *The list of keys portion can probably be changed*
    
    @param list = list of keys
    @param k = 1 or 0. 1 being left sum and 0 being right sum

    """
    result_list = []

    for i, key in enumerate(list[:-1]):
        diff = Decimal(list[i+1]) - Decimal(list[i])
        product = diff * Decimal(data_dict[list[i + k]])
        result_list.append(product) 

    result_sum = sum(result_list)

    return result_sum

if __name__=="__main__":
    total_result_lower = reimann_sum(key_list, 1)
    total_result_upper = reimann_sum(key_list, 0)

    # between 0.05 and 0.55
    sub_list_question_2 = sorted([key for key in key_list if key >= 0.05 and key <= 0.55 ])

    sub_result_lower_question_2 = reimann_sum(sub_list_question_2, 1)
    sub_result_upper_question_2 = reimann_sum(sub_list_question_2, 0)

    # greater than 2.5
    sub_list_question_3 = sorted([key for key in key_list if key < 2.5])

    sub_result_lower_question_3 = reimann_sum(sub_list_question_3, 1)

    percentage_lost = 100 - (sub_result_lower_question_3/total_result_lower * 100)

    print(f"Total lower bounds result for question 1: {total_result_lower}")
    print(f"Total upper bounds result for question 1: {total_result_upper}")

    print()

    print(f"Sub lower bounds result for quesiton 2: {sub_result_lower_question_2}")
    print(f"Sub upper bounds result for quesiton 2: {sub_result_upper_question_2}")

    print(f"Sub lower bounds result for quesiton 3: {sub_result_lower_question_3}")

    print(f"Percentage lost: {percentage_lost}%")
