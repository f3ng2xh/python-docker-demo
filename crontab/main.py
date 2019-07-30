from module.helloworld import hello_world
import requests

if __name__ == '__main__':
    # test inner modules
    hello_world()

    # test require modules
    response =requests.get("http://www.baidu.com")
    response.encoding="utf-8"
    print(response.text)
