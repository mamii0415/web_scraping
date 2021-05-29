from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
import urllib.parse


def translation(english):

    # ヘッドレスモードに設定
    options = Options()
    options.add_argument('--headless')

    # ブラウザの起動
    browser = webdriver.Firefox(options=options)

    # エンコード
    encode = urllib.parse.quote_plus(english)

    # Google翻訳(翻訳したい単語を代入済み)にアクセス
    url = 'https://translate.google.co.jp/#en/ja/{}'.format(encode)
    browser.get(url)

    # 翻訳結果の抽出
    sleep(5)  # 数秒待機
    result = browser.find_element_by_css_selector("span[jsname='W297wb']")
    return result.text

    # ブラウザを閉じる
    browser.quit()


print(translation(input()))
