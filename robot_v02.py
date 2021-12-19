from RPA.Browser.Selenium import Selenium
import time
import pandas as pd

browser_lib = Selenium()
organisation_to_search = "National Science Foundation"


def open_the_website(url):
    browser_lib.open_available_browser(url)
    browser_lib.maximize_browser_window()


def headings():
    browser_lib.click_element("class:tuck-7")
    time.sleep(10)
    tuck5s = browser_lib.find_elements("class:tuck-5")
    agencies_str = []
    for item in tuck5s:
        if "Department" in item.text or "Administration" in item.text or "Agency" in item.text or "Corps" in item.text or "Foundation" in item.text or "Commission" in item.text:
            agencies_str.append(item.text)

    agencies_list = []
    for item in agencies_str:
        temp_list = item.split("\n")
        list_agency_and_value = [x for x in temp_list if "view" not in x and "Total" not in x]
        agencies_list.append(list_agency_and_value)

    with open('agencies.xlsx', 'w') as file:
        df = pd.DataFrame({
            "Agency": [x[0] for x in agencies_list],
            "Amount": [x[1] for x in agencies_list]
        })

        df.to_excel('agencies.xlsx')


def specific_agency():
    browser_lib.click_element("class:tuck-7")
    time.sleep(7)
    tuck5s = browser_lib.find_elements("class:tuck-5")
    for item in tuck5s:
        if organisation_to_search in item.text:
            link = browser_lib.find_elements("tag:a", parent=item)
            href = browser_lib.get_element_attribute(link, "href")
            browser_lib.open_available_browser(href)
    browser_lib.maximize_browser_window()
    browser_lib.scroll_element_into_view("css:h3")
    browser_lib.click_element("css:footer")
    time.sleep(10)
    browser_lib.scroll_element_into_view("css:footer")
    time.sleep(10)

    table_data = []

    table_page = browser_lib.find_elements("tag:td")
    for item in table_page:
        table_data.append(item.text)

    # While next button doesn't have attribute disabled
    next_button = browser_lib.find_element("class:next")
    next_button_attributes = browser_lib.get_element_attribute(next_button, "class")
    browser_lib.click_element("class:next")
    time.sleep(15)

    while True:
        table_page = browser_lib.find_elements("tag:td")
        for item in table_page:
            table_data.append(item.text)

        if "disabled" in next_button_attributes:
            break

        browser_lib.click_element("class:next")
        time.sleep(15)
        next_button = browser_lib.find_element("class:next")
        next_button_attributes = browser_lib.get_element_attribute(next_button, "class")

    individual_investments_splited_cells = []
    for item in table_data:
        if len(item):
            individual_investments_splited_cells.append(item)

    individual_investments = [individual_investments_splited_cells[i: i + 7] for i in range(0, len(individual_investments_splited_cells), 7)]
    df = pd.DataFrame({
        "UII": [x[0] for x in individual_investments],
        "Bureau": [x[1] for x in individual_investments],
        "Investment Title": [x[2] for x in individual_investments],
        "Total FY2021 Spending ($M)": [x[3] for x in individual_investments],
        "Type": [x[4] for x in individual_investments],
        "CIO Rating": [x[5] for x in individual_investments],
        "# of Projects": [x[6] for x in individual_investments],
    })

    df.to_excel('individual_investments.xlsx')

def store_screenshot(filename):
    browser_lib.screenshot(filename=filename)


# Define a main() function that calls the other functions in order:
def main():
    try:
        open_the_website("https://itdashboard.gov/")
        # headings()
        specific_agency()
        store_screenshot("output/current_state_of_business.png")
    finally:
        browser_lib.close_all_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()
