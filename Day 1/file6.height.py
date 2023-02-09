def max_area(hegith):
    left,right=0,len(height)-1
    max_area=0
    while left <right:
        max_area=max(max_area,min(height[left],height[right])*(right-left))
        if hegiht[left]<height[right]:
            left+=1
        else:
            right-=1
    return max_area
height=[int(x) for x in input("Enter the height of the lines separated by space:").split()]
result=max_area(height)
print("The maximum area that can be contained is:",result)
                
