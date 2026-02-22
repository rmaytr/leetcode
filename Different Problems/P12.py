def RomanToInt(s: str) -> int:
    num = int(s)
    ans = ""
    count = 0
    while num > 0:
        digit = num % 10
        if count == 0:
            if digit < 4:
                ans = "I" * digit + ans
            elif digit == 4:
                ans = "IV" + ans
            elif digit < 9:
                ans = "V" + "I" * (digit - 5) + ans
            elif digit == 9:
                ans = "IX" + ans
        elif count == 1:
            if digit < 4:
                ans = "X" * digit + ans
            elif digit == 4:
                ans = "XL" + ans
            elif digit < 9:
                ans = "L" + "X" * (digit - 5) + ans
            elif digit == 9:
                ans = "XC" + ans
        elif count == 2:
            if digit < 4:
                ans = "C" * digit + ans
            elif digit == 4:
                ans = "CD" + ans
            elif digit < 9:
                ans = "D" + "C" * (digit - 5) + ans
            elif digit == 9:
                ans = "CM" + ans
        else:
            ans = "M" * digit + ans
        num //= 10
        count += 1
    return ans


print(RomanToInt(10))  # Output: "MCMXCIV"
