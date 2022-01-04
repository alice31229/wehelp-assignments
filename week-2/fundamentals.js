// Q1 使用迴圈計算最小值到最大值之間，所有整數的總和
function calculate(min, max){
    // 請用你的程式補完這個函式的區塊
    let addition=0;
    for (let i=min; i<=max; i++){
        addition+=i
    };
    console.log(addition)
};

calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30

///////////

// Q2 正確計算出員工的平均薪資
function avg(data){
    // 請用你的程式補完這個函式的區塊
    let salary_incre=0;
    let salaries=data['employees'];
    for (let item of salaries){
        salary_incre+=item['salary'];
    };
    console.log(salary_incre/data['employees'].length);
};

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
}); // 呼叫 avg 函式

//////////

// Q3 兩兩數字相乘後的最大值
function maxProduct(nums){
    // 請用你的程式補完這個函式的區塊
    let max1=nums[0];
    if (nums.length==2){
        console.log(max1*nums[1]);
    } else if (nums.length>2){
        let pos=[];
        let neg=[];
        let pos_max=0;
        let neg_max=0;

        for (n of nums){
            if (n>=0){
                pos.push(n);
            } else{
                neg.push(n);
            };
        };

        if (pos.length>1){
            let max1=pos[0];
            for (n of pos){
                if (n>=max1){
                    max1=n;
                };
            };
            let d=pos.indexOf(max1);
            pos.splice(d,1);
            let max2=pos[0];
            for (n of pos){
                if (n>=max2){
                    max2=n;
                };
            };
            pos_max=max1*max2;
        };

        if (neg.length>1){
            let max1=neg[0];
            for (n of neg){
                if (-n>=-max1){
                    max1=n;
                };
            };
            let d=neg.indexOf(max1);
            neg.splice(d,1);
            let max2=neg[0];
            for (n of neg){
                if (-n>=-max2){
                    max2=n;
                };
            };
            neg_max=max1*max2;
        };
        if (neg_max>pos_max){
            console.log(neg_max);
        } else{
            console.log(pos_max);
        };
        
    };
    
};
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0
maxProduct([-1,-2,0]) // 得到 2

//////////

// Q4 找出兩個數相加為目標分別的index
function twoSum(nums, target){
    // your code here
    for (item of nums){
        if (nums.indexOf(target-item)>-1){
            let ans=[nums.indexOf(item),nums.indexOf(target-item)];
            return ans
        };
    };
};
let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

//////////

// Q5 計算連續出現 0 的最大長度
function maxZeros(nums){
    // 請用你的程式補完這個函式的區塊
    if (nums.indexOf(0)==-1){
        console.log(0);
    } else if(nums.indexOf(0)>-1){
        let zero_count=0;
        let max_count=0;
        for (zero of nums){
            if (zero==0){
                zero_count+=1;
            }
            else{
                if (zero_count>max_count){
                    max_count=zero_count;
                };
                zero_count=0;
            };
        };
        if (zero_count>max_count){
            max_count=zero_count;
        };
        console.log(max_count);
    };
};
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3

//////////