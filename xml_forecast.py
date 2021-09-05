import xml.etree.ElementTree as ET


class TemperatureConverter:

    def convert_celsius_to_fahrenheit(self, file):

        tree2 = ET.parse(file)
        root = tree2.getroot()

        for temp in root.iter('temperature_in_celsius'):

            temp = temp.text

            temp = int(temp)

            temp = 9/5 * temp + 32

            print(f'{temp:.2f}')
