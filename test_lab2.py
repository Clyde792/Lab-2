import lab2

def test_find_min_max():
    input_arr=[10,20,5,8]
    result= lab2.find_min_max(input_arr)
    assert result== [5,20]
    
def test_calc_average():

    input_arr = [10, 20, 30]

    result = lab2.calc_average(input_arr)

    assert result == 20


def test_calc_median_temperature():

    input_arr = [10, 20, 30]

    result = lab2.calc_median_temperature(input_arr)

    assert result == 20