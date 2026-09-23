// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//     pub val: i32,
//     pub left: Option<Rc<RefCell<TreeNode>>>,
//     pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         TreeNode {
//             val,
//             left: None,
//             right: None,
//         }
//     }
// }

use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn validate(node: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> bool {
        // The current node values must be between the low and the high
        if node.is_none() {
            return true
        }
        let node = node.unwrap();
        let node_ref = node.borrow();
        if low < node_ref.val && node_ref.val < high {
            return Solution::validate(node_ref.left.clone(), low, node_ref.val) && Solution::validate(node_ref.right.clone(), node_ref.val, high)
        }

        return false
    }

    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        if root.is_none() {
            return true
        }
        Solution::validate(root, i32::MIN, i32::MAX)
    }
}
