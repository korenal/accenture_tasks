# -*- coding: utf-8 -*-

import names


def main():
    startBrowser("https://www.alza.cz/")
    mouseClick(waitForObject(names.btn_phones_watches_tablets_category))    
    mouseClick(waitForObject(names.btn_phones))
    mouseClick(waitForObject(names.btn_from_the_most_expensive))
    snooze(5)
    mouseClick(waitForObject(names.btn_first_buy))
    test.compare(waitForObjectExists(names.product_has_been_added).innerText, "Zboží bylo přidáno do košíku")     
    activateBrowserTab(waitForObject(names.product_in_cart_browser))   
    mouseClick(waitForObject(names.btn_back))    
    mouseClick(waitForObject(names.btn_second_buy))
    test.compare(waitForObjectExists(names.product_has_been_added).innerText, "Zboží bylo přidáno do košíku")  
    activateBrowserTab(waitForObject(names.product_in_cart_browser))
    mouseClick(waitForObject(names.btn_continue_to_cart))    