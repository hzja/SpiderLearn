# 原创
：  【Python】线性规划模型（笔记）

# 【Python】线性规划模型（笔记）

#### 线性规划的作用

求一个线性目标函数在线性可行域内的最值问题

#### 线性规划的典型应用

#### 线性规划的本质

问题是线性的<br/> 约束是线性的

#### 线性代数基本概念

线性代数基本概念：向量

向量的基本运算：<br/> <img alt="![[Pasted image 20240814153235.png]]" src="https://i-blog.csdnimg.cn/direct/ab9066c427114a14ab01cfd15358d34d.png"/>

向量的集合：矩阵<br/> 这里不细讲了，忘了就复习线性代数

### 运用Python进行矩阵运算
1. 首先导入numpy库
```
import numpy as np

```
1. 使用np.array创建矩阵
```
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2],[3,4],[5,6]])
c = np.array([[1,2,3]])
d = np.array([[9,8,7],[3,2,1]])

```
1. 矩阵加法和数乘
```
sum = a + b #加法
e = 3 * a #数乘

```
1. 使用np.dot进行矩阵相乘
```
e = np.dot(a, b)

```
1. 元素乘（要求行列一致）
```
e = a * d

```
1. 矩阵转置
```
e = c.T

```
1. 使用np.linalg.inv求逆
```
result = np.linalg.inv(e)

```
1. 使用np.linalg.det求行列式
```
reslut = np.linalg.det(e)

```
1. 使用np.linalg.matrix_rank求矩阵的秩
```
e = np.linalg.matrix_rank(d)

```

### 运用Python求解一次方程组

例如：<br/>  
      
       
        
        
          { 
         
         
          
           
            
             
             
               10 
              
             
               x 
              
             
               − 
              
             
               y 
              
             
               − 
              
             
               2 
              
             
               z 
              
             
               = 
              
             
            
           
           
            
             
              
             
               72 
              
             
            
           
          
          
           
            
             
             
               − 
              
             
               x 
              
             
               + 
              
             
               10 
              
             
               y 
              
             
               − 
              
             
               2 
              
             
               z 
              
             
               = 
              
             
            
           
           
            
             
              
             
               83 
              
             
            
           
          
          
           
            
             
             
               − 
              
             
               x 
              
             
               − 
              
             
               y 
              
             
               + 
              
             
               5 
              
             
               z 
              
             
               = 
              
             
            
           
           
            
             
              
             
               42 
              
             
            
           
          
         
        
          ) 
         
        
       
         \left\{\begin{aligned} 10 x-y-2 z= &amp; 72 \\ -x+10 y-2 z= &amp; 83 \\ -x-y+5 z= &amp; 42 \end{aligned}\right) 
        
       
     ⎩
⎨
⎧​10x−y−2z=−x+10y−2z=−x−y+5z=​728342​
​

解法：<br/>  
      
       
        
        
          x 
         
        
          = 
         
         
         
           A 
          
          
          
            − 
           
          
            1 
           
          
         
        
          b 
         
        
       
         x=A^{-1} b 
        
       
     x=A−1b

求数值解：使用numpy库

```
import numpy as np  
  
A = np.array([[10, -1, -2], [-1, 10, -2], [-1, -1, 5]])  # A为系数矩阵  
b = np.array([72, 83, 42])  # b为常数列  
inv_A = np.linalg.inv(A)  # 求A的逆矩阵  
x = inv_A.dot(b)  # A的逆矩阵点乘b  
x = np.linalg.solve(A, b)  # 5,6行可用本行替代  
print(x)

```

结果：[11. 12. 13.]

我们还可以使用sympy库求符号解或数值解：

```
from sympy import symbols, Eq, solve  
  
x, y, z = symbols('x y z')  
# 直接写入方程形式
eqs = [Eq(10 * x - y - 2 * z, 72),  
       Eq(-x + 10 * y - 2 * z, 83),  
       Eq(-x - y + 5 * z, 42)]  
print(solve(eqs, [x, y, z]))

```

结果：{x: 11, y: 12, z: 13}

