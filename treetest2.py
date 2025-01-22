from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# LOG
logging.basicConfig(
    filename="automation_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 瀏覽器
def get_driver():
    driver_path = r"C:\Users\GTW_User\Downloads\chromedriver-win64\chromedriver.exe"
    options = webdriver.ChromeOptions()

    # 行動裝置
    options.add_argument("--window-size=375,990")  # 設定視窗尺寸
    options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_0 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/10.0 Mobile/14A456 Safari/602.1")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def open_menu(driver, menu_button_locator, menu_open_indicator_locator, screenshot_name, timeout=10):
    try:
        menu_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(menu_button_locator)
        )
        logging.info("選單按鈕已成功加載")
        menu_button.click()
        logging.info("成功點擊選單按鈕")

        
        time.sleep(3)

        # 截圖
        screenshot_name = f"{screenshot_name}_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_name)
        logging.info(f"選單展開截圖已儲存: {screenshot_name}")

    except Exception as e:
        logging.error(f"展開選單失敗: {e}")
        error_screenshot_name = f"error_screenshot_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(error_screenshot_name)  # 抓錯誤截圖
        logging.info(f"錯誤截圖已儲存: {error_screenshot_name}")
        raise

def click_product_intro(driver, timeout=10):
    try:
        # 找字
        product_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='產品介紹']"))
        )
        logging.info("已成功定位到 '產品介紹' 按鈕")

        # 點擊按鈕
        product_button.click()
        logging.info("已點擊 '產品介紹' 按鈕")

        # 增加等待時間，確認載入
        time.sleep(3)

        # 截圖新頁
        screenshot_name = f"product_intro_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_name)
        logging.info(f"'產品介紹' 頁面截圖已儲存: {screenshot_name}")

    except Exception as e:
        logging.error(f"點擊 '產品介紹' 按鈕失敗: {e}")
        error_screenshot_name = f"error_screenshot_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(error_screenshot_name)
        logging.info(f"錯誤截圖已儲存: {error_screenshot_name}")
        raise

def click_credit_card(driver, timeout=10):
    try:
        # 定位
        credit_card_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='信用卡']"))
        )
        logging.info("已成功定位到 '信用卡' 按鈕")

        # 點擊按鈕
        credit_card_button.click()
        logging.info("已點擊 '信用卡' 按鈕")

        
        time.sleep(3)

        # 截圖
        screenshot_name = f"credit_card_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_name)
        logging.info(f"'信用卡' 頁面截圖已儲存: {screenshot_name}")

    except Exception as e:
        logging.error(f"點擊 '信用卡' 按鈕失敗: {e}")
        error_screenshot_name = f"error_screenshot_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(error_screenshot_name)
        logging.info(f"錯誤截圖已儲存: {error_screenshot_name}")
        raise

def click_credit_card(driver, timeout=10):
    try:
        # 定位
        credit_card_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='信用卡']"))
        )
        logging.info("已成功定位到 '信用卡' 按鈕")

        # 點擊按鈕
        credit_card_button.click()
        logging.info("已點擊 '信用卡' 按鈕")

        time.sleep(3)

        # 截圖
        screenshot_name = f"credit_card_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_name)
        logging.info(f"'信用卡' 頁面截圖已儲存: {screenshot_name}")

    except Exception as e:
        logging.error(f"點擊 '信用卡' 按鈕失敗: {e}")
        error_screenshot_name = f"error_screenshot_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(error_screenshot_name)
        logging.info(f"錯誤截圖已儲存: {error_screenshot_name}")
        raise

def count_links_in_menu(driver, menu_xpath, timeout=10):
    try:
        # 等待目標出現
        menu_container = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, menu_xpath))
        )
        logging.info("已成功定位到選單")

        # 捲動至目標，子項
        driver.execute_script("arguments[0].scrollIntoView(true);", menu_container)

        # 獲取容器下的所有 <a> 標籤，篩選 id 為 lnk_Link 的項目
        items = menu_container.find_elements(By.XPATH, "./a[@id='lnk_Link']")
        item_count = len(items)
        logging.info(f"選單共有 {item_count} 個子項目")

        return item_count

    except Exception as e:
        logging.error(f"計算選單子項目失敗: {e}")
        raise

