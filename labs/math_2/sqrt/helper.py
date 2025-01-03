import math
from typing import Union


# ---- 1 simple evaluation sqtr ---------------
def sqrt_1(x: Union[int, float]) -> float:
    return math.sqrt(x)


# -----2 raises with message---------------------
def sqrt_2_with_raises(x: Union[int, float]) -> Union[float, str]:
    try:
        result = sqrt_1(x)
        return result
    except ValueError:
        raise ValueError("Ошибка! Невозможно найти квадратный корень из отрицательного числа!")
    except TypeError:
        raise TypeError("Ошибка! Вы забыли ввести выражение!")
    except Exception:
        raise Exception("Ошибка! Вы ввели некорректное выражение!")


# ---------3 exception with return msg-------------
def sqrt_3_with_exceptions(x: Union[int, float]) -> Union[float, str]:
    try:
        result = sqrt_1(x)
        return result
    except ValueError:
        return "Ошибка! Невозможно найти квадратный корень из отрицательного числа!"
    except TypeError:
        return "Ошибка! Вы забыли ввести выражение!"
    except Exception:
        return "Ошибка! Вы ввели некорректное выражение!"


if __name__ == "__main__":
    # print(sqrt_1(16))
    # print(sqrt_1(0))

    print(sqrt_2_with_raises(4))
    print(sqrt_2_with_raises(-4))
    print(sqrt_2_with_raises("string"))

    # print(sqrt_3_with_exceptions(4))
    # print(sqrt_3_with_exceptions(-4))
    # print(sqrt_3_with_exceptions("string"))
