# JSON-Clustering
> Similarity between JSON documents on the basis of their structure, their semantics and context.

---

# Introduction

## What is JSON?

JavaScript Object Notation (JSON) is a widely adopted format for representing structured data in text based format. The notation is derived from the popular JavaScript programming language but its convention can be understood and parsed in several other programming languages. Currently, data is stored and exchanged using the JSON notation. A JSON is commonly structured as an order of key/value pairs. The key is usually a defined string while a value can be of type strings, numbers, booleans, objects or arrays (An ordered list of values). A JSON structure can be represented as a tree.

As mentioned earlier, JSON notations are popularly being used for storing structured data and is used in NoSQL or nonrelational databases. Databases that make use of JSON representation to store, index and query data are called JSON document databases. Due to developments in distributed database systems, for the efficient storage, querying and insertions of documents in these systems, organizations of the documents plays a vital role. JSON clustering improves the effectiveness of document management systems by organizing the documents from a large collection into groups that can be useful for similarity-based retrieval.

A JSON document database is arguably the most popular category in the NoSQL family of databases. NoSQL database management differs from traditional relational databases that struggle to store data outside of columns and rows. Instead, they flexibly adapt to a wide variety of data types, changing application requirements and data models. In an era where physical storage limits are no longer a bottleneck, JSON databases deliver superior scale and performance.

JSON document classes are able to do this because of forming JSON clusters or shards. This concept helps reduce overhead over a centralized approach, while increasing query performance.

## Why do we Cluster?

In distributed data systems, there are two types of major query operations that can be performed based on the availability of the requested data on a given shard. These two operations are - targeted operations and broadcast operations. If we take the example of the MongoDB system, there exists an application/driver that will be making the requests, which will be passed to the MongoDB ecosystem. The first point of contact of this request will be a query router, which is connected to a Config server. Now, based on the query, and the shard key that is available, the query will be either routed to a particular targeted shard, or it will be broadcasted to all shards. In case the query contains the shard key of a shard, the operation will be targeted to that particular shard. Otherwise, the query will be routed to all shards, and the collected results are sent back to the application.

As is obvious, targeted operations have a much lesser overhead in comparison to the broadcast operation. So, our work in this project is mainly targeted towards increasing the number of targeted operations through grouping/clustering similar documents together in a single shard. The main objectives are enumerated below:

* Research and identify the best representation of JSON documents to calculate similarity scores.  
* Find the best ways to calculate similarity scores between JSON documents.  
* Experiment different clustering techniques and compare them on relevant performance metrics.  

---

# Packages Required to Run the Project
> The environment used for development was Python-3.10 and the following pip packages are required

* numpy, pd, matplotlib  
* json, os  
* SetSimilaritySearch
* SentenceTransformers
* nltk, re  
* Jupyter Notebook or similar IDE

---

# Steps to Execute the Code

## Load the Dataset

> Run the file `/scripts/ntl_extractor2.py`

This file loads any dataset specified on line 13, and outputs `/outputs/NTL_paths_list.json` containing all NTL paths. To gain more control over this, consider using the file `/scripts/JACCARD_similarity.ipynb`'s opening cells.

## Generate the Structural Similarity for all Pairs of Documents

> Run the file `/scripts/JACCARD_similarity.ipynb`

This file generates a file `outputs/similarity_result.csv` that contains the JACCARD similarity scores for a combination of datasets, as configured. Apart from this, several other CSV files are generated, each containing JACCARD and COSINE similarity scores on each dataset, for RTL (Root to Leaf) and NTL (Node to Leaf) paths. These files help us observe and conclude the choice of our structural similarity technique.


## Generate the components needed to generate Structural, Contextual and Semantic Similarity Score for all Pairs of Documents
> Run the file `/scripts/contextual_semantic_similarity.ipynb`

This file generates files to aid in the final clustering process of the project. Among the output files, a file titled `scores_final.json` contains the BERT embeddings, WordNet associations and Node-to-Leaf paths of each document. These will be utilized by the `scripts/clustering.ipynb` file to generate a combined similarity score to cluster all the documents appropriately. For the contextual part, embeddings obtained from the BERT Transformer model are obtained, while the semantic similarity is based on the WordNet lexical database associations for each word in a document. 

## Combine the Scores and Cluster the Documents
> Run the file `/scripts/clustering.ipynb`

This file calculates the combined similarity scores for every pair of JSON document (using the outputs stored in `scores_final.json` and applies the (0.5 - 0.25 - 0.25) heuristic threshhold on (Structural - Semantic - Contextual) similarity scores. Then, a dendrogram, K-distance graph and an elbow curve are generated to help us find the probable hyperparameters for the clustering process (for Hierarchical, DBSCAN and K-Means respectively). This is followed by a K-Means implementation to cluster the documents using a custom-metric, that is our similarity score for each pair of document.

![Document Similarity Heatmap](https://user-images.githubusercontent.com/55971005/163239965-3436e4f0-1f0c-4b42-8701-32d60907bba0.png)

---

# Authors
* Ishaan Singh  
* Ikjot Singh Dhody  
* Ashutosh Anand  
* Sudarshan Sundarrajan  
