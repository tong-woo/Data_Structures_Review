
"""
Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
Output: 32
Explanation: We have two files:
"dir/subdir1/file1.ext" of length 21
"dir/subdir2/subsubdir2/file2.ext" of length 32.
We return 32 since it is the longest absolute path to a file.
"""

class Solution:
    def lengthLongestPath(self, input):
        res = 0
        # 用 depth_length_map 保留每层路径的长度，作为前缀和，input.split('\n') 切分为每行分析每行长度与内容
        depth_length_map = {-1: 0}
        for line in input.split('\n'):
            # line.count('\t') 的个数来判断是第几层
            depth = line.count('\t')
            # 每行空格最后要被去掉
            depth_length_map[depth] = depth_length_map[depth - 1] + len(line) - depth
            # line.count('.') 的个数判断是否有文件，有文件获取当前最长路径值
            if line.count('.'):
                # 每层都要添加 depth 个 / ， 长度需要修改变换
                res = max(res, depth_length_map[depth] + depth)
        return res
print("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext".split('\n'))