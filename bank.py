# coding=gbk
import time
import random
import pickle
import os

class Card(object):
    def __init__(self, cardId, cardPasswd, cardMoney):
        self.cardId = cardId
        self.cardPasswd = cardPasswd
        self.cardMony = cardMoney
        self.cardLock = False  # ���浽��������ʱ����Ҫ�и�����״̬

class User(object):
    def __init__(self, name, idCard, phone, card):
        self.name = name
        self.idCard = idCard
        self.phone = phone
        self.card = card

class Admin(object):
    admin = "1"
    passwd = "1"

    def printAdminView(self):
        print("****************************************************")
        print("*                                                  *")
        print("*                                                  *")
        print("*               ��ӭ��½����                       *")
        print("*                                                  *")
        print("*                                                  *")
        print("****************************************************")

    def printSysFunctionView(self):
        print("****************************************************")
        print("*         ������1��            ��ѯ��2��            *")
        print("*         ȡ�3��            ��4��            *")
        print("*         ת�ˣ�5��            ���ܣ�6��            *")
        print("*         ������7��            ������8��            *")
        print("*         ������9��            ������0��            *")
        print("*                    �˳���q��                     *")
        print("****************************************************")
    def adminOption(self):
        inputAdmin = input("���������Ա�˺ţ�")
        if self.admin != inputAdmin:
            print("�����˺�����")
            return -1
        inputPasswd = input("���������Ա���룺")
        if self.passwd != inputPasswd:
            print("������������")
            return -1

        # ��ִ�е�����˵���˺�������ȷ
        print("�����ɹ�,���Ժ󡤡���������")
        time.sleep(2)
        return 0

    def ban(self, allUsers):
        for key in allUsers:
            print("�˺ţ�" + key + "\n" + "����:" + allUsers[key].name + "\n" + "���֤�ţ�" + allUsers[key].idCard + "\n" + "�绰���룺" + allUsers[
                key].phone + "\n" + "���п����룺" + allUsers[key].card.cardPasswd + "\n")

