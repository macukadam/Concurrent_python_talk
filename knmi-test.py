from KNMIdata import KNMI

# When download set to true it will remove and download files.
knmi = KNMI(data_type='hourly', download=True)

# If hourly data files are already downloaded
knmi = KNMI()

# returns station data by station id
df = knmi[277]

# returns closest station data by postcode
df = knmi.find_df('1092AX')
