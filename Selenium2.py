from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# options.add_argument("--headless") # 若要無頭模式

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

wait = WebDriverWait(driver, 15)

# STEP 1: 先前往登入頁面
driver.get("https://kktix.com/users/sign_in")

# 等待頁面加載，輸入帳號密碼登入
wait.until(EC.visibility_of_element_located((By.ID, "user_login"))).send_keys("n995526@ntub.edu.tw")
wait.until(EC.visibility_of_element_located((By.ID, "user_password"))).send_keys("Hs350149")

# 點擊登入按鈕
wait.until(EC.element_to_be_clickable((By.NAME, "commit"))).click()

# 等待登入完成（例如等待個人資料顯示或首頁元素出現）
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".profile, .header, .navbar")))

# STEP 2: 登入完成後再前往購票頁面
driver.get("https://kktix.com/events/donghaeeastcoastwave-01")

wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "立即購票"))).click()

# 增加票券
increase_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='quantityBtnClick(1)']")))
increase_btn.click()

# 個人服務條款同意按鈕
agree_checkbox = wait.until(EC.element_to_be_clickable(
    (By.ID, "person_agree_terms"))
)

# 點擊勾選
agree_checkbox.click()

next_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@ng-click='challenge()' and .//span[text()='下一步']]")
    )
)

next_btn.click()


input("按 Enter 後關閉瀏覽器...")
driver.quit()