#RISHAB KSHATRI PES2UG19CS327
#GOURAV ARAVINDA PES2UG19CS130
#SRIVATSAN NARENDIRAN PES2UG19CS408
#TEJAS REDDY PES2UG19CS308
#IMPORTING THE REQUIRED MODULES

from pyspark.sql import SparkSession

from pyspark.ml.clustering import KMeans

from pyspark.ml.evaluation import ClusteringEvaluator

spark = SparkSession.builder.appName(‘Clustering using K-Means’).getOrCreate()

data_customer=spark.read.csv('CC General.csv', header=True, inferSchema=True)

data_customer.printSchema()
#PRINTING 

silhouette_score=[]
#INITIALIZING THE VARIABLE

evaluator = ClusteringEvaluator(predictionCol='prediction', featuresCol='standardized', \
                                metricName='silhouette', distanceMeasure='squaredEuclidean')
#STARTING THE LOOP                            
for i in range(2,10):

    KMeans_algo=KMeans(featuresCol='standardized', k=i)
    
    KMeans_fit=KMeans_algo.fit(data_scale_output)
    
    output=KMeans_fit.transform(data_scale_output)
    
    score=evaluator.evaluate(output)
    
    silhouette_score.append(score)
    
    print("Silhouette Score:",score)
