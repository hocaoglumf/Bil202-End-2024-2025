# 1'den 100'e kadar sayıların karelerini üreten  Python kodu
# verim ve dolayısıyla üreteç

# Sonraki kare sayısını
# yazdıran sonsuz bir üreteç işlevi görür


def nextSquare():
	i = 1

	# sonsuz döngü
	while True:
		yield i*i
		i += 1


for num in nextSquare():
	if num > 100:
		break
	print(num)
