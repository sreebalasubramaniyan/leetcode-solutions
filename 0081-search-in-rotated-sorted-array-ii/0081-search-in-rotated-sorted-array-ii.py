class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # There is only propblem we have is 
        # nums[i] = nums[j] = nums[mid]
        # here we don't which part is sorted 
        # My approach 
            # I used tow pointers and left and right
            # move it untill we see other element upto i + 1 and j - 1 respectively
            # and now check the new pointers 
                # if right <= taget <= j -> skip left part
                # else : -> skip right part
        # Optimal / Strivers approach
            # nums[i] = nums[j] = nums[mid]
            # we always check nums[mid] == target and it this case if it's != target 
            # then we don't need that one 
            # so we have to strink the array 
            # by i += 1 and j-=1 continue
            # continue for repited [3,3,3,1,3,3]
        if len(nums) == 1 :
            if nums[0] == target : return True
            else : return False
        else :
            i = 0 ; j =len(nums) - 1 
            while i<=j:
                mid = (i+j) // 2
                if nums[mid] == target or nums[i] == target or nums[j] == target: 
                    return True
                if nums[i] == nums[j] == nums[mid]:
                # My approach
                    # if j==i: return False
                    # left = right = mid
                    # while left - 1 > i and nums[left] == nums[mid] :
                    #     left -= 1
                    # while right + 1 < j and nums[right] == nums[mid] : 
                    #     right += 1
                    # if nums[left] == target or nums[right] == target : return True
                    # if nums[right] <= target <= nums[j] :
                    #         i = right + 1
                    # else : 
                    #         j = left - 1
                # Optimal
                    i += 1 ; j-= 1 ; continue
                #print(left,right)

                
                if nums[i] <= nums[mid] : # -> left part is sorted 
                    if(nums[i] <= target <= nums[mid]): # -> target is in left part 
                        j = mid - 1 # -> skip right part
                    else : # target is not in left part 
                        i = mid + 1 # -> skip left part
                else : #-> right part is sorted 
                    if(nums[mid] <= target <= nums[j]): # -> target in right part 
                        i = mid + 1 # -> skip left part
                    else : # target is not in right part 
                        j = mid - 1 # skip right part
            return False