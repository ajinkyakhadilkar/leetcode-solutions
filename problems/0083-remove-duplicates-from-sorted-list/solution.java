/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(null == head) {
            return head;
        }
        ListNode root = head;
        ListNode tempHead = head;
        int duplicateCheck = head.val;

        while(null != head.next) {
            head = head.next;
            if(tempHead.val != head.val) {
                tempHead.next = head;
                tempHead = head;
            } else{
                continue;
            }
            //head = tempHead;
        }
        tempHead.next = null;
        return root;
    }
}
