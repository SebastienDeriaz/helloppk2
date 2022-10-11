"""
PPK2 test file
"""
# Import python packages
from msilib.schema import Error
import numpy as np
from time import sleep
# Import PPK2 API
from ppk2_api.ppk2_api import PPK2_API

COM_PORT = "COM5"

# Example from https://github.com/IRNAS/ppk2-api-python

# Open COM port
ppk2 = PPK2_API(COM_PORT)

ppk2.get_modifiers()
ppk2.use_source_meter()  # set source meter mode
ppk2.set_source_voltage(3300)  # set source voltage in mV
ppk2.start_measuring()  # start measuring

sleep(0.4)
# read measured values in a for loop like this:
read_data = ppk2.get_data()
if read_data != b'':
    samples = np.array(ppk2.get_samples(read_data))
    print(f"Average of {samples.size} samples is: {np.mean(samples)}uA")

    print(f"Samples : {samples}")

ppk2.stop_measuring()

