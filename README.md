# Complex-Aggregate-Queries

This repository contains the code used for the experiments described in the paper titled

_An execution cost model of apprgate query based on knowledge graph._

## Requirements

The experiments have been run on an CentOS Linux release 7.3.1611 computer with a 2.1 GHz Xeon processor and 64GB RAM. All programs are written with `java1.8` and make use of two external libraries [Apache Commons Math](http://commons.apache.org/proper/commons-math/download_math.cgi), [EJML](http://ejml.org/wiki/index.php?title=Main_Page).

## Datasets and Query Workloads

Datasets: [DBpedia dataset](https://drive.google.com/drive/folders/1fQEbz7tmcbe8R3sTO_LwJ9LVBDtqlyph?usp=sharing), [Freebase dataset](https://drive.google.com/drive/folders/1wZSbxF_x2DSJWiMf5sW9WnJ1NW_RR3IG?usp=sharing), [Yago dataset](https://drive.google.com/drive/folders/1Q35R1RImlZPYwTdBwXyvGSj-4aWIONb_?usp=sharing), each one consists of an `entity file` and an `edge file`.

The experiment uses `QALD-4`, `WebQuestions`, and `Synthetic queries` as [benchmarks](https://drive.google.com/drive/folders/19T1Th9G4HcffIhAbaCHqOJPxeWElOy51?usp=sharing) for DBpedia, Freebase, and Yago datasets, respectively.

**Example of the dataset (DBpedia)**

edge file

| entity1_id | entity2_id | entity1_name | predicate | entity2_name |
| :--------: | :--------: | :----------: | :-------: | :----------: |
|  3471751   |  1712537   | Porsche_944  | assembly  |   Germany    |

entity file

| entity_id | entity_name |    type    |
| :-------: | :---------: | :--------: |
|  3471751  | Porsche_944 | automobile |
|  1712537  |   Germany   |  country   |

## Usage

### Effectiveness and Efficiency Evaluation

#### Our Method
