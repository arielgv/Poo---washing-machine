#Definition
class Washer:
    def __init__(self):
        pass

    def wash(self, temperature='90~'):
        self.temperature = temperature
        self._addingwater(temperature)
        self._soap()
        self._washing(temperature)
        self._drying()
    
    def _addingwater(self,temperature):
        print (f'Starting.. \n Adding water at {temperature} degrees.')
    def _soap(self):
        print(f'Adding soap.')
    def _washing(self,temperature):
        print(f'Start washing process at {temperature} degrees.')
    def _drying(self):
        print(f'Finishing the process. Drying.')

if __name__=='__main__':
    Philips = Washer()
    degrees=input('Pick the temperature: (enter for 90) ')
    if degrees == '':
        degrees = 90
    else:
        pass
    Philips.wash(degrees)

