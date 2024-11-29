from playwright.sync_api import sync_playwright


def substring_after(s, sep):
    return s.partition(sep)[2]

def safe_text_content(page, selector):
    try:
        # Attempt to get the text content of the selector
        return page.text_content(selector)
    except Exception:
        # Ignore the error and return None
        return None

def get_car_valuation(registration, mileage):
    url = "https://www.webuyanycar.com/car-valuation/"

    with sync_playwright() as p:
        # Launch a headless browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Navigate to the valuation page
        page.goto(url)
        page.click('button:has-text("Accept all")')
        page.get_by_placeholder("Enter your reg").fill(registration)
        page.get_by_placeholder("Mileage").fill(str(mileage))
        page.click('button:has-text("Get my car valuation")')

        error = safe_text_content(page, ".text-start")
        print(f"{registration} : Error Not Found : {error}")

        if error:
            return [registration, "Invalid Vehicle"]

        manufacture = page.text_content('.spec-manufacturer')
        full_spec = page.text_content('.spec-full-name')
        divs = page.locator("div.col-6.spec-value")
        year = divs.nth(1).text_content()
        reg = divs.nth(0).text_content()

        # Close the browser
        browser.close()

        #Return Final
        man_str =  substring_after(full_spec, " ")
        return[reg, manufacture, man_str, year]


if __name__ == "__main__":
    # Example usage
    registration_number = "KT17DLX"  # Replace with a valid registration number
    mileage_value = 15000  # Replace with the car's mileage
    result1 = get_car_valuation(registration_number, mileage_value)
    print(result1)
