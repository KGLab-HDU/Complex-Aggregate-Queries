# Complex-Aggregate-Queries

This repository contains the code used for the experiments described in the paper titled

_An execution cost model of apprgate query based on knowledge graph._

## Requirements

The experiments have been run on an CentOS Linux release 7.3.1611 computer with a 2.1 GHz Xeon processor and 64GB RAM. All programs are written with `java1.8` and make use of two external libraries [Apache Commons Math](http://commons.apache.org/proper/commons-math/download_math.cgi), [EJML](http://ejml.org/wiki/index.php?title=Main_Page).

## Datasets and Query Workloads

Datasets: [DBpedia dataset](https://drive.google.com/drive/folders/1RTi2L5Kevoj6Xnov-Ibmgz1r-DP9Yh79?usp=drive_link), [Freebase dataset](https://drive.google.com/drive/folders/11LygOGkAxP6hZ7FnP0KFotiKcPTT2C05?usp=drive_link), [Yago dataset](https://drive.google.com/drive/folders/1EsYWH5KgST_v32fyyn1nCHvKUrSWxMJl?usp=drive_link), each one consists of an `entity file` and an `adjTable file`.

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

#### Our Methods

Our proposed method requires the same parameters. It can be run using the following command:

```
Exact: Java -jar Exact.jar < community models > < dataset_name > <dataset_type> <query_node> < queryK > < metapath >

SEA: Java -jar SEA.jar < community models > < dataset_name > <dataset_type> <query_node> < queryK > < metapath >

SEA-size-bounded: Java -jar SEA_size.jar < community models > < dataset_name > <dataset_type> <query_node> < queryK > <Minsize> <Maxsize> < metapath >

```
#### Our Method
