from spectral_functions import *

data_dir = 'Example_Data/'
for item in os.listdir(data_dir):
    if item == '.DS_Store':
        # .DS_Store is a file that shows up when running on OSX, this ignores that
        continue
    spectra_dict = import_spectra(data_dir+item)

    plot_spectra(spectra_dict, item)
    plt.savefig('Example_Plots/{}.png'.format(item), bbox_inches='tight')
    plt.close()
