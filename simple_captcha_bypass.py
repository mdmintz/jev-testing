# An example of regular CAPTCHA-bypass with SeleniumBase
from seleniumbase import sb_cdp


def bypass_captcha_on_url(url):
    sb = sb_cdp.Chrome()
    sb.goto(url)
    sb.sleep(3)
    sb.solve_captcha()
    sb.sleep(3)
    sb.quit()


if __name__ == "__main__":
    bypass_captcha_on_url("https://dash.cloudflare.com/sign-up")
