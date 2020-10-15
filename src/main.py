import random
from memory_sim import MemorySim

VIRTUAL_PAGES = 8
PHYSICAL_PAGES = 4
PAGE_FRAMES = 4
PAGE_SIZE = 1024 # Bytes
ADDRESS_SIZE = 4 # Bytes - 64bits

ms = MemorySim(VIRTUAL_PAGES, PHYSICAL_PAGES, PAGE_SIZE, ADDRESS_SIZE)
ms.run(ms.FIFO, 100)
