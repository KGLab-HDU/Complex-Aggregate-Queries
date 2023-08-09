# Complex-Aggregate-Queries

This repository contains the code used for the experiments described in the paper titled

_An execution cost model of apprgate query based on knowledge graph._

## Requirements

The experiments have been run on an CentOS Linux release 7.3.1611 computer with a 2.1 GHz Xeon processor and 64GB RAM. All programs are written with `java1.8` and make use of two external libraries [Apache Commons Math](http://commons.apache.org/proper/commons-math/download_math.cgi), [EJML](http://ejml.org/wiki/index.php?title=Main_Page).

## Datasets and Query Workloads

Datasets: [DBpedia dataset](https://drive.google.com/drive/folders/1RTi2L5Kevoj6Xnov-Ibmgz1r-DP9Yh79?usp=drive_link), [Freebase dataset](https://drive.google.com/drive/folders/11LygOGkAxP6hZ7FnP0KFotiKcPTT2C05?usp=drive_link), [Yago dataset](https://drive.google.com/drive/folders/1EsYWH5KgST_v32fyyn1nCHvKUrSWxMJl?usp=drive_link), each one consists of an `entity file` ,an `adjTable file` and a 'simFile file'. The 'entity file' contains all entity of the dataset.The 'adjTable file' contains the relationship between the nodes of the data set, and the predicate is used to describe the relationship more accurately.The 'simFile file' contains the similarity between the predicates used in the experiment and the predicates of the whole graph obtained through the word2Vec method training.

The experiment uses `QALD-4`, `WebQuestions`, and `Synthetic queries` as [benchmarks](https://drive.google.com/drive/folders/19T1Th9G4HcffIhAbaCHqOJPxeWElOy51?usp=sharing) for DBpedia, Freebase, and Yago datasets, respectively.

**Example of the dataset (DBpedia)**

adjTable file

| entity1_id | predicate_1 | entity2_id | predicate_2 | entity3_id |
| :--------: | :--------: | :----------: | :-------: | :----------: |
|  0   |  country   | 2679443  | isPartOf  |   3777430    |

entity file

| entity_id | entity_name |    type    |
| :-------: | :---------: | :--------: |
|  3471751  | Porsche_944 | automobile |
|  1712537  |   Germany   |  country   |

## Usage

### Our Methods

Our proposed method requires some parameters. Next, we will follow different steps to illustrate the whole process of our program running.
#### Collect

This step is to obtain our relevant training data through AQS, where AnchorNode refers to the starting node, predicate refers to the predicate, and TargetType refers to the type of the target node. For example, how many cars are produced in Germany? AnchorNode is Germany. , the predicate is assembly (similar predicates such as produce are also available), TargetType is automobile, Dataset_File_path is the folder path where the dataset is located, and ResultFile_Path is the path where the output result file is located.And the code is running as follow:
```
Collect: Java -jar CollectTrainingData.jar < AnchorNode > < predicate > <TargetType> <Dataset_File_path> < ResultFile_Path >

```

This step will output three files, which are the subgraph of the problem (including entity.txt and edge.txt, output under Dataset_File_path), and the data we need to train the model, output under ResultFile_Path .

#### Training
In this step, we will train our model based on the file output by collect. First, we find the output file under ResultFile_Path (the file name is AnchorNode-predicate-TargetType.txt), and we change the file extension to xlsx or xls, click to see that we have four columns of data. The first column is the error e, the second column is the number of samples S, the third column is the sampling and correctness verification time $T_{sv}$, and the fourth column is the estimation and accuracy guarantee time T<sub>e</sub>.
Then we need to create four folders named e-S, e-Tv, e-Tsve, and S-Tsv, and divide the previously obtained quadruple xlsx into corresponding meanings, and name the xls files obtained from the division as corresponding The serial number of the question, here we take 1 as an example (that is, 1.xls) and store it in the corresponding folder. Please note that here you need to insert the first column of each split file as 1 (it has nothing to do with the serial number of the question). The figure below is We get the split file of e-S of question 1.
![image](https://github.com/KGLab-HDU/Complex-Aggregate-Queries/assets/94584738/c40df50d-8573-40ff-8637-a8b3910d4d84)
Then we put Train.py in the same directory as e-S and other folders, and run the following code to get the parameter results of our training model in the e-Tsve folder, which is the relevant parameters of the Cost Model.
```
Train: Python Train.py

```
PS: Here you need to modify the range value of i in the py file. The range is the number of questions we need to train. If there are 5 questions to train, you need to change i to 5.

#### Query

#### Our Method
