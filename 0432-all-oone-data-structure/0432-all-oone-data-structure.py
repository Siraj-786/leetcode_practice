import bisect

class AllOne:

    def __init__(self):
        self.counts = {}  # Stores the count of each string
        self.sorted_counts = []  # Sorted list of (count, key) tuples

    def inc(self, key: str) -> None:
        if key in self.counts:
            old_count = self.counts[key]
            # Remove the old (count, key) pair from the sorted list
            self.sorted_counts.remove((old_count, key))
            new_count = old_count + 1
            self.counts[key] = new_count
        else:
            new_count = 1
            self.counts[key] = new_count

        # Insert the new (count, key) pair into the sorted list
        bisect.insort(self.sorted_counts, (new_count, key))

    def dec(self, key: str) -> None:
        if key in self.counts:
            old_count = self.counts[key]
            # Remove the old (count, key) pair from the sorted list
            self.sorted_counts.remove((old_count, key))
            if old_count == 1:
                del self.counts[key]  # Remove the key if the count becomes 0
            else:
                new_count = old_count - 1
                self.counts[key] = new_count
                # Insert the new (count, key) pair into the sorted list
                bisect.insort(self.sorted_counts, (new_count, key))

    def getMaxKey(self) -> str:
        if not self.sorted_counts:
            return ""
        return self.sorted_counts[-1][1]  # Return the key with the maximum count

    def getMinKey(self) -> str:
        if not self.sorted_counts:
            return ""
        return self.sorted_counts[0][1]  # Return the key with the minimum count
