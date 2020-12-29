"""
This problem was asked by Microsoft.

Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances. And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), return the second instance.
"""
call_times = 0


class String:
    def __init__(self):
        self.string = None

    def get_instance(self):
        global call_times
        call_times += 1
        first_instance = String()
        first_instance.string = "instance 1"
        second_instance = String()
        second_instance.string = "instance 2"
        if call_times % 2 == 0:
            return first_instance
        else:
            return second_instance


# Driver code
for i in range(6):
    obj = String().get_instance()
    print("".join("Call n°" + str(i)) + ":")
    print(obj.string)
