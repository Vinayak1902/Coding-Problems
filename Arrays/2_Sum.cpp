class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int,int> indices;
            int n = nums.size();
            for(int i=0;i<n;i++){
                int val = target - nums[i];
                if(indices.find(val)!=indices.end()){
                    return {indices[val],i};
                }
                indices[nums[i]] = i;
            }
            return {-1,-1};
        }
    };