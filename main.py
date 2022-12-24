from DataCollection import DataCollector
from DataAccess.Read import ReadData

yemeksepeti_url = "https://www.yemeksepeti.com/restaurant/lm6l/popeyes-lm6l"
maydonoz_url = "https://www.yemeksepeti.com/restaurant/sopa/maydonoz-doner-sopa"
popeyes_url = "https://www.yemeksepeti.com/restaurant/lm6l/popeyes-lm6l"
dominos_url = "https://www.yemeksepeti.com/restaurant/qfq9/dominos-pizza-qfq9"
morgis_url = "https://www.yemeksepeti.com/restaurant/defq/morgis-odun-atesinde-doner"

# Ekranda bir url kısmı ve buton olacak, url kısmına koyulan urli kullanarak asagıdaki fonksiyon cagrılacak.

DataCollector.open_webpage(maydonoz_url)
