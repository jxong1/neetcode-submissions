class MedianFinder:

    def __init__(self):
        self.lHeap, self.rHeap = [], []
        heapq.heapify_max(self.lHeap)
        heapq.heapify(self.rHeap)

    def addNum(self, num: int) -> None:
        if len(self.lHeap) == 0 or num <= self.lHeap[0]:
            heapq.heappush_max(self.lHeap, num)
        else:
            heapq.heappush(self.rHeap, num)
        if len(self.lHeap) > len(self.rHeap) + 1:
            heapq.heappush(self.rHeap, heapq.heappop_max(self.lHeap))
        elif len(self.rHeap) > len(self.lHeap) + 1:
           heapq.heappush_max(self.lHeap, heapq.heappop(self.rHeap))

    def findMedian(self) -> float:
        if len(self.rHeap) > len(self.lHeap):
            return self.rHeap[0]
        elif len(self.lHeap) > len(self.rHeap):
            return self.lHeap[0]
        else:
            return (self.rHeap[0] + self.lHeap[0]) / 2
        