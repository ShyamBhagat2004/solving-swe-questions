class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        for dir in path.split("/"):

            if dir == "":
                pass
            elif dir == ".":
                pass
            elif dir == "..":
                if stack:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(dir)
        return "/" + "/".join(stack)
        