"""
Code snippets to import and use this repository
------------------------------------------------


.mat files includes the signal array (image or time-series)

.hea files indicates the "Header" as metadata
"""



#%% SETUP


import sys
sys.path.insert(0, r'C:\Users\EXCALIBUR\Desktop\Python\CODES\ECG\file-analysis-system-for-ai-models')

from scripts.operations.mat_file_reader import MatAnalyzer
from scripts.operations.hea_file_reader import HeaAnalyzer

MAT_FILE_PATH = r'C:\Users\EXCALIBUR\Desktop\Python\CODES\ECG\JS05332.mat'   # path of example files to analyze
HEA_FILE_PATH = r'C:\Users\EXCALIBUR\Desktop\Python\CODES\ECG\JS05332.hea'



#%% MAT Method 1: Generate an analyzer


# Basic usage
analyzer = MatAnalyzer(MAT_FILE_PATH)




print("MatAnalyzer created")



data = analyzer.load()  

# now your data becomes a dictionary, key of the signal array is 'val'


print(f"Loaded {len(data)} variables")
print(f"Keys: {list(data.keys())}")



#%% MAT Method 2: list_keys() - Get clean variable names


keys = analyzer.list_keys()


print(f"Variable names: {keys}")


#%% MAT Method 3: summarize_variables() - Get detailed info


summaries = analyzer.summarize_variables()  

for a in summaries:
    print(f"{a.name}: shape={a.shape}, dtype={a.dtype}")


#%% MAT Method 4: detect_feature_candidates() - Find feature matrices


features = analyzer.detect_feature_candidates()

print(f"Feature candidates: {features}")


if features:
    X = data[features[0]]       # array of the signal is obtained
    print(f"Shape: {X.shape}")


#%% MAT Method 5: detect_label_candidates() - Find label arrays


labels = analyzer.detect_label_candidates()   # it is empty 

print(f"Label candidates: {labels}")


if labels: 
    y = data[labels[0]]                      # variable y absent in this case
    print(f"Shape: {y.shape}")
    

#%% MAT Method 6: label_distributions() - Count classes


distributions = analyzer.label_distributions()   # empty


for var_name, dist in distributions.items():
    print(f"{var_name}: {dist}")
    

#%% MAT Method 7: find_class_name_candidates() - Find string arrays

class_names = analyzer.find_class_name_candidates()  # empty again

for var_name, strings in class_names.items():
    print(f"{var_name}: {strings}")
    

#%% MAT Method 8: suggest_label_name_mapping() - Map numbers to names


mappings = analyzer.suggest_label_name_mapping()     # empty again

for label_var, mapping in mappings.items():
    print(f"{label_var}: {mapping}")
    

#%% MAT Method 9: build_report() - Generate text report


analyzer.print_report()


#%% MAT COMPLETE WORKFLOW - Get data for ML model


analyzer = MatAnalyzer(MAT_FILE_PATH)

data = analyzer.load()


features = analyzer.detect_feature_candidates()
labels = analyzer.detect_label_candidates()

X = data[features[0]]
y = data[labels[0]].ravel()     # IndexError


print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")





#%% HEA Method 1: Utilize HEA analyzer


hea_analyzer = HeaAnalyzer(HEA_FILE_PATH)


print("HeaAnalyzer is generated")


#%% HEA Method 2: load() - Load and parse .hea file


hea_analyzer.load()

print("HEA file loaded and parsed")


#%% HEA Method 3: record_summary() - Get record information


record = hea_analyzer.record_summary()   # indicates the important information to consider about the data


print(f"Record name: {record.record_name}")
print(f"Number of signals: {record.n_signals}")
print(f"Sampling rate: {record.fs_hz} Hz")
print(f"Number of samples: {record.n_samples}")
print(f"Extra info: {record.extra_tokens}")


#%% HEA Method 4: signal_summaries() - Get signal information


signals = hea_analyzer.signal_summaries()   # applies the summary for all existing signals in the data

print(f"Found {len(signals)} signals:")


for sig in signals:
    print(f"\nSignal {sig.index}:")
    print(f"  File: {sig.file_name}")
    print(f"  Format: {sig.fmt}")
    print(f"  Gain: {sig.gain}")
    print(f"  Bit resolution: {sig.bit_resolution}")
    print(f"  Units: {sig.units}")
    print(f"  Description: {sig.description}")
    

#%% HEA Method 5: build_report() - Generate text report



hea_analyzer.print_report()


#%% HEA COMPLETE WORKFLOW - Extract all metadata


hea_analyzer = HeaAnalyzer(HEA_FILE_PATH)
hea_analyzer.load()

# Get record info
record = hea_analyzer.record_summary()
fs = record.fs_hz  # Sampling frequency
n_samples = record.n_samples
n_signals = record.n_signals

# Get signal info
signals = hea_analyzer.signal_summaries()
signal_descriptions = [s.description for s in signals]
signal_units = [s.units for s in signals]
signal_gains = [s.gain for s in signals]

print(f"Record: {record.record_name}")
print(f"Sampling rate: {fs} Hz")
print(f"Duration: {n_samples/fs:.2f} seconds")
print(f"Signals: {signal_descriptions}")
print(f"Units: {signal_units}")



