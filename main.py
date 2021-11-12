from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GPUBot:
    DRIVER_PATH = "/usr/bin/chromedriver"

    BEST_BUY_URLS = {
        "RTX 3080": [
            "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440",
            "https://www.bestbuy.com/site/evga-rtx-3080-xc3-ultra-gaming-10g-p5-3885-kh-pci-express-4-0-lhr/6471615.p?skuId=6471615"
        ],
        "RTX 3080 Ti": [
            "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-ti-12gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6462956.p?skuId=6462956",
            "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3080-ti-ftw3-ultra-gaming-12gb-gddr6x-pci-express-4-0-graphics-card/6467808.p?skuId=6467808",
            "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-ti-gaming-oc-12gb-gddr6x-pci-express-4-0-graphics-card/6466561.p?skuId=6466561",
        ],
        "RTX 3090": [
            "https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434"
        ]
    }

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.DRIVER_PATH)

    def check_best_buy(self):
        for name, urls in self.BEST_BUY_URLS.items():
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] Checking BestBuy inventory for {name}...")
            for url in urls:
                self.driver.get(url)
                try:
                    add_to_cart_button = WebDriverWait(self.driver, 1).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
                    )
                except Exception as e:
                    # self.driver.refresh()
                    continue
                else:
                    print(f"[{timestamp}] ==> Found inventory for {name} <==", flush=True)
                    print(f"[{timestamp}] ==> URL: {url}", flush=True)

    def run(self):
        while True:
            try:
                self.check_best_buy()
            except KeyboardInterrupt:
                exit(1)


if __name__ == "__main__":
    bot = GPUBot()
    bot.run()
