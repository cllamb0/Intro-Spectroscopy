from spectral_functions import *

data_dir = 'Example_Data/'
for item in os.listdir(data_dir):
    if item == '.DS_Store':
        continue # Using the directory so I can tab-complete (lazy)
    spectra_dict = import_spectra(data_dir+item)

    plot_spectra(spectra_dict, item)
    plt.savefig('Example_Plots/{}.png'.format(item), bbox_inches='tight')
    plt.close()
