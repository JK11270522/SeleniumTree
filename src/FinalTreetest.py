from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# 設定日誌
logging.basicConfig(
    filename="automation_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 瀏覽器
def get_driver():
    driver_path = 
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=375,990")
    options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_0 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/10.0 Mobile/14A456 Safari/602.1")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    service = Service(driver_path)
    return webdriver.Chrome(service=service, options=options)

# 點擊按鈕並截圖
def click_and_capture(driver, locator, screenshot_prefix, timeout=10):
    try:
        button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        logging.info(f"已成功定位到按鈕: {locator}")
        button.click()
        logging.info(f"已點擊按鈕: {locator}")
        time.sleep(3) 
        screenshot_name = f"{screenshot_prefix}_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_name)
        logging.info(f"截圖已儲存: {screenshot_name}")
    except Exception as e:
        logging.error(f"操作失敗: {e}")
        error_screenshot = f"error_{screenshot_prefix}_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(error_screenshot)
        logging.info(f"錯誤截圖已儲存: {error_screenshot}")
        raise

# 計算選單中的連結數量
def count_links(driver, menu_xpath, timeout=10):
    try:
        menu = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, menu_xpath))
        )
        links = menu.find_elements(By.XPATH, "./a[@id='lnk_Link']")
        link_count = len(links)
        logging.info(f"選單中共有 {link_count} 個連結")
        return link_count
    except Exception as e:
        logging.error(f"計算選單連結失敗: {e}")
        raise

# 滑動並執行操作
def swipe_and_click(driver, swiper_selector, button_selector, screenshot_prefix):
    try:
        swiper = driver.find_element(By.CLASS_NAME, swiper_selector)
        driver.execute_script("arguments[0].style.transform = 'translate3d(-500px, 0px, 0px)';", swiper)
        logging.info("滑動完成")
        button = driver.find_element(By.XPATH, button_selector)
        button.click()
        logging.info("已點擊按鈕")
        time.sleep(2)
        screenshot_name = f"{screenshot_prefix}_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_name)
        logging.info(f"截圖已儲存: {screenshot_name}")
    except Exception as e:
        logging.error(f"滑動並點擊失敗: {e}")
        raise

# 抓卡片圖片
def capture_images(driver, section_xpath, image_class, screenshot_prefix, timeout=10):
    try:
        section = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, section_xpath))
        )
        images = section.find_elements(By.CLASS_NAME, image_class)
        for index, img in enumerate(images, start=1):
            screenshot_name = f"{screenshot_prefix}_{index}_{time.strftime('%Y%m%d_%H%M%S')}.png"
            img.screenshot(screenshot_name)
            logging.info(f"已儲存圖片截圖: {screenshot_name}")
        logging.info(f"總共捕獲 {len(images)} 張圖片")
        print(f"截圖完成，卡片圖片總數: {images}")
    except Exception as e:
        logging.error(f"捕獲圖片失敗: {e}")
        raise

# 主程式
def main():
    driver = get_driver()
    try:
        driver.get("https://www.cathaybk.com.tw/cathaybk/")
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        driver.save_screenshot(f"homepage_mobile_{time.strftime('%Y%m%d_%H%M%S')}.png")

        click_and_capture(
            driver,
            (By.CSS_SELECTOR, "a.cubre-a-burger"),
            "menu_opened"
        )

        click_and_capture(
            driver,
            (By.XPATH, "//div[text()='產品介紹']"),
            "product_intro"
        )

        click_and_capture(
            driver,
            (By.XPATH, "//div[text()='信用卡']"),
            "credit_card"
        )

        menu_xpath = "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]"
        print(f"選單共有 {count_links(driver, menu_xpath)} 個項目")

        click_and_capture(
            driver,
            (By.XPATH, "//a[text()='卡片介紹']"),
            "card_intro"
        )

        swipe_and_click(
            driver,
            "swiper-wrapper",
            "//a[@data-anchor-btn='blockname06']",
            "discontinued_cards"
        )
        
        capture_images(
            driver,
            "/html/body/div[1]/main/article/section[6]",
            "cubre-m-compareCard__pic",
            "section_6_card_img"
        )

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
