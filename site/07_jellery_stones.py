
class Solution(object):
    def numJewelsInStones(self, J, S):
        """

        :param J:
        :param S:
        :return:
        """
        count = 0
        for c in S:
            if c in J:
                count += 1
        return count

    def numJewels_dic(self, J, S):
        """

        :param J:
        :param S:
        :return:
        """
        dic = {key: 0 for key in J}
        print(dic)
        for key in S:
            print(key)
            try:
                dic[key] += 1
            except KeyError:
                continue
            print(dic[key]), '31', key
        return sum(dic.values())

    def numJewelsIn(self, J, S):
        """

        :param J:
        :param S:
        :return:
        """
        return sum(S.count(i) for i in J)

if __name__ == '__main__':
    J = 'aS'
    S = 'PaSSadasffsafssss'
    JS = Solution().numJewelsInStones(J,S)
    print(JS)

    numJS = Solution().numJewels_dic(J, S)
    print(numJS)

    numJSIn = Solution().numJewelsIn(J, S)
    print(numJSIn)