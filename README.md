# Deletable Bloom Filters in a Distributed Proxy Server Caching

## Introduction: 

Bloom filters (BF) are popular data structures for determining set membership. Random hashing of keys to bit arrays translates to compact storage and fast queries. Hash collisions in the bit array results in the false positive query results. However, traditional BF’s will never return a false negative result for a query. The false positive rate (FPR) of a BF can be reduced by increasing the size of the bit array or increasing the number of hash functions. Thus, there is an aspect of a tradeoff between space and performance. Traditional BF’s support insertions but not deletions. The FPR increases with the number of added items and thus traditional BF’s benefit from knowing the set cardinality when the number of hash functions and bit array size are being selected for an application.

Bloom filters have been widely employed to allow for fast queries of set membership with a compact data structure and an allowance for an acceptable false negative rate. One such application is for the distributed caching of web content on proxy servers as discussed in (Broder & Mitzenmacher, 2004). This project will examine the performance of a variant of a BF, Deletable Bloom Filter (DBF) for the above application.

## Problem Statement:

A proposed framework for cooperation among networked proxy servers (Fan, Cao,  Almeida, Broder, 2000) is one where a proxy servers contain summaries of the contents of other proxy servers to allow for rapid direction of content queries to servers that contain the desired content. In this setting, BF’s provide a compact and quickly queried data structure for summarizing a server’s contents. Proxy servers may store new items and have old items removed during normal operation. To account for changes in contents, the proxy server must periodically recompute a BF representing its contents by rehashing its contents and then broadcasting the rebuilt BF bit array to neighboring servers. In this context, a DBF could eliminate the need to rehash all of its contents to create an updated BF by simply allowing removed items to potentially be deleted and simply inserting new items. 

This project compares the performace of DBF and BF in a distributed proxy server cache application in two scenarios, one with deletions and other one with insertions and deletions.

## Results:

**Performance of a BF vs DBF when there are only insertions**<br> 
<p align="center">
  <img width="300" height="200" src= results/exp1.png>
</p>


**Performace of DBF with there are multiple insertions and deletions**<br>
<p align="center">
  <img width="300" height="200" src= results/exp2.png>
</p>

## References:

Rothenberg, C. E., Macapuna, C. A., Verdi, F. L., & Magalhaes, M. F. (2010). The Deletable Bloom Filter: A New Member of the Bloom Family. IEEE Communications Letters, 557-559.

Broder, A., & Mitzenmacher, M. (2004). Network Applications of Bloom Filters: A Survey. Internet Mathematics, 485-509.

L. Fan, P. Cao, J. Almeida, and A. Z. Broder (2000). “Summary Cache: A Scalable Wide-Area Web Cache Sharing Protocol.” IEEE/ACM Transactions on Networking 8:3, 281—293
