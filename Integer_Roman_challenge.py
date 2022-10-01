# Roman to Integer
def romanToInt(s: str) -> int:
        roman_int_dict = {"I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D":500, "M":1000}
        special_case = ["IV", "IX", "XL", "XC", "CD", "CM"]
        if len(s) == 1:
            return roman_int_dict[s]
        else:
            S=0
            for cas in special_case:
                S += (roman_int_dict[cas[1]] - roman_int_dict[cas[0]]) * s.count(cas)
                s = s.replace(cas, '')
            for i in s:
                S += roman_int_dict[i]
            return S

# Integer to Roman
def intToRoman(num: int) -> str:
        roman_int_dict = [{"1": "I", "5": "V"}, {"1": "X", "5":"L"}, {"1": "C", "5":"D"}]
        special_case = [{"4":"IV", "9":"IX"}, {"4":"XL", "9":"XC"}, {"4":"CD", "9":"CM"}]
        str_num = str(num)
        m = ''
        if len(str_num) == 4:
            m = 'M'* (num//1000)
            str_num = str_num[1:]
            
        result = []
        for i, j in enumerate(str_num[::-1]):
            if j in ["4", "9"]:
                result.append(special_case[i][j])
            else:
                if int(j) >= 5:
                    result.append(roman_int_dict[i]["5"] +  roman_int_dict[i]["1"] * (int(j) - 5))
                    
                else:
                    result.append(roman_int_dict[i]["1"] * int(j))
        result.append(m)
        result.reverse()
        return ''.join(result)

if __name__=='__main__':
    s = int(input("int: "))
    print(intToRoman(s))