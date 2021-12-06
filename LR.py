#RISHAB KSHATRI PES2UG19CS327
#GOURAV ARAVINDA PES2UG19CS130
#SRIVATSAN NARENDIRAN PES2UG19CS408
#TEJAS REDDY PES2UG19CS308
from pyspark.ml.regression import LinearRegression

# Load training data
spark = SparkSession \
    .builder \
    .appName("sentiment analysis") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
training = spark.read.format("csv")\
    .load("/Downloads/sentiment/train.csv")

lr = LinearRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)

# Fit the model
lrModel = lr.fit(training)

# Print th

e coefficients and intercept for linear regression
print("Coefficients: %s" % str(lrModel.coefficients))
print("Intercept: %s" % str(lrModel.intercept))

# Summarize the model over the training set and print out some metrics
trainingSummary = lrModel.summary
print("numIterations: %d" % trainingSummary.totalIterations)
print("objectiveHistory: %s" % str(trainingSummary.objectiveHistory))
trainingSummary.residuals.show()
print("RMSE: %f" % trainingSummary.rootMeanSquaredError)
print("r2: %f" % trainingSummary.r2)
