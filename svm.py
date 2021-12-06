#RISHAB KSHATRI PES2UG19CS327
#GOURAV ARAVINDA PES2UG19CS130
#SRIVATSAN NARENDIRAN PES2UG19CS408
#TEJAS REDDY PES2UG19CS308

from pyspark.ml.classification import LinearSVC

spark = SparkSession \
    .builder \
    .appName("sentiment analysis") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    
# Load training data
training = spark.read.format("csv").load("/Downloads/sentiment/train.csv")
#LOADING THE DATA 
#FROM THE CSV FILE 
#AND PUT FOR TRAINING
lsvc = LinearSVC(maxIter=10, regParam=0.1)

# Fit the model
lsvcModel = lsvc.fit(training)

# Print the coefficients and intercept for linear SVC
print("Coefficients: " + str(lsvcModel.coefficients))
print("Intercept: " + str(lsvcModel.intercept))