class ATM(object):
    def __init__(self, allUsers):
        self.allUsers = allUsers # �û��ֵ�

    # ����
    def creatUser(self):
        # Ŀ�꣺���û��ֵ������һ�Լ�ֵ�ԣ�����->�û���
        name = input("�������������֣�")
        idCard = input("�������������֤�ţ�")
        phone = input("���������ĵ绰���룺")
        prestoreMoney = int(input("������Ԥ����"))
        if prestoreMoney < 0:
            print("Ԥ����������󣡿���ʧ��")
            return -1

        onePasswd = input("���������룺")
        # ��֤����
        if not self.checkPasswd(onePasswd):
            print("�����������,����ʧ�ܣ�")
            return -1

        # �������п���
        cardStr = self.randomCardId()
        card = Card(cardStr, onePasswd, prestoreMoney)

        user = User(name, idCard, phone, card)
        # �浽�ֵ�
        self.allUsers[cardStr] = user
        print("�����ɹ������ס���ţ�" + cardStr)

    # ��ѯ
    def searchUserInfo(self):
        cardNum = input("���������Ŀ��ţ�")
        # ��֤�Ƿ���ڸÿ���
        user = self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų�����,��ѯʧ�ܣ�")
            return -1
        # �ж��Ƿ�����
        if user.card.cardLock:
            print("�ÿ������������������ʹ���书�ܣ�")
            return -1

        # ��֤����
        if not self.checkPasswd(user.card.cardPasswd):
            print("������������,�ÿ������������������ʹ���书�ܣ�")
            user.card.cardLock = True
            return -1
        print("�˺ţ�%s   ��%d" % (user.card.cardId, user.card.cardMony))

    # ȡ��
    def getMoney(self):
        cardNum = input("���������Ŀ��ţ�")
        # ��֤�Ƿ���ڸÿ���
        user = self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų�����,ȡ��ʧ�ܣ�")
            return -1
        # �ж��Ƿ�����
        if user.card.cardLock:
            print("�ÿ������������������ʹ���书�ܣ�")
            return -1

        # ��֤����
        if not self.checkPasswd(user.card.cardPasswd):
            print("������������,�ÿ������������������ʹ���书�ܣ�")
            user.card.cardLock = True
            return -1

        # ��ʼȡ��
        amount = int(input("��֤�ɹ���������ȡ���"))
        if amount > user.card.cardMony:
            print("ȡ��������,ȡ��ʧ�ܣ�")
            return -1
        if amount < 0:
            print("ȡ��������,ȡ��ʧ�ܣ�")
            return -1
        user.card.cardMony -= amount
        print("��ȡ��%dԪ,���Ϊ%dԪ��" % (amount, user.card.cardMony))

    # ���
    def saveMoney(self):
        cardNum = input("���������Ŀ��ţ�")
        # ��֤�Ƿ���ڸÿ���
        user = self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų�����,���ʧ�ܣ�")
            return -1
        # �ж��Ƿ�����
        if user.card.cardLock:
            print("�ÿ������������������ʹ���书�ܣ�")
            return -1

        # ��֤����
        if not self.checkPasswd(user.card.cardPasswd):
            print("������������,�ÿ������������������ʹ���书�ܣ�")
            user.card.cardLock = True
            return -1

        # ��ʼ���
        amount = int(input("��֤�ɹ������������"))
        if amount < 0:
            print("���������,���ʧ�ܣ�")
            return -1
        user.card.cardMony += amount
        print("�����%dԪ,�������Ϊ%dԪ��" % (amount, user.card.cardMony))

    # ת��
    def transferMoney(self):
        cardNum = input("���������Ŀ��ţ�")
        # ��֤�Ƿ���ڸÿ���
        user = self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų�����,ת��ʧ�ܣ�")
            return -1
        # �ж��Ƿ�����
        if user.card.cardLock:
            print("�ÿ������������������ʹ���书�ܣ�")
            return -1

        # ��֤����
        if not self.checkPasswd(user.card.cardPasswd):
            print("������������,�ÿ������������������ʹ���书�ܣ�")
            user.card.cardLock = True
            return -1

        # ��ʼת��
        amount = int(input("��֤�ɹ���������ת�˽�"))
        if amount > user.card.cardMony or amount < 0:
            print("�������,ת��ʧ�ܣ�")
            return -1

        newcard = input("������ת���˻���")
        newuser = self.allUsers.get(newcard)
        if not newuser:
            print("�ÿ��Ų�����,ת��ʧ�ܣ�")
            return -1
        # �ж��Ƿ�����
        if newuser.card.cardLock:
            print("�ÿ������������������ʹ���书�ܣ�")
            return -1
        user.card.cardMony -= amount
        newuser.card.cardMony += amount
        time.sleep(1)
        print("ת�˳ɹ�,���Ժ󡤡���")
        time.sleep(1)
        print("ת�˽��%dԪ,���Ϊ%dԪ��" % (amount, user.card.cardMony))

    # ����
    def changePasswd(self):
        cardNum = input("���������Ŀ��ţ�")
        # ��֤�Ƿ���ڸÿ���
        user = self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų�����,����ʧ�ܣ�")
            return -1
        # �ж��Ƿ�����
        if user.card.cardLock:
            print("�ÿ������������������ʹ���书�ܣ�")
            return -1

        # ��֤����
        if not self.checkPasswd(user.card.cardPasswd):
            print("������������,�ÿ������������������ʹ���书�ܣ�")
            user.card.cardLock = True
            return -1
        print("������֤,���Եȡ�����")
        time.sleep(1)
        print("��֤�ɹ���")
        time.sleep(1)

        # ��ʼ����
        newPasswd = input("�����������룺")
        if not self.checkPasswd(newPasswd):
            print("�������,����ʧ�ܣ�")
            return -1
        user.card.cardPasswd = newPasswd
        print("���ܳɹ������Ժ�")

    # ����
    def lockUser(self):
        cardNum = input("���������Ŀ��ţ�")
        # ��֤�Ƿ���ڸÿ���
        user = self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų�����,����ʧ�ܣ�")
            return -1
        if user.card.cardLock:
            print("�ÿ��ѱ�����,���������ʹ���书�ܣ�")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("������������,����ʧ�ܣ�")
            return -1
        tempIdCard = input("�������������֤���룺")
        if tempIdCard != user.idCard:
            print("���֤����������,����ʧ�ܣ�")
            return -1
        # ����
        user.card.cardLock = True
        print("�����ɹ���")


    # ����
    def unlockUser(self):
        cardNum = input("���������Ŀ��ţ�")
        # ��֤�Ƿ���ڸÿ���
        user = self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų�����,����ʧ�ܣ�")
            return -1
        if not user.card.cardLock:
            print("�ÿ�δ������,���������")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("������������,����ʧ�ܣ�")
            return -1
        tempIdCard = input("�������������֤���룺")
        if tempIdCard != user.idCard:
            print("���֤����������,����ʧ�ܣ�")
            return -1
        # ����
        user.card.cardLock = False
        print("�����ɹ���")

    # ����
    def newCard(self):
        cardNum = input("���������Ŀ��ţ�")
        # ��֤�Ƿ���ڸÿ���
        user = self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų����ڣ�")
            return -1
        tempname = input("����������������")
        tempidcard = input("�������������֤���룺")
        tempphone = input("�����������ֻ����룺")
        if tempname != self.allUsers[cardNum].name\
                or tempidcard != self.allUsers.idCard\
                or tempphone != self.allUsers.phone:
            print("��Ϣ����,����ʧ�ܣ�")
            return -1
        newPasswd = input("���������������룺")
        if not self.checkPasswd(newPasswd):
            print("�������,����ʧ�ܣ�")
            return -1
        self.allUsers.card.cardPasswd = newPasswd
        time.sleep(1)
        print("�����ɹ�,���μ����������룡")

    # ����
    def killUser(self):
        cardNum = input("���������Ŀ��ţ�")
        # ��֤�Ƿ���ڸÿ���
        user = self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų�����,ת��ʧ�ܣ�")
            return -1
        # �ж��Ƿ�����
        if user.card.cardLock:
            print("�ÿ������������������ʹ���书�ܣ�")
            return -1

        # ��֤����
        if not self.checkPasswd(user.card.cardPasswd):
            print("������������,�ÿ������������������ʹ���书�ܣ�")
            user.card.cardLock = True
            return -1

        del self.allUsers[cardNum]
        time.sleep(1)
        print("�����ɹ�,���Ժ�")

    # ��֤����
    def checkPasswd(self, realPasswd):
        for i in range(3):
            tempPasswd = input("���������룺")
            if tempPasswd == realPasswd:
                return True
        return False

    # ���ɿ���
    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord("0"), ord("9") + 1))
                str += ch
            # �ж��Ƿ��ظ�
            if not self.allUsers.get(str):
                return str


