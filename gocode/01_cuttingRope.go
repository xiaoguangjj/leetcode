/*
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

package main
import "math"
import "fmt"

func  main() {
	fmt.Printf("绳子段数：%d\n",cuttingRope(10))
}

func cuttingRope(n int) int {
	if n <= 2{
		return 1
	}
	if n == 3{
		return 2
	}
	parts := n / 3
	another := n % 3
	var result float64
	switch another {
		case 2:
			result = math.Pow(3, float64(parts))
			result *= 2
		case 1:
			result = math.Pow(3, float64(parts-1))
			result *= 4
		default:
			result = math.Pow(3, float64(parts))
	}

	return int(result)
}

