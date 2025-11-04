# Leetcode
# 274. H-Index



class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Step 1: Count total number of papers
        papers = len(citations)

        # Step 2: Create buckets to count how many papers have a given number of citations.
        # We use (papers + 1) buckets because any citation count greater than 'papers'
        # can be treated as 'papers' (since h-index cannot exceed total number of papers).
        citation_buckets = [0] * (papers + 1)

        # Step 3: Fill the buckets.
        # For each citation count:
        # - If citation <= papers, increment its exact bucket.
        # - If citation > papers, increment the last bucket (papers),
        #   since having more than 'papers' citations doesn’t increase h-index beyond that.
        for citation in citations:
            citation_buckets[min(citation, papers)] += 1

        # Step 4: Traverse from high to low to find the maximum h-index.
        # We'll keep track of cumulative_papers = total papers with >= current citation count.
        cumulative_papers = 0

        # We go backwards: from the highest possible h (papers) down to 0
        for h_index in range(papers, -1, -1):
            # Add all papers that have at least 'h_index' citations
            cumulative_papers += citation_buckets[h_index]

            # Step 5: If the number of papers with at least 'h_index' citations
            # is >= h_index, then we've found the h-index.
            if cumulative_papers >= h_index:
                return h_index
