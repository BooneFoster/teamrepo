class Invoice:

        def __init__(self):
            self.items = {}


        def totalImpurePrice(self, products):
            total_impure_price = 0
            for k, v in products.items():
                total_impure_price += float(v['unit_price']) * int(v['qnt'])
            total_impure_price = round(total_impure_price, 2)
            return total_impure_price

        def addProduct(self, qnt, price, discount, tax, fee):
            self.items['qnt'] = qnt
            self.items['unit_price'] = price
            self.items['discount'] = discount
            self.items['tax'] = tax
            self.items['fee'] = fee
            return self.items

        def totalDiscount(self, products):
            total_discount = 0
            for k, v in products.items():
                total_discount += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount']) / 100
            total_discount = round(total_discount, 2)
            self.total_discount = total_discount
            return total_discount

        def totalPurePrice(self, products):
            total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
            return total_pure_price

        def inputAnswer(self, input_value):
            while True:
                userInput = input(input_value)
                if userInput in ['y', 'n']:
                    return userInput
                print("y or n! Try again.")

        def inputNumber(self, input_value):
            while True:
                try:
                    userInput = float(input(input_value))
                except ValueError:
                    print("Not a number! Try again.")
                    continue
                else:
                    return userInput

        def salesTax(self, products):
            totalTax = 0
            for k, v in products.items():
                totalTax += (int(v['qnt']) * float(v['unit_price']) - (int(v['qnt']) * float(v['unit_price'])) \
                            * float(v['discount']) / 100) * float(v['tax']) / 100
            totalTax = round(totalTax, 2)
            self.totalTax = totalTax
            return totalTax

        def taxPrice(self, products):
            total_tax_price = (self.totalImpurePrice(products) - self.totalDiscount(products)) + self.salesTax(products)
            return total_tax_price

        def deliveryPrice(self, products):
            totalFee = 0
            for k, v in products.items():
                totalFee += float(v['fee'])
            totalFee = round(totalFee, 2)
            self.totalFee = totalFee
            total_delivery_price = (self.totalImpurePrice(products) - self.totalDiscount(products)
                                    + self.salesTax(products) + totalFee)
            return total_delivery_price