def click_card_intro(driver, timeout=10):
    try:
        # 使用 XPath 基於文字內容定位按鈕
        card_intro_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='卡片介紹']"))
        )
        logging.info("已成功定位到 '卡片介紹' 按鈕")

        # 點擊按鈕
        card_intro_button.click()
        logging.info("已點擊 '卡片介紹' 按鈕")

        time.sleep(3)

        # 截圖
        screenshot_name = f"card_intro_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_name)
        logging.info(f"'卡片介紹' 頁面截圖已儲存: {screenshot_name}")

    except Exception as e:
        logging.error(f"點擊 '卡片介紹' 按鈕失敗: {e}")
        error_screenshot_name = f"error_screenshot_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(error_screenshot_name)
        logging.info(f"錯誤截圖已儲存: {error_screenshot_name}")
        raise

def swipe_to_discontinued_cards(driver):
    try:
        # 定位滑動
        swiper_wrapper = driver.find_element(By.CLASS_NAME, "swiper-wrapper")

        # JavaScript 修改 transform
        driver.execute_script(
            "arguments[0].style.transform = 'translate3d(-500px, 0px, 0px)';", 
            swiper_wrapper
        )
        logging.info("滑動到指定位置")

        discontinued_cards_tab = driver.find_element(By.XPATH, "//a[@data-anchor-btn='blockname06']")
        discontinued_cards_tab.click()
        logging.info("已成功點擊 '停發卡' 按鈕")
        time.sleep(2)

        # 截圖
        screenshot_name = f"discontinued_cards_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_name)
        logging.info(f"'停發卡' 頁面截圖已儲存: {screenshot_name}")

    except Exception as e:
        logging.error(f"滑動並點擊 '停發卡' 按鈕失敗: {e}")
        raise

def capture_card_images_in_section(driver, timeout=10):
    try:
        # 定位 section[6] 
        section_container = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/main/article/section[6]")
            )
        )
        logging.info("成功定位 section[6] 容器")

        # 找到 section[6] 下的所有卡片
        card_pic_containers = section_container.find_elements(
            By.CLASS_NAME, "cubre-m-compareCard__pic"
        )
        logging.info(f"在 section[6] 中找到 {len(card_pic_containers)} 個卡片圖片容器")

        # 逐一處理圖片
        total_images = 0
        for index, container in enumerate(card_pic_containers, start=1):
            # 找到容器內的 <img>
            img = container.find_element(By.TAG_NAME, "img")

            # 截圖每個 <img>
            screenshot_name = f"section_6_card_img_{index}_{time.strftime('%Y%m%d_%H%M%S')}.png"
            img.screenshot(screenshot_name)
            logging.info(f"已儲存卡片圖片截圖: {screenshot_name}")
            total_images += 1

        logging.info(f"總共處理了 {total_images} 張卡片圖片")
        return total_images

    except Exception as e:
        logging.error(f"捕獲 section[6] 卡片圖片失敗: {e}")
        raise


























# 主要流程
def main():
    driver = get_driver()

    try:
        driver.get("https://www.cathaybk.com.tw/cathaybk/")

        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        screenshot_name = f"homepage_mobile_{time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_name)
        logging.info(f"行動版截圖已儲存: {screenshot_name}")
        # 打開選單
        open_menu(
            driver,
            menu_button_locator=(By.CSS_SELECTOR, "a.cubre-a-burger"),
            menu_open_indicator_locator=(By.CSS_SELECTOR, "ul.menu-list li"),
            screenshot_name="menu_opened"
        )
        # 點擊 "產品介紹"
        click_product_intro(driver)

        # 點擊 "信用卡"
        click_credit_card(driver)

        # 計算選單項目數量
        menu_xpath = "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]"
        item_count = count_links_in_menu(driver, menu_xpath)
        print(f"選單共有 {item_count} 個項目")

        # 點擊 "卡片介紹"
        click_card_intro(driver)

        # 滾動並點擊 "停發卡"
        swipe_to_discontinued_cards(driver)

        # 捕獲 section[6] 區域內的所有卡片圖片
        total_images = capture_card_images_in_section(driver)
        print(f"截圖完成，卡片圖片總數: {total_images}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
