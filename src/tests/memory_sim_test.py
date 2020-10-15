import pytest
from src import MemorySim

class TestMemorySim:
    def test_get_max_virtual_address(self):
        for i in [1, 2, 4 ,8]:
            ms: MemorySim = MemorySim(8, 4, 1024, i)
            assert ms.get_max_virtual_address() == int(8191 / i)

    def test_translage_address_to_page(self):
        ms = MemorySim(8, 4, 1024, 1)
        assert ms.translate_address_to_page(8191) == 7
        ms = MemorySim(8, 4, 1024, 4)
        assert ms.translate_address_to_page(1023) == 3

        ms = MemorySim(8, 4, 2048, 1)
        assert ms.translate_address_to_page(8191) == 3

        ms = MemorySim(16, 4, 1024, 1)
        assert ms.translate_address_to_page(16383) == 15

    def test_FIFO(self):
        ms = MemorySim(16, 4, 1024, 1)
        for page in [0,7,2,7,5,8,9,2,4]:
            ms.load_pageframe_FIFO(page)
        assert ms.page_hits == 2
        assert ms.page_faults == 7

    def test_LRU(self):
        ms = MemorySim(16, 4, 1024, 1)
        for page in [0,7,2,7,5,8,9,2,4]:
            ms.load_pageframe_LRU(page)
        assert ms.page_hits == 1
        assert ms.page_faults == 8