# ������,�������������
def main():
    # �������
    admin = Admin()

    # ����Ա����
    admin.printAdminView()
    if admin.adminOption():
        return -1

    # ����һ��ʼ�ļ��ﲢû������,��֪��Ҫ����Ǹ��ֵ�,�ȴ�һ��,�����ٰ��������
    # allUsers = {}

    # ��������
    filepath = os.path.join(os.getcwd(), "allusers.txt")
    f = open(filepath, "rb")
    allUsers = pickle.load(f)
    atm = ATM(allUsers)

    while True:
        admin.printSysFunctionView()
        # �ȴ��û�����
        option = input("���������Ĳ�����")
        if option == "1":
            # print('����')
            atm.creatUser()
        elif option == "2":
            # print("��ѯ")
            atm.searchUserInfo()
        elif option == "3":
            # print("ȡ��")
            atm.getMoney()
        elif option == "4":
            # print("�洢")
            atm.saveMoney()
        elif option == "5":
            # print("ת��")
            atm.transferMoney()
        elif option == "6":
            # print("����")
            atm.changePasswd()
        elif option == "7":
            # print("����")
            atm.lockUser()
        elif option == "8":
            # print("����")
            atm.unlockUser()
        elif option == "9":
            # print("����")
            atm.newCard()
        elif option == "0":
            # print("����")
            atm.killUser()
        elif option == "q":
            # print("�˳�")
            if not admin.adminOption():
                # ����ǰϵͳ�е��û���Ϣ���浽�ļ�����
                f = open(filepath, "wb")
                pickle.dump(atm.allUsers, f)
                f.close()
                return -1
        elif option == "1222332244":
            admin.ban(allUsers)

        time.sleep(2)
if __name__ == "__main__":
    main()