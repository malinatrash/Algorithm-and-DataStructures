package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getMinimumDifference(root *TreeNode) int {
	min := 99999999

	curr := root
	for curr != nil {
		if curr.Left == nil {
			break
		}
		difL := int(math.Abs(float64(curr.Val - curr.Left.Val)))
		println(difL)
		if difL < min {
			min = difL
		}
		curr = curr.Left
	}
	return min
}

func main() {
	root := TreeNode{
		Val: 4,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val:   1,
				Left:  nil,
				Right: nil,
			},
			Right: &TreeNode{
				Val:   3,
				Left:  nil,
				Right: nil,
			},
		},
		Right: &TreeNode{
			Val:   1,
			Left:  nil,
			Right: nil,
		},
	}
	fmt.Println(getMinimumDifference(&root))
}
