from selenium import webdriver
from selenium.webdriver.common.by import By

# create a webdriver instance
driver = webdriver.Chrome()

# navigate to the Airbnb website
driver.get("https://www.airbnb.com/")

# enter the destination and dates into the search form
destination_input = driver.find_element(By.ID, "Koan-magic-carpet-koan-search-bar__input")
destination_input.send_keys("Lagos, Nigeria")

# click the check-in and check-out input fields to open the calendars
checkin_input = driver.find_element(By.ID, "checkin_input")
checkin_input.click()
checkout_input = driver.find_element(By.ID, "checkout_input")
checkout_input.click()

# select the check-in and check-out dates on the calendars
checkin_date = driver.find_element(By.CSS_SELECTOR, "[aria-label='Sat, May 15, 2021']")
checkin_date.click()
checkout_date = driver.find_element(By.CSS_SELECTOR, "[aria-label='Sat, May 22, 2021']")
checkout_date.click()

# submit the search form
search_button = driver.find_element(By.CSS_SELECTOR, "._1s98zs81")
search_button.click()

# wait for the search results to load
driver.implicitly_wait(10)

# scrape the listings from the search results page
while True:
    for listing in listings:
        title = listing.find_element(By.CSS_SELECTOR, ".AirbnbStyle__CardContent-sc-1vh4e1a-3").text
        price = listing.find_element(By.CSS_SELECTOR, ".AirbnbStyle__CardPrice-sc-1vh4e1a-5").text
        print(f"{title}: {price}")

    # check if there is a "Next" button
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, ".next_page")
    except NoSuchElementException:
        # if there is no "Next" button, break out of the loop
        break

    # click the "Next" button to go to the next page
    next_button.click()

    # wait for the next page to load
    driver.implicitly_wait(10)

    # scrape the listings from the next page
    listings = driver.find_elements(By.CSS_SELECTOR, ".AirbnbStyle__CardContainer-sc-1vh4e1a-2")

# close the webdriver
driver.quit()