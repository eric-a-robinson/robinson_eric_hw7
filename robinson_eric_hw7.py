# Hello! This is my HW7 code!

# Importing necessary modules
import numpy as np
from astropy import units as u
from matplotlib import pyplot as plt

# Text concerning the structure of the sed.txt file:
# columns are wavelength (micron) and specific luminosity (Lsun/micron)

# Reading in the data, including the comma delimiter
data = np.loadtxt("/home/robinson.eric/ast4930/hw7/sed.txt", delimiter=",")

# Defining the x and y axes as the first and second columns
wav = data[:,0]
flux = data[:,1]

# Finding what index 10 microns starts
under_10_array = np.where(wav <= 10.0)
#print(under_10_array)
#print(wav[833], wav[834])
# The output finds the index to be 833 (because the code is backwards).

wav *= u.micron
flux *= u.Lsun / u.micron

# Plotting code
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Galaxy Spectral Energy Distribution')
#ax.loglog(wav[0:833],flux[0:833])
ax.loglog(wav,flux)
#ax.set_xlim([10,1000])
ax.set_xlabel(r'Wavelength ($\mu$m)')
ax.set_ylabel(r'Solar Luminosities/Wavelength [Lsun /($\mu$m)]')
plt.savefig('/home/robinson.eric/ast4930/hw7/galaxy_SED.png',dpi=300)

# Integrating
integral = (np.trapz(flux[0:833], x=-wav[0:833])).to(u.erg / u.s)
print("The integral of the SED is:",integral)
