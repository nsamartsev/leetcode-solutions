class Codec:
    storage = dict()
    prefix = "https://short.ru/"

    def encode(self, longUrl: str) -> str:
        short = self.prefix + str(hash(longUrl))
        self.storage[short] = longUrl
        return short

    def decode(self, shortUrl: str) -> str:
        return self.storage[shortUrl]


def main():
    codec = Codec()
    assert codec.decode(
        codec.encode("https://leetcode.com/problems/design-tinyurl")) == "https://leetcode.com/problems/design-tinyurl"
    print("tests ok")


main()