### 从矩阵角度思考线性规划的标准形式
1. 不等式组条件矩阵化1. 方程组条件矩阵化1. 写出变量自身的取值范围1. 把目标函数向量化1. 求极值
用程序做线性规划问题时的规范形式：<br/>  
      
       
        
         
          
           
            
           
          
          
           
            
             
             
              
              
                min 
               
              
                ⁡ 
               
              
             
               x 
              
             
             
             
               c 
              
             
               T 
              
             
            
              x 
             
            
           
          
         
         
          
           
            
           
          
          
           
            
             
            
               s.t.  
             
             
             
               { 
              
              
               
                
                 
                  
                  
                    A 
                   
                  
                    x 
                   
                  
                    ≤ 
                   
                  
                    b 
                   
                  
                 
                
               
               
                
                 
                  
                  
                    A 
                   
                  
                    e 
                   
                  
                    q 
                   
                  
                    ⋅ 
                   
                  
                    x 
                   
                  
                    = 
                   
                  
                    b 
                   
                  
                    e 
                   
                  
                    q 
                   
                  
                 
                
               
               
                
                 
                  
                  
                    l 
                   
                  
                    b 
                   
                  
                    ≤ 
                   
                  
                    x 
                   
                  
                    ≤ 
                   
                  
                    u 
                   
                  
                    b 
                   
                  
                 
                
               
              
             
            
           
          
         
        
       
         \begin{aligned} &amp; \min _x c^T x \\ &amp; \text { s.t. }\left\{\begin{array}{l} A x \leq b \\ A e q \cdot x=b e q \\ l b \leq x \leq u b \end{array}\right. \end{aligned} 
        
       
     ​xmin​cTx s.t. ⎩
⎨
⎧​Ax≤bAeq⋅x=beqlb≤x≤ub​​
1. 求一个线性函数的极小值1. 不等式约束一定是小于等于号
线性规划的三要素：<mark>决策变量、目标函数、约束条件</mark>

### 线性规划的Python程序求解

例：

 
      
       
        
        
          max 
         
        
          ⁡ 
         
         
        
          z 
         
        
          = 
         
        
          2 
         
         
         
           x 
          
         
           1 
          
         
        
          + 
         
        
          3 
         
         
         
           x 
          
         
           2 
          
         
        
          − 
         
        
          5 
         
         
         
           x 
          
         
           3 
          
         
        
       
         \max \quad z=2 x_1+3 x_2-5 x_3 
        
       
     maxz=2x1​+3x2​−5x3​<br/>  
      
       
        
        
          s 
         
        
          . 
         
        
          t 
         
        
          . 
         
         
         
           { 
          
          
           
            
             
              
               
               
                 x 
                
               
                 1 
                
               
              
                + 
               
               
               
                 x 
                
               
                 2 
                
               
              
                + 
               
               
               
                 x 
                
               
                 3 
                
               
              
                = 
               
              
                7 
               
              
             
            
           
           
            
             
              
              
                2 
               
               
               
                 x 
                
               
                 1 
                
               
              
                − 
               
              
                5 
               
               
               
                 x 
                
               
                 2 
                
               
              
                + 
               
               
               
                 x 
                
               
                 3 
                
               
              
                &gt; 
               
              
                = 
               
              
                10 
               
              
             
            
           
           
            
             
              
               
               
                 x 
                
               
                 1 
                
               
              
                + 
               
              
                3 
               
               
               
                 x 
                
               
                 2 
                
               
              
                + 
               
               
               
                 x 
                
               
                 3 
                
               
              
                &lt; 
               
              
                = 
               
              
                12 
               
              
             
            
           
           
            
             
              
               
               
                 x 
                
               
                 1 
                
               
              
                , 
               
               
               
                 x 
                
               
                 2 
                
               
              
                , 
               
               
               
                 x 
                
               
                 3 
                
               
              
                &gt; 
               
              
                = 
               
              
                0 
               
              
             
            
           
          
         
        
       
         s.t. \left\{\begin{array}{l}x_1+x_2+x_3=7 \\ 2 x_1-5 x_2+x_3&gt;=10 \\ x_1+3 x_2+x_3&lt;=12 \\ x_1, x_2, x_3&gt;=0\end{array}\right. 
        
       
     s.t.⎩
⎨
⎧​x1​+x2​+x3​=72x1​−5x2​+x3​&gt;=10x1​+3x2​+x3​&lt;=12x1​,x2​,x3​&gt;=0​

前面提到，规范形式中要求极小值，且不等式约束必须是小于等于号

所以目标函数和第一条不等式需要乘以-1

```
import numpy as np  
from scipy import optimize  
  
# 向量化  
c = np.array([-2, -3, 5])  # 乘以-1变为求极小值  
Aeq = np.array([[1, 1, 1]])  # 方程  
beq = np.array([7])  
A = np.array([[-2, 5, -1], [1, 3, 1]])  # 不等式  
b = np.array([-10, 12])  
x1, x2, x3 = (0, None), (0, None), (0, None) # 范围 
  
res = optimize.linprog(c, A, b, Aeq, beq, bounds=(x1, x2, x3)) # 计算
print(res)

```

结果：

```
message: Optimization terminated successfully. (HiGHS Status 7: Optimal)
        success: True
         status: 0
            fun: -14.571428571428571 # 最优函数值（因为要取最大值所以结果要取fun的相反数）
              x: [ 6.429e+00  5.714e-01  0.000e+00] # x的结果
            nit: 3 # 3轮计算得出结果
          lower:  residual: [ 6.429e+00  5.714e-01  0.000e+00]
                 marginals: [ 0.000e+00  0.000e+00  7.143e+00]
          upper:  residual: [       inf        inf        inf]
                 marginals: [ 0.000e+00  0.000e+00  0.000e+00]
          eqlin:  residual: [ 0.000e+00]
                 marginals: [-2.286e+00]
        ineqlin:  residual: [ 0.000e+00  3.857e+00]
                 marginals: [-1.429e-01 -0.000e+00]
 mip_node_count: 0
 mip_dual_bound: 0.0
        mip_gap: 0.0

```

算法的特性：<mark>输入、输出、有穷性、确定性、可行性</mark>
