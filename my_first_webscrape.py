from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.kabum.com.br/hardware/placa-de-video-vga?gclid=Cj0KCQiAr93gBRDSARIsADvHiOqRJwY4TqngpvXX6YGT2QzjccqzzYQFmypdDUvThKzdSoDg6Z0sOTAaAv18EALw_wcB'

# Opening the connection, storing the page 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#Html parser
page_soup = soup(page_html, "html.parser")

#If i type in the following, the console will return what i asked for in that given WebPage

#For example, if i type page_soup.h2, it should return all the h2's on the WebPage
#class="h2titcategoria">Placa de vídeo (VGA)</h2>
#In our case, the return is the given above

#We can also try it with other HTML's properties, such as title
#<title>Placa de vídeo (VGA) - Melhores ofertas de Placa de vídeo (VGA) no KaBuM!</title>
#The return is the given above

#This grabs each product
containers = page_soup.findAll("div",{"class":"listagem-box"})

#The command line "containers[0]" returns the HTML for the first item on that object
#You can check the HTML of our example inside the new window.

#The next lines of code will loop through the item's names
for container in containers:
 brand = container.div.a.img["title"]

 title_container = container.findAll("span",{"class":"H-titulo" })
 product_name = title_container[0].text

 price_container = container.findAll("li",{"style":"font-size:10px; text-align:left;"})
 price = price_container[0].text.strip()

	
 print("brand:  " + brand)
 print("product_name:  " + product_name)
 print("price:  " + price)
