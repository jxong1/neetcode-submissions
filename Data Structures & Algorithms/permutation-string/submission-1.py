class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False

        need = [0] * 26
        seen = [0] * 26
        for i in range(len(s1)):
            need[ord(s1[i]) - ord('a')] += 1
            seen[ord(s2[i]) - ord('a')] += 1
        
        if (need == seen):
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            seen[ord(s2[right]) - ord('a')] += 1
            seen[ord(s2[left]) - ord('a')] -= 1
            left+= 1

            print(seen)
            if (need == seen):
                return True
        return False