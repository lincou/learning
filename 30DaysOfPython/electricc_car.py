"""一次模拟汽车的简单尝试"""


class Car:
    def __init__(self, make, model, year): 
          self.make = make 
          self.model = model 
          self.year = year 
          self.odometer_reading = 0 
 
    def get_descriptive_name(self): 
        long_name = f"{self.year} {self.make} {self.model}" 
        return long_name.title() 

    def read_odometer(self): 
        print(f"This {self.make} {self.model} has {self.odometer_reading} miles on it.") 

    def update_odometer(self, mileage): 
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage 
        else: 
            print("You can't roll back an odometer!") 

    def increment_odometer(self, miles): 
        self.odometer_reading += miles

class Battery: 
    def __init__(self, battery_size=70): 
        self.battery_size = battery_size 
        self.battery_level = 70 
 
    def describe_battery(self): 
        print(f"This car has a {self.battery_size}-kWh battery.") 
 
    def get_range(self): 
        if self.battery_level == 70: 
            range = 240 
        elif self.battery_level == 100: 
            range = 300 
        else: 
            range = self.battery_level * 10 
        print(f"This car can go about {range} miles on a full charge.") 
 
    def upgrade_battery(self): 
        if self.battery_level == 70: 
            self.battery_level = 100 
            print("Battery upgraded to a high-capacity model.") 
        else: 
            print("This car already has a high-capacity battery.") 

class ElectricCar(Car,Battery): 
    def __init__(self, make, model, year): 
        super().__init__(make, model, year) 
        self.battery = Battery()

# xiaomiSu7 = ElectricCar("Xiaomi", "SU7", 2021) 
# xiaomiSu7.battery.get_range() 
# xiaomiSu7.battery.upgrade_battery() 
# xiaomiSu7.battery.get_range() 

