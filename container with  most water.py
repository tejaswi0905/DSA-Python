height = [1,8,6,2,5,4,8,3,7]
area = 0
i = 0
j = len(height)-1
while(i<j):
    if height[i]<=height[j]:
        area1 = height[i]*(j-i)
        if area1 > area:
            area = area1
        i+=1
    if height[j]<=height[i]:
        area1 = height[j]*(j-i)
        if area1 > area:
            area = area1
        j-=1
print(area)