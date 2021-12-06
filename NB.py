#RISHAB KSHATRI PES2UG19CS327
#GOURAV ARAVINDA PES2UG19CS130
#SRIVATSAN NARENDIRAN PES2UG19CS408
#TEJAS REDDY PES2UG19CS308
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
spark = SparkSession \
    .builder \
    .appName("sentiment analysis") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    
# Load training data
data = spark.read.format("csv") \
    .load("/Downloads/sentiment/train.csv")

# Split the data into train and test
splits = data.randomSplit([0.6, 0.4], 1234)
train = splits[0]
test = splits[1]

# create the trainer and set its parameters
nb = NaiveBayes(smoothing=1.0, modelType="multinomial")

# train the model
model = nb.fit(train)

# select example rows to display.
predictions = model.transform(test)
predictions.show()

# compute accuracy on the test set
evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction",
                                              metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print("Test set accuracy = " + str(accuracy))
