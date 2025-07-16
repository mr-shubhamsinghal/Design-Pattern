
class Subscriber:
    def update(self):
        print("publisher is updated")

class Publisher:
    def __init__(self, name):
        self.name = name
        self.subscriber = []
    
    def subscribe(self, subscriber):
        self.subscriber.append(subscriber)
    
    def update_name(self, name):
        self.name = name
        self.notify_observers()
    
    def notify_observers(self):
        for subscriber in self.subscriber:
            subscriber.update()

pub = Publisher('Subh')
pub.subscribe(Subscriber())
pub.update_name("bro")

