## metrics 
Docker image with Python mtrics collection script inside


## Requirements
* python 2 or 3 version
* psutil
* docker

## Usage
First, you need to build container. Copy the ```metrics.py``` and ```Dockerfile``` to your directory and run
```docker build -t metrics .```  inside your directory.
After build successfully finished, run container with ```docker run metrics cpu```  or  ```docker run mtrics mem```


## Example of output
```
MEM
virtual total     16731308032
virtual used      5660549120
virtual free      10275917824
virtual total     552914944
swap total        2147479552
swap used         0.8
swap used         3063808
```

```
CPU
system.cpu.idle   6062193.13
system.cpu.user   184993.01
system.cpu.guest  0.0
system.cpu.iowait 10644.66
system.cpu.stolen 0.0
system.cpu.system 41600.0
```
