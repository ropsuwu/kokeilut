cm = int(input("Kuinka pitkä olet? "))
ikä = int(input("Kuinka vanha olet? "))
if  100 <= cm < 140:
    print("Saat mennä lasten laitteisiin")
elif ikä <= 8:
    print("Saat mennä kaikkiin paitsi Tulirekeen")
elif cm == 195:
    print("Saat mennä kaikkiin muihin paitsi Kirnuun")
elif cm >= 140:
    print("Saat mennä kaikkiin laitteisiin")
else:
    print("Et pääse minnekkään")
