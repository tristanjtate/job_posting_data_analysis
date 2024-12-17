import kagglehub

# this is all to download dataset via kaggle api

# downloading latest version of my dataset
path = kagglehub.dataset_download("rrkcoder/glassdoor-data-science-job-listings")

# prints path to where dataset is
print("Path to dataset files:", path)