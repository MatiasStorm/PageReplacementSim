from typing import Dict, List
import random


class PageMap:
    def __init__(self, virtual_page: int, physical_page: int):
        self.virtual_page: int = virtual_page
        self.physical_page: int = physical_page

class PageMapper:
    def __init__(self, virtual_pages: int):
        self.page_maps: List[PageMap] = [PageMap(i, -1) for i in range(virtual_pages)]

    def is_page_hit(self, virtual_page: int) -> bool:
        for page_map in self.page_maps:
            if page_map.virtual_page == virtual_page:
                return page_map.physical_page > -1
        return False

    def get_physical_page_from_virtual(self, virtual_page: int) -> int:
        for page_map in self.page_maps:
            if page_map.virtual_page == virtual_page:
                return page_map.physical_page
        return -1
    
    def update_page(self, virtual_page, physical_page):
        for page_map in self.page_maps:
            if page_map.virtual_page == virtual_page:
                page_map.physical_page = physical_page
            elif page_map.physical_page == physical_page:
                page_map.physical_page = -1

class MemorySim:
    FIFO = "FIFO"
    LRU = "LRU"
    def __init__(self, virtual_pages: int, physical_pages: int, page_size: int, address_size: int):
        self.page_faults = 0
        self.page_hits = 0
        self.virtual_pages: int= virtual_pages
        self.physical_pages: int = physical_pages
        self.page_size: int = page_size
        self.address_size: int = address_size
        self.page_mapper = PageMapper(virtual_pages)

        self.first_in: List[int] = [i for i in range(physical_pages)]
        self.last_recently_used: List[int] = [i for i in range(physical_pages)]

    def get_max_virtual_address(self) -> int:
        return int(self.virtual_pages * self.page_size / self.address_size - 1)

    def generate_random_virtal_address(self) -> int:
        max_address: int = self.get_max_virtual_address()
        return random.randint(0, max_address)
        
    def translate_address_to_page(self, address: int) -> int:
        page: int = int(address / (self.page_size / self.address_size))
        return page

    def record_page_fault(self):
        self.page_faults += 1

    def record_page_hit(self):
        self.page_hits += 1

    def load_pageframe_LRU(self, virtual_page):
        if not self.page_mapper.is_page_hit(virtual_page):
            self.record_page_fault()
            physical_page: int = self.last_recently_used.pop(0)
            self.page_mapper.update_page(virtual_page, physical_page)
            self.last_recently_used.append(physical_page)
        else:
            self.record_page_hit()
            physical_page: int = self.page_mapper.get_physical_page_from_virtual(virtual_page)
            self.last_recently_used.remove(physical_page)
            self.last_recently_used.append(physical_page)

    def load_pageframe_FIFO(self, virtual_page):
        if not self.page_mapper.is_page_hit(virtual_page):
            self.record_page_fault()
            physical_page = self.first_in.pop(0)
            self.page_mapper.update_page(virtual_page, physical_page)
            self.first_in.append(physical_page)
        else:
            self.record_page_hit()

    def run(self, algorithm: str, iterations: int):
        for i in range(iterations):
            self.step(algorithm)

        print(f"Page Faults: {self.page_faults} - Page Hits: {self.page_hits}")

    def step(self, algorithm: str):
        virtual_address: int = self.generate_random_virtal_address()
        virtual_page: int = self.translate_address_to_page(virtual_address)
        if algorithm == MemorySim.FIFO:
            self.load_pageframe_FIFO(virtual_page)
        elif algorithm == MemorySim.LRU:
            self.load_pageframe_LRU(virtual_page)













