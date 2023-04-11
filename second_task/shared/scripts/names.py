# encoding: UTF-8

from objectmaphelper import *

alza_browsertab = {"title": "Alza.cz – rychlý a pohodlný nákup odkudkoliv | Alza.cz", "type": "BrowserTab"}
btn_phones_watches_tablets_category = {"container": alza_browsertab, "id": "litp18890259", "tagName": "LI"}

phones_watches_tablets_browsertab = {"title": "Mobily, chytré hodinky a tablety | Alza.cz", "type": "BrowserTab"}
btn_phones = {"container": phones_watches_tablets_browsertab, "simplifiedInnerText": "Mobilní telefony", "tagName": "A"}

phones_browsertab = {"title": "Mobilní telefony, mobily | Alza.cz", "type": "BrowserTab"}
btn_from_the_most_expensive = {"container": phones_browsertab, "id": "ui-id-6", "simplifiedInnerText": "Od nejdražšího", "tagName": "A"}
btn_first_buy = {"container": phones_browsertab, "simplifiedInnerText": "Koupit", "tagName": "A"}

most_expensive_phones_browser = {"title": "Nejdražší mobily | Alza.cz", "type": "BrowserTab"}
btn_second_buy = {"container": most_expensive_phones_browser, "simplifiedInnerText": "Koupit", "tagName": "A", "occurrence": 2}


product_in_cart_browser = {"title": "Zboží přidáno do košíku | Alza.cz", "type": "BrowserTab"}
product_has_been_added =  {"container": product_in_cart_browser, "simplifiedInnerText": "Zboží bylo přidáno do košíku", "tagName": "A"}
btn_back = {"container": product_in_cart_browser, "id": "varBBackButton", "simplifiedInnerText": "Zpět", "tagName": "A"}
btn_continue_to_cart = {"container": product_in_cart_browser, "id": "varBToBasketButton", "simplifiedInnerText": "Pokračovat do košíku", "tagName": "A"}