class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):

            j = i

            # Find the separator
            while s[j] != "#":
                j += 1

            # Get the length
            length = int(s[i:j])

            # Extract the actual string
            word = s[j + 1 : j + 1 + length]

            result.append(word)

            # Move to the next encoded string
            i = j + 1 + length

        return result