import requests


class Test1:
    def __init__(self):
        self.s = requests.Session()

    """
    获取svn信息
    """

    def getsvnlist(self):
        res = self.s.get(url="http://10.96.163.20:8080/view/201717_MDU_EOC_LMT/job/2017427-MDU-AN5142_CT-coverity/260/")
        str1 = res.text
        list1 = str1.split()
        list2 = []
        flag = 0
        for value in list1:
            if "Changes" in value:
                flag = 0
            if flag == 1:
                list2.append(value)
            if "Revisions" in value:
                flag = 1
        str2 = ''.join(list2)
        list2 = str2.split("</li><li>")
        for value in list2:
            if value.find("<ul><li>") != -1:
                value = value.replace("<ul><li>", '')
            if value.find("</li></ul>") != -1:
                value = value.replace("</li></ul>", '')
            print(value)
        return value


if __name__ == '__main__':
    T1 = Test1().getsvnlist()
    print(T1)
