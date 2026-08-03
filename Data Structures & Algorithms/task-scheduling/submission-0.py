import heapq

class Solution:
    class _HeapElem:
        def __init__(self, task: str, freq: int) -> None:
            self._task = task
            self._freq = freq
            self.ready_time = 0

        @property
        def task(self) -> str:
            return self._task

        @property
        def freq(self) -> int:
            return self._freq

        def decrement_freq(self) -> None:
            if self._freq > 0:
                self._freq -= 1
            else:
                raise RuntimeError(f"{self._freq = } cannot be decremented")

        def __lt__(self, other: _HeapElem) -> bool:
            return self.freq > other.freq

    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freqs: dict[str, int] = {}
        for task in tasks:
            task_freqs[task] = task_freqs.get(task, 0) + 1

        max_heap: list[self._HeapElem] = []
        for task, freq in task_freqs.items():
            max_heap.append(self._HeapElem(task, freq))
        heapq.heapify(max_heap)

        # Pop one of each iteration to add to max heap
        cooldown_q: list[str] = []

        time = 0
        while max_heap or cooldown_q:
            time += 1
            # Get most frequent task (greedy strategy)
            if max_heap:
                most_freq_t = heapq.heappop(max_heap)
                most_freq_t.decrement_freq()
                if most_freq_t.freq >= 1:
                    most_freq_t.ready_time = time + n
                    cooldown_q.append(most_freq_t)

            if cooldown_q and cooldown_q[0].ready_time <= time:
                cooled_down_task = cooldown_q.pop(0)
                heapq.heappush(max_heap, cooled_down_task)

        return time