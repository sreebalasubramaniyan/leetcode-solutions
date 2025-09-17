class Solution(object):
    def nextGreaterElements(self, nums):
        """
        1 2 1 1 2 1 
          1 
          
        so basically we have advantage that we can see the greater ele rotationally
        means be can check both front and back sind eo the elements 

        so will extend the array twise (assume like a strightened circle)
        
        traverese from the reverse(extended) from 2n-1 to n
        just call this as a pre looked
            means we are check any element greater(not neccssarily) for the n-1'th element

 

        so the actuall search is start from n-1 th element so   

        now we are checking for the next greater elem in the ranger [0,n-1] it may be in [n,2n-1]
        also (cuz it didn't poped during the first traversal)
        
            and when ever you got the greater element at the stack put in the ans and pop 

            if lesser and pop upto valid and again put it into ans

            if stack is empty then just put -1 (no greater element)


        """
        stack = [] ; n = len(nums)
        ans  = [-1 for _ in range(n)]
        for i in range(2*n-1,-1,-1):
           
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if i <= n-1:
                if stack : 
                    ans[i] = stack[-1]
            stack.append(nums[i%n])
        return ans 