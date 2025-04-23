def ist_palindrom(s: str) -> bool:
    return s == s[::-1]

wort = input("Wort eingeben:")
print(f"{wort} ist ein Palindrom? {ist_palindrom(wort)}")