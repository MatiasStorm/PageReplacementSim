# Memory Page Replacement Simulation
Simple pyhton simulation of memory page replacement algorithms.

Operating systems use page replacement algorithms to manage the mapping between virtual- and physical memory.
For example a process might have 8 pages of virtual memory but the hardware only has 4,
then a page replacement algorithm is used to select which physical pages are to store parts of the program when a page fault occurs.
A page fault happens when a program tries to fetch data from a virtual page which is not loaded into main memory.

## Example of a virtual to physical memory mapping
| Vitual page | Physical Page | Page fault if addressed |
|-------------|---------------|-------------------------|
| 0           | NaN           | Yes                     |
| 1           | 3             | No                      |
| 2           | NaN           | Yes                     |
| 3           | 2             | No                      |
| 4           | 0             | No                      |
| 5           | NaN           | Yes                     |
| 6           | 1             | No                      |
| 7           | NaN           | Yes                     |


## Tested algoritms:
### FIFO (First In First Out)
This algorithm selects the first physical page that was loaded to be overwritten if a page fault occurs.

### LRU (Least Recently Used)
This algorithm selects the least recently used physical page to be overwritten when a page fault occurs.

## Modify simulation:
You can change the following global variables in [main.py](src/main.py) to alter the simulation parameters.
```
VIRTUAL_PAGES = 8
PHYSICAL_PAGES = 4
PAGE_FRAMES = 4
PAGE_SIZE = 1024 # Bytes
ADDRESS_SIZE = 4 # Bytes
ITERATIONS = 1000
```

## Run
run `python main.py`


## Test
run `pytest`
