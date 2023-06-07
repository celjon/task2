def filtrui_bazar(filtering, array):
    filtered_bazar = filter(filtering, array)
    return list(filtered_bazar)

filt_spaces = lambda s: " " not in s

filt_str_start_with_a = lambda s: not s.startswith("a")

filt_short_str = lambda s: len(s) >= 5

input_str = input("Введите строки, разделяя их запятой: ")
input_array = input_str.split(",")

filtered_bazar = filtrui_bazar(filt_spaces, input_array)
print("Исключаем строки с  пробелами:", filtered_bazar)

filtered_bazar = filtrui_bazar(filt_str_start_with_a, input_array)
print("Исключение строк начинающихся с а:", filtered_bazar)

filtered_bazar = filtrui_bazar(filt_short_str, input_array)
print("Исключаем строки меньше 5:", filtered_bazar)
