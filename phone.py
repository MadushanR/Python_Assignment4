class Phone:

    def __init__(self,imei,brand,model):
        self.imei = imei
        self.brand = brand
        self.model = model

    def getImei(self):
        return self.imei

    def getBrand(self):
        return self.brand
    
    def getModel(self):
        return self.model
    
    def setImei(self,imei):
        self.imei = imei

    def setBrand(self,brand):
        self.brand = brand

    def setModel(self,model):
        self.model = model