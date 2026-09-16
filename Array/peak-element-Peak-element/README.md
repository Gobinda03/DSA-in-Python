# Peak element

## Problem

Courses

Tutorials

Practice

Jobs

Switch to Dark Mode
45

Menu

Back to Explore Page

Ask A DoubtMy Doubts

FREQUENTLY ASKED QUESTIONS

ProblemEditorialSubmissionsComments

Peak element
Solved

Difficulty: MediumAccuracy: 38.86%Submissions: 652K+Points: 4Average Time: 30m

Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist).

If there are multiple peak elements, Return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".

Note: Consider the element before the first element and the element after the last element to be negative infinity.

Examples :

Input: arr = [1, 2, 4, 5, 7, 8, 3]
Output: true
Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].

Input: arr = [10, 20, 15, 2, 23, 90, 80]
Output: true
Explanation: Element 20 at index 1 is a peak since 10 < 20 > 15. Index 5 (value 90) is also a peak, but returning any one peak index is valid.

Constraints:
1 ≤ arr.size() ≤ 106
-231 ≤ arr[i] < 231

Expected Complexities

Time Complexity: O(log n)
Auxiliary Space: O(1)

Company Tags

AccoliteAmazonVisaAdobeGoogle

Topic Tags

ArraysSearchingBinary Search

Related Interview Experiences

Amazon Interview Experience Set 257 Off Campus

Related Articles

Find A Peak In A Given Array

Discussions ( 1660 Threads )

Commenting as Gobinda HazraComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Sarika Kumar3 weeks agoAug 23, 2026 11:51 (GMT +5:30)

class Solution:
def peakElement(self, arr):
for i in range(len(arr)-1):
if arr[i] < arr[i+1] and arr[i+1] >arr[i+2]:
print(i+1)
break

0

Reply
(Show 1 Replies)

Anjali Gupta3 weeks agoAug 20, 2026 10:20 (GMT +5:30)

class Solution {
public:
int peakElement(vector<int> &arr) {
// code here
int s =0;
int e = arr.size()-1;
int mid;
while(s<e){
mid=s+(e-s)/2;
if(arr[mid]<arr[mid+1]){
s=mid+1;
}
else{
e=mid;
}

}
return s;
}
};

0

Reply

VINIT KUMAR4 weeks agoAug 18, 2026 23:26 (GMT +5:30)

while(lo<hi) {
int mid=(lo+hi)/2;
if(arr[mid]>arr[mid+1]) hi=mid;
else lo=mid+1;
}
return lo;

0

Reply

Anonymous_Geek1 month agoJul 31, 2026 10:49 (GMT +5:30)

class Solution {
public:
int peakElement(vector<int> &arr) {
// code here
int n=arr.size();
int i=0;
while(arr[i]<arr[i+1]&&i<n-1){i++;}

return i;
}
};

0

Reply

Anonymous_Geek1 month agoJul 31, 2026 10:33 (GMT +5:30)

class Solution {
public:
int peakElement(vector<int> &arr) {
// code here
int n=arr.size();
for(int i=0;i<n;i++){
if((i==0||arr[i]>arr[i-1])&&(i==n-1||arr[i]>arr[i+1])){
return i;
}
}
return -1;
}
};

0

Reply

Shubham Kumar2 months agoJul 18, 2026 20:51 (GMT +5:30)

class Solution {
public int peakElement(int[] arr) {
// code here
int start = 0 , end = arr.length-1;
while(start<end){
int mid = (start+end)/2;
if(arr[mid]<arr[mid+1]){
start = mid+1;
}else{
end = mid;
}

}
return start;

}
}

2

Reply

Sai Kiran Ganta2 months agoJul 10, 2026 18:50 (GMT +5:30)

test cases are invalid for the problem

2

Reply

Shivanshu Srivastava(Edited)02/07/2026, 01:51
2 months agoJul 02, 2026 01:46 (GMT +5:30)

int n=arr.size();
int low=1;
int high=n-2;
if(n==1) return 0;
if(arr[0]>arr[1]) return 0;
else if(arr[n-1]>arr[n-2]) return n-1;
while(low<=high){
int mid=low+(high-low)/2;
if(arr[mid]>arr[mid+1] && arr[mid]>arr[mid-1]) return mid;
else if(arr[mid]<arr[mid+1]) low=mid+1;
else high=mid-1;
}
return -1;                                                                                                                                                                                     In this approach when we are deciding whether peak will be on left or right we are checking by if (arr[mid]<arr[mid+1]). This approach because if this condition is satisfied there will be atleast the last element which will be the peak and same for first element.

0

Reply

Shivanshu Srivastava2 months agoJul 02, 2026 01:46 (GMT +5:30)

int n=arr.size();
int low=1;
int high=n-2;
if(n==1) return 0;
if(arr[0]>arr[1]) return 0;
else if(arr[n-1]>arr[n-2]) return n-1;
while(low<=high){
int mid=low+(high-low)/2;
if(arr[mid]>arr[mid+1] && arr[mid]>arr[mid-1]) return mid;
else if(arr[mid]<arr[mid+1]) low=mid+1;
else high=mid-1;
}
return -1;

0

Reply

BODDU NEHRU2 months agoJul 01, 2026 11:08 (GMT +5:30)

class Solution:
def peakElement(self, arr):
low = 0
high = len(arr) - 1

while low <= high:
mid = (low + high) // 2

# Check if mid is a peak element
if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
return mid

# If the left neighbor is greater, the peak lies in the left half
if mid > 0 and arr[mid - 1] > arr[mid]:
high = mid - 1
else:  # Else, the peak lies in the right half
low = mid + 1

return -1  # This case will never be reached

1

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total2 / 2Accuracy : 100%

Time Taken0.44

You get marks only for the first correct submission if you solve the problem without viewing the full solution.

Python3
C (gcc 5.4)
C++ (17)
Java (21)
Python3
C#
Javascript (Node v22)

Editor Settings
Font Size
Theme

Choose Your Preferred font For The Code Editor
12px13px14px15px16px18px20px22px

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27

class Solution:
def peakElement(self, arr):
n = len(arr)
# single element array, so that's my peak element
if n == 1:
return 0
# first element is peak
if arr[0]> arr[1]:
return 0
# last element is peak
if arr[n-1] > arr[n-2]:
return n-1

low, high = 1, n-2

while low <= high:
mid = (low + high)//2

# chech whether mid element is peak or not
if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
return mid

# if mid is lesser than next element then there might be peak on right side
if arr[mid] < arr[mid+1]:
low = mid + 1
else:
high = mid - 1

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total2 / 2Accuracy : 100%

Time Taken0.44

You get marks only for the first correct submission if you solve the problem without viewing the full solution.

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Peak element](https://www.geeksforgeeks.org/problems/peak-element/1)
