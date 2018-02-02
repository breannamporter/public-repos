# Public Repos 

This program takes in a Github username and calls the List User Repositories Github REST API to display all public repositories owned by the specified user.  

### Prerequisites

- Python 2.7 

### Installing

This program uses the requests library which can be installed with pip. 

```
pip install requests 
```

### Running 

This program can be run on the command line by navigating to the folder containing public-repos.py and then executing the command below with the username you wish to query about as an argument.  
```
python public-repos.py <username> 
```

For example, running the command: 

```
python public-repos.py breannamporter
```
prints the following to the command line.

```
public-repos
TestRepo1
TestRepo2
```

