import requests, json


class RunMain:
    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return res

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return res

    def run_main(self, url, method, id=None):
        res = None
        if method == 'GET':
            if id:
                url = url.replace("all", "detail") + str(id)
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    run = RunMain()
    url = "http://127.0.0.1:8000/datalist/all/"
    data = {"name": "User8",
            "city": "LA",
            "cardnumber": "5105105105105100",
            "phonenumber": "(319)-883-4480",
            "created": "Sun, 23 Feb 2020 08:18:51 GMT",
            "token": "7f38e7a645fbd1b3c68fbc75ecd62d24"
            }
    data1 = {"name": "User8"}
    print(run.run_main(url, 'POST', data))
    print(run.run_main(url, 'GET', 1))
    print(run.run_main(url, 'GET'))
