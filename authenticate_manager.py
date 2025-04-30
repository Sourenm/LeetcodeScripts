class AuthenticationManager:
    tokens = {}
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens:
            self.tokens[tokenId] = currentTime
        
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            if currentTime - self.tokens[tokenId] < self.timeToLive:
                self.tokens[tokenId] = currentTime
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for k, v in self.tokens.items():
            if currentTime - v < self.timeToLive:
                count += 1
        return count


am = AuthenticationManager(5)
am.renew("aaa", 1)
am.generate("aaa", 2)
print(am.countUnexpiredTokens(6))
am.generate("bbb", 7)
am.renew("aaa", 8)
am.renew("bbb", 10)
print(am.countUnexpiredTokens(15))


