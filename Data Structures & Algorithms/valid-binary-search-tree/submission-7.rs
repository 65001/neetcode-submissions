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
    pub fn validate(node: &Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> bool {
        // The current node values must be between the low and the high
        match node {
            Some(node) => {
                let node_ref = node.borrow();
                let node_val : i32 = node_ref.val;
                return low < node_val && node_val < high  && Solution::validate(&node_ref.left, low, node_val) && Solution::validate(&node_ref.right, node_val, high)
            },
            None => return true
        }
    }

    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Solution::validate(&root, i32::MIN, i32::MAX)
    }
}
