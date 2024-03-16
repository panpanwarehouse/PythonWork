class Product:

    def __init__(self, name, describe, price, invention=0):
        self.name = name
        self.describe = describe
        self.price = price
        self.invention = invention

    def __str__(self):
        return '名称：《%s》 描述：%s 价格：%s\n库存量：%s ' % (self.name, self.describe, self.price, self.invention)

class ProductManager:
    products = []

    def __init__(self):
        product1 = Product('纤排', '带脊骨', 19.9,100)
        product2 = Product('蒙牛特仑苏纯牛奶', '250ml*12', 55,1500)
        product3 = Product('心相印茶语纸巾', '120抽*10包', 33.6, 1000)
        self.products.append(product1)
        self.products.append(product2)
        self.products.append(product3)

    def menu(self):
        print('欢迎使用超市商品管理系统\n')
        while True:
            print('1.查看所有商品\n2.添加商品\n3.销售商品\n4.检查库房\n5.补货\n6.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_all_product()
            elif choice == 2:
                self.add_product()
            elif choice == 3:
                self.sale_product()
            elif choice == 4:
                self.check_product()
            elif choice == 5:
                self.replenish_product()
            elif choice == 6:
                self.exit_system()
                break

    def show_all_product(self):
        print('商品信息如下：')
        for product in self.products:
            print(product)
            print('')

    def add_product(self):
        new_name = input('请输入商品名称：')
        new_describe = input('请输入商品描述：')
        new_price = input('请输入商品单价：')
        new_invention = input('请输入库存量：')
        new_product = Product(new_name, new_describe, new_price,new_invention)
        self.products.append(new_product)
        print('商品录入成功！\n')

    def check_product(self):
        name = input("输入货品名称")
        for product in self.products:
            if product.name == name:
                print(product.invention)
                return
        else:
            print("无该商品信息！")

    def sale_product(self):
        name = input('请输入商品名称：')
        num=int(input("请输入要销售的数量："))
        for product in self.products:
            if product.name==name:
                if product.invention>=num:
                    sum=num*product.price
                    print("销售成功!总价为:{}".format(sum))
                    product.invention-=num
                else:
                    print("销售失败，库存不足！")
                return
                print("无该商品信息!")



    def replenish_product(self):
        name = input('请输入补货的商品名称：')
        num = int(input('请输入补货数量：'))
        for product in self.products:
            if product.name==name:
                product.invention+=num
                print("补货成功!")
                return
            else:
                print("无该商品信息!")
    def exit_system(self):
        print("感谢使用!!!")

manager = ProductManager()
manager.menu()