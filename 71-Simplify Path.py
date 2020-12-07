class Solution:
    def simplifyPath(self, path: str) -> str:
        path_lst = path.split("/")
        stack = []
        for directory in path_lst:
            if directory == '' or directory == '.': continue
            if stack and directory == '..':
                stack.pop()
            elif directory != '..':
                stack.append(directory)
        
        return '/' if not stack else "/"+ "/".join(stack)
        