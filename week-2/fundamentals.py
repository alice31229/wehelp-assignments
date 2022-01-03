# Q1 使用迴圈計算最小值到最大值之間，所有整數的總和
def calculate(min, max):
    # 請用你的程式補完這個函式的區塊
    i=min
    for j in range(min+1,max+1):
        i+=j
    print(i)
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

##############

# Q2 正確計算出員工的平均薪資
def avg(data):
    # 請用你的程式補完這個函式的區塊
    incre_salary=0
    for e in data["employees"]:
        incre_salary+=e["salary"]
    print(incre_salary/len(data["employees"]))

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式

##############

# Q3 兩兩數字相乘後的最大值
def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    max1=nums[0]
    
    if len(nums)==2:
        print(max1*nums[1])
    elif len(nums)>2:
        for n in nums:
            if n>=max1:
                max1=n
        nums.remove(max1)
        max2=nums[0]
        for n in nums:
            if n>=max2:
                max2=n
        
        print(max1*max2)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0

###############

# Q4 找出兩個數相加為目標分別的index
def twoSum(nums, target):
    # your code here
    ans=[]
    for i in range(len(nums)):
        if target-nums[i] in nums:
            ans.append(i)
            ans.append(nums.index(target-nums[i]))
            return ans

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

###############

# Q5 計算連續出現 0 的最大長度
def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    if 0 not in nums:
        print(0)
    else:
        zero_count=0
        max_count=0
        for i in nums:
            if i==0:
                zero_count+=1
            else:
                if zero_count>max_count:
                    max_count=zero_count
                zero_count=0
        if zero_count>max_count:
            max_count=zero_count
        print(max_count)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3

###############