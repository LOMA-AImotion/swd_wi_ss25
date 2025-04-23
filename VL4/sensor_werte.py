werte = [3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2]
# nehme nur jeden zweiten Wert bis zur ersten Hälfte, per slicing 
# soll sein [3.2, 2.8, 4.5]
print(werte[:1+len(werte) // 2:2])
