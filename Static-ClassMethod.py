
class ClassTest:
  def instance_method(self):
    print(f"Chamando instance_method of {self}")

  @classmethod
  def class_method(cls):
    print(f"Chamando class_method of {cls}")

  @staticmethod
  def static_method():
    print("Chamando static_method")



ClassTest.static_method()    

ClassTest.class_method() 
