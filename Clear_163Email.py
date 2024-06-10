from DrissionPage import ChromiumPage, ChromiumOptions
import time as time

co = ChromiumOptions().set_paths(browser_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                                 user_data_path=r'C:\Users\ASUS\AppData\Local\Microsoft\Edge\User Data\Default',
                                 local_port=9999)
co.set_pref('profile.default_content_settings.popups', 0)  # 禁止所有弹出窗口
co.set_pref('credentials_enable_service', False)  # 隐藏是否保存密码的提示

# 禁止所有弹出窗口
co.set_pref(arg='profile.default_content_settings.popups', value='0')
# 隐藏是否保存密码的提示
co.set_pref('credentials_enable_service', False)
page = ChromiumPage(co)  # 创建对象
page.get(' 在这里粘贴你的网易163邮箱网站地址 ')


def get_fly_button_xpath(number):
    # 构造 XPath 字符串，将数字插入到 'fly' 后面
    return f'x://*[@id="fly{number}"]'


def delete_emails_on_current_page(page, page_number):
    time.sleep(1)
    # 使用辅助函数生成全选按钮的 XPath，并点击
    fly_button_xpath = get_fly_button_xpath(page_number)
    page.ele(fly_button_xpath).click()
    time.sleep(1.3)
    # 点击删除按钮
    page.ele("x://span[@class='nui-btn-text' and text()='删 除']").click()
    time.sleep(0.5)


# 处理删除操作
def process_deletion(page):
    # 获取用户输入的页面数
    pages_to_delete = input("请输入您希望删除的页面数（数字）: ")
    time.sleep(1)  # 等待收件箱加载

    try:
        pages_to_delete = int(pages_to_delete)  # 尝试将输入转换为整数
        if pages_to_delete <= 0:
            print("请输入一个正数。")
            return
    except ValueError:
        print("输入无效，请输入一个数字。")
        return

    # 执行删除操作
    for page_number in range(1, pages_to_delete + 1):
        delete_emails_on_current_page(page, page_number)
        print(f"已删除第 {page_number} 页的邮件。")


# 开始处理所有页面的邮件
if __name__ == "__main__":
    process_deletion(page)

# 最后关闭浏览器
page.close()
