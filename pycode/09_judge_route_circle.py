# coding=utf-8


class Solution(object):
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U':
                y -= 1
            elif move == 'D':
                y += 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        print(x,y)
        # if x == 0 and y ==0:
        #     return True
        # else:
        #     return False
        return x == y == 0

if __name__=='__main__':
    moves = ['U', 'D', 'L', 'R']
    So = Solution().judgeCircle(moves)
    # print(So)
    print('z'<'a')