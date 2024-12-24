# helper.py or utility.py or (any name you want for file with utility funcytions)
# utility functions are self-made functions which makes code easier to read
def count_substring(txt, sub_txt):
    return txt.count(sub_txt)

def get_string_and_substring():
    txt = input('Enter a string >')
    sub_txt = input('Enter a substring >')
    return txt, sub_txt

def outcome():
    txt, sub_txt = get_string_and_substring()
    count_sub = count_substring(txt, sub_txt)
    print('the substring ' + '"' + sub_txt + '"' + ' appears ' + str(count_sub) + ' times' + ' in ' + '"' + txt + '"')
    f_str = f'the substring "{sub_txt}" appears {count_sub} times in "{txt}"'
    # return f'the substring {sub_txt} appears {count_sub} times in {txt}'
    # print(f_str)
